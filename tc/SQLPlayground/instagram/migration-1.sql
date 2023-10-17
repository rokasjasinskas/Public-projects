CREATE TABLE comment_backup AS SELECT * FROM comment;

DROP TABLE comment;

CREATE TABLE comment (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    post_id INTEGER NOT NULL,
    text VARCHAR NOT NULL,
    created_at TIMESTAMP NOT NULL,
    reply_comment_id INTEGER,
    FOREIGN KEY(reply_comment_id) REFERENCES comment(id)
);

INSERT INTO comment SELECT * FROM comment_backup;

DROP TABLE comment_backup;