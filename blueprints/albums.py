"""Create, Read, Update and Delete over the albums table.

Based on the examples.py blueprint formatting - one file per feature, every
query written out in full instead of hidden behind helper functions.
"""

from flask import Blueprint, flash, redirect, render_template, request, url_for

from database import get_connection

albums_bp = Blueprint("albums", __name__)


@albums_bp.route("/albums")
def albums():
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT id, title, release_year, record_label, "
            "copies_sold_millions, description "
            "FROM albums ORDER BY release_year ASC"
        )
        rows = cursor.fetchall()
    finally:
        # Always in a finally block. Every request opens its own connection, so
        # one that is never closed stays open on a server the whole class
        # shares.
        conn.close()
    return render_template("albums.html", albums=rows)


@albums_bp.route("/albums/add", methods=["POST"])
def add_album():
    title = request.form.get("title", "").strip()
    release_year = request.form.get("release_year", "").strip()
    record_label = request.form.get("record_label", "").strip()
    copies_sold_millions = request.form.get("copies_sold_millions", "").strip()
    description = request.form.get("description", "").strip()

    if not title or not release_year:
        flash("Title and release year are required.", "danger")
        return redirect(url_for("albums.albums"))

    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        # %s is the placeholder. Never build SQL by joining strings together or
        # with an f-string - that is how SQL injection gets in.
        cursor.execute(
            "INSERT INTO albums "
            "(title, release_year, record_label, copies_sold_millions, description) "
            "VALUES (%s, %s, %s, %s, %s)",
            (title, release_year, record_label, copies_sold_millions or None, description),
        )
        conn.commit()
    finally:
        conn.close()

    flash(f"Added {title}.", "success")
    return redirect(url_for("albums.albums"))


@albums_bp.route("/albums/edit/<int:album_id>", methods=["POST"])
def edit_album(album_id):
    title = request.form.get("title", "").strip()
    release_year = request.form.get("release_year", "").strip()
    record_label = request.form.get("record_label", "").strip()
    copies_sold_millions = request.form.get("copies_sold_millions", "").strip()
    description = request.form.get("description", "").strip()

    if not title or not release_year:
        flash("Title and release year are required.", "danger")
        return redirect(url_for("albums.albums"))

    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "UPDATE albums SET title = %s, release_year = %s, record_label = %s, "
            "copies_sold_millions = %s, description = %s WHERE id = %s",
            (title, release_year, record_label, copies_sold_millions or None, description, album_id),
        )
        conn.commit()
    finally:
        conn.close()

    flash(f"Updated {title}.", "success")
    return redirect(url_for("albums.albums"))


@albums_bp.route("/albums/delete/<int:album_id>", methods=["POST"])
def delete_album(album_id):
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("DELETE FROM albums WHERE id = %s", (album_id,))
        conn.commit()
    finally:
        conn.close()

    flash("Deleted.", "success")
    return redirect(url_for("albums.albums"))
