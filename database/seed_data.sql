-- Starting rows, so the Albums page has something to show before you have
-- added anything yourself. Safe to run more than once only if you clear the
-- table first - these do not check for duplicates.
--
-- Michael Jackson's solo studio albums. Sales figures are widely cited
-- estimates (RIAA/industry reporting), rounded to one decimal place.

INSERT INTO albums (title, release_year, record_label, copies_sold_millions, description) VALUES
    ('Got to Be There', 1972, 'Motown', 3.7, 'His first solo studio album, released while still a member of the Jackson 5.'),
    ('Ben', 1972, 'Motown', 2.2, 'Title track became his first US #1 solo single.'),
    ('Music & Me', 1973, 'Motown', 0.2, 'Modest commercial performance compared to his earlier solo releases.'),
    ('Forever, Michael', 1975, 'Motown', 0.2, 'His final album for Motown before moving to Epic.'),
    ('Off the Wall', 1979, 'Epic', 20.0, 'First collaboration with producer Quincy Jones; four US top-10 singles.'),
    ('Thriller', 1982, 'Epic', 70.0, 'The best-selling album of all time.'),
    ('Bad', 1987, 'Epic', 45.0, 'First album with five US #1 singles.'),
    ('Dangerous', 1991, 'Epic', 32.0, 'First album without Quincy Jones as producer, working instead with Teddy Riley.'),
    ('HIStory: Past, Present and Future, Book I', 1995, 'Epic', 20.0, 'Double album pairing a greatest-hits disc with a disc of new material.'),
    ('Invincible', 2001, 'Epic', 13.0, 'His final studio album released during his lifetime.');
