CREATE TABLE comment_backup AS SELECT * FROM comment;

DROP TABLE comment;

CREATE TABLE comment (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    post_id INTEGER,
    text VARCHAR NOT NULL,
    created_at TIMESTAMP NOT NULL,
    reply_comment_id INTEGER,
    likes_id INTEGER,
    FOREIGN KEY(reply_comment_id) REFERENCES comment(id),
    FOREIGN KEY(likes_id) REFERENCES likes(id)

);

INSERT INTO comment SELECT * FROM comment_backup;

DROP TABLE comment_backup;




CREATE TABLE likes_backup AS SELECT * FROM likes;

DROP TABLE likes;

CREATE TABLE likes (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    post_id INTEGER,

    UNIQUE (user_id, post_id), -- Ensures a user can like a post only once
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (post_id) REFERENCES post(id)
);

INSERT INTO likes SELECT * FROM likes_backup;

DROP TABLE likes_backup;
