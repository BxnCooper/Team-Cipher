# Team Cipher Database Setup

A beginner-friendly SQLite 3 database for the Team Cipher marketplace application.

## 📁 Folder Structure

```
database/
├── __init__.py          # Makes database a Python package
├── db.py                # Main database functions
├── schema.sql           # Table definitions
├── main.py              # Test script
└── team_cipher.db       # Actual database file (created automatically)
```

## 🗄️ What is SQLite?

**SQLite** is a lightweight database that stores data in a single file instead of requiring a separate server. Perfect for learning and small projects!

**Key Points:**
- No server needed - just a `.db` file
- Easy to understand and use
- Great for prototyping before moving to larger databases

## 📊 Database Tables

### 1. **users** - Store user information
```
id          | username | email           | password    | created_at
1           | binita   | binita@ex.com   | hash12345   | 2026-03-26...
2           | john     | john@ex.com     | hash67890   | 2026-03-26...
```

### 2. **listings** - Store items for sale
```
id | user_id | title      | price | category    | status
1  | 1       | iPhone 14  | 800   | electronics | active
2  | 2       | Desk       | 150   | furniture   | active
```

### 3. **messages** - Store messages between users
```
id | sender_id | receiver_id | message | created_at
1  | 1         | 2           | Hi!     | 2026-03-26...
```

### 4. **favorites** - Store user's favorite listings
```
id | user_id | listing_id | created_at
1  | 1       | 5          | 2026-03-26...
```

### 5. **reviews** - Store reviews/ratings
```
id | reviewer_id | reviewed_user_id | rating | comment
1  | 1           | 2                | 5      | Great seller!
```

## 🚀 Quick Start

### 1. Initialize the Database

```python
from database import initialize_db

# Run this once to create all tables
initialize_db()
```

This creates the `team_cipher.db` file with all the tables defined in `schema.sql`.

### 2. Add a User

```python
from database import add_user

user_id = add_user("binita", "binita@example.com", "password123")
print(f"User created with ID: {user_id}")
```

### 3. Get All Users

```python
from database import get_users

users = get_users()
for user in users:
    print(f"{user['username']} - {user['email']}")
```

### 4. Add a Listing

```python
from database import add_listing

listing_id = add_listing(
    user_id=1,
    title="iPhone 14",
    description="Good condition",
    price=800.00,
    category="electronics"
)
```

### 5. Run the Test Script

```bash
cd database
python main.py
```

This will:
- Initialize the database
- Create test users
- Create test listings
- Show you all the data

## 📚 Available Functions

### User Operations
```python
add_user(username, email, password)           # Create new user
get_users()                                    # Get all users
get_user_by_id(user_id)                      # Get specific user by ID
get_user_by_username(username)                # Get user by username
update_user(user_id, username, email, password)  # Update user
delete_user(user_id)                          # Delete user
```

### Listing Operations
```python
add_listing(user_id, title, description, price, category)  # Create listing
get_listings()                                 # Get all listings
get_listing_by_id(listing_id)                 # Get specific listing
get_user_listings(user_id)                    # Get user's listings
update_listing(listing_id, ...)               # Update listing
delete_listing(listing_id)                    # Delete listing
```

## 🔑 How It Works - Under the Hood

### `db.py` - The Main File

This file contains all the database functions. Here's what happens:

#### 1. **Connection Function**
```python
def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Makes rows act like dictionaries
    return conn
```
- Creates a connection to the database file
- `row_factory` makes results easier to work with

#### 2. **Database Initialization**
```python
def initialize_db():
    conn = get_connection()
    # Read schema.sql
    # Execute all SQL commands
    # Create tables
```
- Reads the `schema.sql` file
- Creates all tables if they don't exist
- Run this once when your app starts

#### 3. **SQL Queries**
```python
cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", (username, email))
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
```
- `?` are placeholders for safety (prevents SQL injection)
- Variables go in the second argument as a tuple

## 🛡️ Security Best Practices

### ⚠️ IMPORTANT: Password Hashing

**Current Code:** Stores passwords as plain text ❌

```python
add_user("binita", "binita@example.com", "password123")  # NOT SAFE!
```

**What You Should Do:** Hash passwords before storing ✅

```python
from werkzeug.security import generate_password_hash

password_hash = generate_password_hash("password123")
add_user("binita", "binita@example.com", password_hash)
```

### SQL Injection Prevention

✅ **GOOD** - Using placeholders (safe):
```python
cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
```

❌ **BAD** - String concatenation (unsafe):
```python
cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
```

## 📝 SQL Explained (For Beginners)

### SELECT - Get data
```sql
SELECT * FROM users;                    -- Get all users
SELECT id, username FROM users;         -- Get specific columns
SELECT * FROM users WHERE id = 1;       -- Get user with id=1
```

### INSERT - Add data
```sql
INSERT INTO users (username, email, password) 
VALUES ('john', 'john@ex.com', 'pass123');
```

### UPDATE - Change data
```sql
UPDATE users SET email = 'newemail@ex.com' WHERE id = 1;
```

### DELETE - Remove data
```sql
DELETE FROM users WHERE id = 1;
```

### JOIN - Connect tables
```sql
SELECT listings.title, users.username
FROM listings
JOIN users ON listings.user_id = users.id;
```

## 🐛 Troubleshooting

### Database file already exists
```
Remove or rename team_cipher.db and run initialize_db() again
```

### "No module named database"
```
Make sure you're in the parent directory (Team-Cipher/)
Not in the database/ folder
```

### Import errors
```
Make sure __init__.py exists in the database folder
```

## 🔄 Integration with Flask Backend

In `backend/app.py`:

```python
from database import get_users, add_user, initialize_db

# Initialize database when app starts
initialize_db()

@app.route('/api/users', methods=['GET'])
def list_users():
    users = get_users()
    return jsonify(users)

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    user_id = add_user(data['username'], data['email'], data['password'])
    return jsonify({'id': user_id})
```

## 📖 Next Steps

1. ✅ Run `python main.py` to test the database
2. ✅ Connect it to your Flask backend (`backend/app.py`)
3. ✅ Add more functions as needed (messages, reviews, favorites, etc.)
4. ✅ Implement password hashing with `werkzeug`
5. ✅ Add data validation and error handling

## 📚 References

- [SQLite Documentation](https://www.sqlite.org/lang.html)
- [Python sqlite3 Module](https://docs.python.org/3/library/sqlite3.html)
- [SQL Tutorial](https://www.w3schools.com/sql/)

---

**Questions?** Add more functions to `db.py` following the same pattern!
