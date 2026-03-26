"""
Database Test Script - Team Cipher
==================================

This script demonstrates how to use the database functions.
Run this to test that your database is working correctly.

To run this file:
    cd database
    python main.py
"""

from db import (
    initialize_db, 
    add_user, 
    get_users, 
    get_user_by_username,
    add_listing,
    get_listings,
    get_user_listings
)

if __name__ == "__main__":
    print("=" * 50)
    print("Team Cipher Database Test")
    print("=" * 50)
    
    # 1. Initialize the database (creates tables)
    print("\n1. Initializing database...")
    initialize_db()
    
    # 2. Add some test users
    print("\n2. Adding test users...")
    user1_id = add_user("binita", "binita@example.com", "password123")
    user2_id = add_user("john", "john@example.com", "password456")
    
    if user1_id:
        print(f"   ✓ User 'binita' created with ID: {user1_id}")
    if user2_id:
        print(f"   ✓ User 'john' created with ID: {user2_id}")
    
    # 3. Get all users
    print("\n3. Getting all users...")
    users = get_users()
    for user in users:
        print(f"   - {user['username']} ({user['email']})")
    
    # 4. Get a specific user
    print("\n4. Getting user by username...")
    user = get_user_by_username("binita")
    if user:
        print(f"   Found: {user['username']} - {user['email']}")
    
    # 5. Add listings
    if user1_id and user2_id:
        print("\n5. Adding listings...")
        listing1 = add_listing(
            user_id=user1_id,
            title="iPhone 14",
            description="Excellent condition, barely used",
            price=800.00,
            category="electronics"
        )
        
        listing2 = add_listing(
            user_id=user2_id,
            title="Wooden Table",
            description="Antique wooden dining table",
            price=150.00,
            category="furniture"
        )
        
        if listing1:
            print(f"   ✓ Listing created: 'iPhone 14' (ID: {listing1})")
        if listing2:
            print(f"   ✓ Listing created: 'Wooden Table' (ID: {listing2})")
    
    # 6. Get all listings
    print("\n6. Getting all listings...")
    listings = get_listings()
    for listing in listings:
        print(f"   - {listing['title']} (${listing['price']}) - {listing['category']}")
    
    # 7. Get user's listings
    if user1_id:
        print(f"\n7. Getting listings from user {user1_id}...")
        user_listings = get_user_listings(user1_id)
        for listing in user_listings:
            print(f"   - {listing['title']} (${listing['price']})")
    
    print("\n" + "=" * 50)
    print("✓ Database test complete!")
    print("=" * 50)