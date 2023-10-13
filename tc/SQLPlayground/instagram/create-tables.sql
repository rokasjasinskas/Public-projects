-- users table
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username VARCHAR NOT NULL UNIQUE,
    email VARCHAR NOT NULL UNIQUE,
    password VARCHAR NOT NULL
);

-- post table
CREATE TABLE post (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    image_url TEXT NOT NULL, -- SQLite doesn't have a URL datatype, so TEXT is used
    caption VARCHAR,
    created_at TIMESTAMP NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- comment table
CREATE TABLE comment (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    post_id INTEGER NOT NULL,
    text VARCHAR NOT NULL,
    created_at TIMESTAMP NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (post_id) REFERENCES post(id)
);

-- likes table
CREATE TABLE likes (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    post_id INTEGER NOT NULL,
    UNIQUE (user_id, post_id), -- Ensures a user can like a post only once
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (post_id) REFERENCES post(id)
);

-- followers table
CREATE TABLE followers (
    follower_id INTEGER NOT NULL,
    followee_id INTEGER NOT NULL,
    PRIMARY KEY (follower_id, followee_id), -- Composite primary key
    FOREIGN KEY (follower_id) REFERENCES users(id),
    FOREIGN KEY (followee_id) REFERENCES users(id)
);

-- message table
CREATE TABLE message (
    id INTEGER PRIMARY KEY,
    sender_id INTEGER NOT NULL,
    receiver_id INTEGER NOT NULL,
    text VARCHAR NOT NULL,
    created_at TIMESTAMP NOT NULL,
    FOREIGN KEY (sender_id) REFERENCES users(id),
    FOREIGN KEY (receiver_id) REFERENCES users(id)
);
