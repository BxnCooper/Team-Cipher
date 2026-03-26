# Database Quick Reference Guide

Quick copy-paste examples for common database operations.

## Users

### Add a new user
```python
from database import add_user

user_id = add_user("username", "email@example.com", "password")
```

### Get all users
```python
from database import get_users

users = get_users()
for user in users:
    print(user['username'])
```

### Get a specific user
```python
from database import get_user_by_id

user = get_user_by_id(1)
print(user['email'])
```

### Get user by username (for login)
```python
from database import get_user_by_username

user = get_user_by_username("binita")
if user and check_password(user['password'], input_password):
    # Login successful
    pass
```

### Update user
```python
from database import update_user

update_user(1, email="newemail@example.com")
```

### Delete user
```python
from database import delete_user

delete_user(1)
```

## Listings

### Create a listing
```python
from database import add_listing

listing_id = add_listing(
    user_id=1,
    title="iPhone 14",
    description="Good condition, barely used",
    price=800.00,
    category="electronics"
)
```

### Get all listings
```python
from database import get_listings

listings = get_listings()
for listing in listings:
    print(f"{listing['title']} - ${listing['price']}")
```

### Get specific listing
```python
from database import get_listing_by_id

listing = get_listing_by_id(5)
print(listing['description'])
```

### Get user's listings
```python
from database import get_user_listings

my_listings = get_user_listings(1)
for listing in my_listings:
    print(listing['title'])
```

### Update listing
```python
from database import update_listing

update_listing(5, price=750.00)
```

### Delete listing
```python
from database import delete_listing

delete_listing(5)
```

## Testing

### Run the test script
```bash
cd database
python main.py
```

### Reset database (delete and recreate)
```bash
# 1. Delete team_cipher.db file
# 2. Run initialize_db() again
```

## Common Patterns

### Check if item exists
```python
from database import get_user_by_id

user = get_user_by_id(1)
if user:
    print("User found!")
else:
    print("User not found")
```

### Loop through results
```python
from database import get_listings

listings = get_listings()
for listing in listings:
    print(f"ID: {listing['id']}, Title: {listing['title']}")
```

### Count rows
```python
from database import get_users

users = get_users()
user_count = len(users)
```

### Error handling
```python
from database import add_user

try:
    user_id = add_user("binita", "binita@example.com", "pass123")
    if user_id:
        print("User created successfully!")
    else:
        print("Failed to create user")
except Exception as e:
    print(f"Error: {e}")
```

## Flask Integration Examples

### Route to get all users
```python
@app.route('/api/users', methods=['GET'])
def get_all_users():
    from database import get_users
    users = get_users()
    return jsonify(users)
```

### Route to get user by ID
```python
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    from database import get_user_by_id
    user = get_user_by_id(user_id)
    if user:
        return jsonify(user)
    return jsonify({'error': 'User not found'}), 404
```

### Route to create user
```python
@app.route('/api/users', methods=['POST'])
def create_user():
    from database import add_user
    data = request.json
    user_id = add_user(
        data['username'],
        data['email'],
        data['password']
    )
    if user_id:
        return jsonify({'id': user_id}), 201
    return jsonify({'error': 'Failed to create user'}), 400
```

### Route to get listings
```python
@app.route('/api/listings', methods=['GET'])
def get_all_listings():
    from database import get_listings
    listings = get_listings()
    return jsonify(listings)
```

### Route to create listing
```python
@app.route('/api/listings', methods=['POST'])
def create_listing():
    from database import add_listing
    data = request.json
    listing_id = add_listing(
        user_id=data['user_id'],
        title=data['title'],
        description=data['description'],
        price=data['price'],
        category=data['category']
    )
    if listing_id:
        return jsonify({'id': listing_id}), 201
    return jsonify({'error': 'Failed to create listing'}), 400
```

---

**Need more functions?** Add them to `db.py` following the same pattern!
