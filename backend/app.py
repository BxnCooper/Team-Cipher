"""
Flask Backend - Team Cipher Marketplace
Connected to SQLite Database

This backend provides API endpoints for the Team Cipher marketplace,
handling users, listings, messages, and reviews.
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

# Add parent directory to path so we can import database module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import (
    initialize_db,
    add_user,
    get_users,
    get_user_by_id,
    get_user_by_username,
    update_user,
    delete_user,
    add_listing,
    get_listings,
    get_listing_by_id,
    get_user_listings,
    update_listing,
    delete_listing,
)

app = Flask(__name__)
CORS(app)  # Enable CORS for Next.js frontend

# Initialize database on startup
try:
    initialize_db()
    print("✓ Database connected successfully!")
except Exception as e:
    print(f"✗ Database initialization error: {e}")

# ============================================================================
# BASIC EXAMPLE ENDPOINTS
# ============================================================================

@app.route('/')
def home():
    """Beautiful backend home page"""
    html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask Backend - CSC 489</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 20px;
            }
            
            .container {
                background: white;
                border-radius: 20px;
                box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
                max-width: 800px;
                width: 100%;
                padding: 40px;
            }
            
            .header {
                text-align: center;
                margin-bottom: 40px;
            }
            
            .status-badge {
                display: inline-block;
                background: #10b981;
                color: white;
                padding: 8px 16px;
                border-radius: 20px;
                font-size: 14px;
                font-weight: 600;
                margin-bottom: 20px;
                animation: pulse 2s infinite;
            }
            
            @keyframes pulse {
                0%, 100% { opacity: 1; }
                50% { opacity: 0.7; }
            }
            
            h1 {
                font-size: 2.5rem;
                color: #1a202c;
                margin-bottom: 10px;
            }
            
            .subtitle {
                color: #64748b;
                font-size: 1.1rem;
            }
            
            .info-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 20px;
                margin: 30px 0;
            }
            
            .info-card {
                background: #f8fafc;
                padding: 20px;
                border-radius: 12px;
                border: 2px solid #e2e8f0;
            }
            
            .info-label {
                color: #64748b;
                font-size: 12px;
                text-transform: uppercase;
                letter-spacing: 0.5px;
                margin-bottom: 8px;
                font-weight: 600;
            }
            
            .info-value {
                color: #1a202c;
                font-size: 1.1rem;
                font-weight: 600;
                font-family: monospace;
            }
            
            .endpoints {
                margin-top: 40px;
            }
            
            .section-title {
                font-size: 1.5rem;
                color: #1a202c;
                margin-bottom: 20px;
                display: flex;
                align-items: center;
                gap: 10px;
            }
            
            .endpoint {
                background: #f8fafc;
                padding: 16px;
                border-radius: 12px;
                margin-bottom: 12px;
                border-left: 4px solid #667eea;
                transition: all 0.3s ease;
            }
            
            .endpoint:hover {
                background: #f1f5f9;
                transform: translateX(5px);
            }
            
            .endpoint-method {
                display: inline-block;
                background: #667eea;
                color: white;
                padding: 4px 12px;
                border-radius: 6px;
                font-size: 12px;
                font-weight: 700;
                margin-right: 10px;
            }
            
            .endpoint-method.post {
                background: #10b981;
            }
            
            .endpoint-path {
                font-family: monospace;
                color: #1a202c;
                font-weight: 600;
            }
            
            .endpoint-desc {
                color: #64748b;
                font-size: 14px;
                margin-top: 8px;
            }
            
            .test-button {
                background: #667eea;
                color: white;
                border: none;
                padding: 12px 24px;
                border-radius: 8px;
                font-weight: 600;
                cursor: pointer;
                font-size: 14px;
                transition: all 0.3s ease;
                margin-top: 10px;
            }
            
            .test-button:hover {
                background: #5568d3;
                transform: translateY(-2px);
                box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
            }
            
            .footer {
                margin-top: 40px;
                padding-top: 30px;
                border-top: 2px solid #e2e8f0;
                text-align: center;
            }
            
            .footer-text {
                color: #64748b;
                font-size: 14px;
            }
            
            .footer-links {
                margin-top: 15px;
                display: flex;
                gap: 20px;
                justify-content: center;
                flex-wrap: wrap;
            }
            
            .footer-link {
                color: #667eea;
                text-decoration: none;
                font-weight: 600;
                transition: color 0.3s ease;
            }
            
            .footer-link:hover {
                color: #5568d3;
            }
            
            .emoji {
                font-size: 1.5rem;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div class="status-badge">✓ ONLINE</div>
                <h1>🚀 Flask Backend</h1>
                <p class="subtitle">CSC 489 - Web Application Security</p>
            </div>
            
            <div class="info-grid">
                <div class="info-card">
                    <div class="info-label">Framework</div>
                    <div class="info-value">Flask 3.0</div>
                </div>
                <div class="info-card">
                    <div class="info-label">Database</div>
                    <div class="info-value">SQLite 3</div>
                </div>
                <div class="info-card">
                    <div class="info-label">Server</div>
                    <div class="info-value">localhost:5000</div>
                </div>
                <div class="info-card">
                    <div class="info-label">Status</div>
                    <div class="info-value" style="color: #10b981;">Running</div>
                </div>
            </div>
            
            <div class="endpoints">
                <h2 class="section-title">
                    <span class="emoji">📡</span>
                    Available Endpoints
                </h2>
                
                <div class="endpoint">
                    <div>
                        <span class="endpoint-method">GET</span>
                        <span class="endpoint-path">/api/test</span>
                    </div>
                    <div class="endpoint-desc">Test endpoint to verify API connectivity</div>
                    <a href="/api/test" target="_blank">
                        <button class="test-button">Test Endpoint →</button>
                    </a>
                </div>
                
                <div class="endpoint">
                    <div>
                        <span class="endpoint-method post">POST</span>
                        <span class="endpoint-path">/api/login</span>
                    </div>
                    <div class="endpoint-desc">User authentication (placeholder - implement your logic)</div>
                </div>
                
                <div class="endpoint">
                    <div>
                        <span class="endpoint-method">GET</span>
                        <span class="endpoint-path">/api/...</span>
                    </div>
                    <div class="endpoint-desc">Add your custom endpoints here!</div>
                </div>
            </div>
            
            <div class="footer">
                <p class="footer-text">
                    <strong>Default Credentials:</strong> admin / admin123
                </p>
                <p class="footer-text" style="margin-top: 10px;">
                    Add your features in <code>backend/app.py</code>
                </p>
                <div class="footer-links">
                    <a href="https://flask.palletsprojects.com/" target="_blank" class="footer-link">
                        Flask Docs
                    </a>
                    <a href="https://www.sqlite.org/docs.html" target="_blank" class="footer-link">
                        SQLite Docs
                    </a>
                    <a href="http://localhost:3000" target="_blank" class="footer-link">
                        Open Frontend →
                    </a>
                </div>
            </div>
        </div>
    </body>
    </html>
    '''
    return html

@app.route('/api/test')
def test():
    """Test endpoint to verify API and database are working"""
    try:
        users = get_users()
        return jsonify({
            'message': '✓ API and Database working!',
            'status': 'online',
            'backend': 'Flask',
            'database': 'SQLite',
            'users_count': len(users)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ============================================================================
# USER ENDPOINTS
# ============================================================================

@app.route('/api/users', methods=['GET'])
def get_all_users():
    """Get all users from database"""
    try:
        users = get_users()
        return jsonify(users)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get a specific user by ID"""
    try:
        user = get_user_by_id(user_id)
        if user:
            return jsonify(user)
        return jsonify({'error': 'User not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/users/username/<username>', methods=['GET'])
def get_user_route(username):
    """Get a user by username (useful for login)"""
    try:
        user = get_user_by_username(username)
        if user:
            return jsonify(user)
        return jsonify({'error': 'User not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/users', methods=['POST'])
def create_user():
    """Create a new user"""
    try:
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        
        if not username or not email or not password:
            return jsonify({'error': 'Missing required fields'}), 400
        
        user_id = add_user(username, email, password)
        if user_id:
            return jsonify({
                'id': user_id,
                'username': username,
                'email': email,
                'message': 'User created successfully'
            }), 201
        return jsonify({'error': 'Failed to create user'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user_route(user_id):
    """Update user information"""
    try:
        data = request.get_json()
        success = update_user(
            user_id,
            username=data.get('username'),
            email=data.get('email'),
            password=data.get('password')
        )
        if success:
            user = get_user_by_id(user_id)
            return jsonify(user)
        return jsonify({'error': 'User not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user_route(user_id):
    """Delete a user"""
    try:
        success = delete_user(user_id)
        if success:
            return jsonify({'message': 'User deleted successfully'})
        return jsonify({'error': 'User not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ============================================================================
# LISTINGS ENDPOINTS
# ============================================================================

@app.route('/api/listings', methods=['GET'])
def get_all_listings():
    """Get all listings"""
    try:
        listings = get_listings()
        return jsonify(listings)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/listings/<int:listing_id>', methods=['GET'])
def get_listing(listing_id):
    """Get a specific listing by ID"""
    try:
        listing = get_listing_by_id(listing_id)
        if listing:
            return jsonify(listing)
        return jsonify({'error': 'Listing not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/users/<int:user_id>/listings', methods=['GET'])
def get_user_listings_route(user_id):
    """Get all listings from a specific user"""
    try:
        listings = get_user_listings(user_id)
        return jsonify(listings)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/listings', methods=['POST'])
def create_listing():
    """Create a new listing"""
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        title = data.get('title')
        description = data.get('description')
        price = data.get('price')
        category = data.get('category')
        
        if not all([user_id, title, price, category]):
            return jsonify({'error': 'Missing required fields'}), 400
        
        listing_id = add_listing(user_id, title, description, price, category)
        if listing_id:
            return jsonify({
                'id': listing_id,
                'user_id': user_id,
                'title': title,
                'price': price,
                'category': category,
                'message': 'Listing created successfully'
            }), 201
        return jsonify({'error': 'Failed to create listing'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/listings/<int:listing_id>', methods=['PUT'])
def update_listing_route(listing_id):
    """Update a listing"""
    try:
        data = request.get_json()
        success = update_listing(
            listing_id,
            title=data.get('title'),
            description=data.get('description'),
            price=data.get('price'),
            category=data.get('category')
        )
        if success:
            listing = get_listing_by_id(listing_id)
            return jsonify(listing)
        return jsonify({'error': 'Listing not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/listings/<int:listing_id>', methods=['DELETE'])
def delete_listing_route(listing_id):
    """Delete a listing"""
    try:
        success = delete_listing(listing_id)
        if success:
            return jsonify({'message': 'Listing deleted successfully'})
        return jsonify({'error': 'Listing not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ============================================================================
# LEGACY ENDPOINTS (deprecated, use endpoints above instead)
# ============================================================================

@app.route('/api/login', methods=['POST'])
def login():
    """
    Legacy login endpoint (deprecated)
    Use /api/users/username/<username> instead
    """
    try:
        data = request.get_json()
        username = data.get('username', '')
        password = data.get('password', '')
        
        user = get_user_by_username(username)
        if user and user['password'] == password:
            return jsonify({
                'message': 'Login successful',
                'user': dict(user)
            })
        return jsonify({'error': 'Invalid credentials'}), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ============================================================================
# RUN SERVER
# ============================================================================

if __name__ == '__main__':
    print("=" * 60)
    print("Flask Backend Starting...")
    print("Backend running on: http://localhost:5000")
    print("API endpoints available at: http://localhost:5000/api/...")
    print("=" * 60)
    app.run(debug=True, port=5000)
