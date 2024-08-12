import sqlite3

def create_tables():
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    
    # Create Users table
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    ''')

    # Create Posts table
    c.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            content TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        )
    ''')
    
    conn.commit()
    conn.close()

def insert_user(name, email):
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Error: Email already exists.")
    conn.close()

def insert_post(user_id, title, content):
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    c.execute("INSERT INTO posts (user_id, title, content) VALUES (?, ?, ?)", (user_id, title, content))
    conn.commit()
    conn.close()

def fetch_users():
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    conn.close()
    return users

def fetch_posts_by_user(user_id):
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    c.execute("SELECT * FROM posts WHERE user_id = ?", (user_id,))
    posts = c.fetchall()
    conn.close()
    return posts

def update_user_email(user_id, new_email):
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    try:
        c.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Error: Email already exists.")
    conn.close()

def delete_user(user_id):
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()

if __name__ == "__main__":

    """
    Demonstrates the use of SQLite with Python by managing users and posts
    in a simple blog system.

    - Creates the `users` and `posts` tables.
    - Inserts two users into the `users` table.
    - Inserts posts associated with the users into the `posts` table.
    - Fetches and displays all users from the `users` table.
    - Fetches and displays all posts associated with a specific user.
    - Updates the email address of a user.
    - Deletes a user and demonstrates cascading delete functionality.
    """

    create_tables()

    insert_user("Alice", "alice@example.com")
    insert_user("Bob", "bob@example.com")

    insert_post(1, "Alice's First Post", "This is the content of Alice's first post.")
    insert_post(2, "Bob's First Post", "This is the content of Bob's first post.")
    insert_post(1, "Alice's Second Post", "This is the content of Alice's second post.")

    users = fetch_users()
    print("Users:")
    for user in users:
        print(user)

    alice_posts = fetch_posts_by_user(1)
    print("\nAlice's Posts:")
    for post in alice_posts:
        print(post)

    update_user_email(1, "alice_new@example.com")

    print("\nUsers after email update:")
    users = fetch_users()
    for user in users:
        print(user)

    delete_user(2)

    print("\nUsers after deleting Bob:")
    users = fetch_users()
    for user in users:
        print(user)
