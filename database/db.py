import sqlite3
import os
from pathlib import Path

# Get the database file path - stores 'team_cipher.db' in the database folder
DB_PATH = os.path.join(os.path.dirname(__file__), 'team_cipher.db')


def get_connection():
    """
    Create and return a database connection.
    
    This function:
    - Connects to the SQLite database
    - Sets row_factory so results come back as dictionaries (easier to work with)
    - Returns the connection object
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # This makes rows act like dictionaries
    return conn


def initialize_db():
    """
    Initialize the database by creating all tables if they don't exist.
    
    This function:
    - Reads the schema.sql file
    - Executes all SQL commands to create tables
    - Should be called once when the app starts
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    # Read the schema.sql file
    schema_path = os.path.join(os.path.dirname(__file__), 'schema.sql')
    with open(schema_path, 'r') as f:
        schema = f.read()
    
    # Execute all SQL commands from schema.sql
    cursor.executescript(schema)
    conn.commit()
    conn.close()
    print("✓ Database initialized successfully!")


# =====================
# USERS TABLE FUNCTIONS
# =====================

def add_user(username, email, password):
    """
    Add a new user to the database.
    
    Args:
        username: User's username (must be unique)
        email: User's email address
        password: User's password (IMPORTANT: should be hashed in production!)
    
    Returns:
        The user ID if successful, None if there was an error
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
            (username, email, password)
        )
        
        conn.commit()
        user_id = cursor.lastrowid
        conn.close()
        return user_id
    except sqlite3.IntegrityError as e:
        print(f"Error adding user: {e}")
        return None


def get_users():
    """
    Get all users from the database.
    
    Returns:
        A list of all users as dictionaries
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    
    conn.close()
    # Convert sqlite3.Row objects to dictionaries
    return [dict(user) for user in users]


def get_user_by_id(user_id):
    """
    Get a specific user by their ID.
    
    Args:
        user_id: The ID of the user to retrieve
    
    Returns:
        A dictionary with user data, or None if not found
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    
    conn.close()
    return dict(user) if user else None


def get_user_by_username(username):
    """
    Get a specific user by their username (useful for login).
    
    Args:
        username: The username to search for
    
    Returns:
        A dictionary with user data, or None if not found
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    
    conn.close()
    return dict(user) if user else None


def update_user(user_id, username=None, email=None, password=None):
    """
    Update user information.
    
    Args:
        user_id: The ID of the user to update
        username: New username (optional)
        email: New email (optional)
        password: New password (optional)
    
    Returns:
        True if successful, False otherwise
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # Build the update query dynamically
        updates = []
        params = []
        
        if username is not None:
            updates.append("username = ?")
            params.append(username)
        if email is not None:
            updates.append("email = ?")
            params.append(email)
        if password is not None:
            updates.append("password = ?")
            params.append(password)
        
        if not updates:
            return False
        
        params.append(user_id)
        query = f"UPDATE users SET {', '.join(updates)} WHERE id = ?"
        cursor.execute(query, params)
        
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Error updating user: {e}")
        return False


def delete_user(user_id):
    """
    Delete a user from the database.
    
    Args:
        user_id: The ID of the user to delete
    
    Returns:
        True if successful, False otherwise
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Error deleting user: {e}")
        return False


# =====================
# LISTINGS TABLE FUNCTIONS
# =====================

def add_listing(user_id, title, description, price, category):
    """
    Add a new listing (for-sale item).
    
    Args:
        user_id: ID of the user creating the listing
        title: Title of the listing
        description: Detailed description
        price: Price of the item
        category: Category (e.g., "electronics", "furniture", etc.)
    
    Returns:
        The listing ID if successful, None if there was an error
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute(
            "INSERT INTO listings (user_id, title, description, price, category) VALUES (?, ?, ?, ?, ?)",
            (user_id, title, description, price, category)
        )
        
        conn.commit()
        listing_id = cursor.lastrowid
        conn.close()
        return listing_id
    except Exception as e:
        print(f"Error adding listing: {e}")
        return None


def get_listings():
    """Get all listings from the database."""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM listings")
    listings = cursor.fetchall()
    
    conn.close()
    return [dict(listing) for listing in listings]


def get_listing_by_id(listing_id):
    """Get a specific listing by ID."""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM listings WHERE id = ?", (listing_id,))
    listing = cursor.fetchone()
    
    conn.close()
    return dict(listing) if listing else None


def get_user_listings(user_id):
    """Get all listings created by a specific user."""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM listings WHERE user_id = ?", (user_id,))
    listings = cursor.fetchall()
    
    conn.close()
    return [dict(listing) for listing in listings]


def update_listing(listing_id, title=None, description=None, price=None, category=None):
    """Update listing information."""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        updates = []
        params = []
        
        if title is not None:
            updates.append("title = ?")
            params.append(title)
        if description is not None:
            updates.append("description = ?")
            params.append(description)
        if price is not None:
            updates.append("price = ?")
            params.append(price)
        if category is not None:
            updates.append("category = ?")
            params.append(category)
        
        if not updates:
            return False
        
        params.append(listing_id)
        query = f"UPDATE listings SET {', '.join(updates)} WHERE id = ?"
        cursor.execute(query, params)
        
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Error updating listing: {e}")
        return False


def delete_listing(listing_id):
    """Delete a listing from the database."""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM listings WHERE id = ?", (listing_id,))
        
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Error deleting listing: {e}")
        return False