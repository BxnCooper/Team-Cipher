# Flask Backend

This is the backend API for your capstone project.

## Setup

**IMPORTANT: Use a virtual environment to avoid dependency conflicts!**

### Step 1: Create Virtual Environment

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

You should see `(venv)` in your terminal prompt when activated.

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the Server

```bash
python app.py
```

The backend will be available at `http://localhost:5000`

### Deactivating Virtual Environment

When you're done working:
```bash
deactivate
```

## Default Test User

- Username: `admin`
- Password: `admin123`

## Database

SQLite database file: `database.db`

The database is automatically created when you first run `app.py`.

## Adding New Features

1. Add new database tables in the `init_db()` function
2. Create new API endpoints using `@app.route()`
3. Use `get_db()` to access the database
4. Return JSON responses using `jsonify()`

## Example Endpoint

```python
@app.route('/api/example', methods=['GET'])
def example():
    return jsonify({'message': 'Hello!'})
```

## Important Notes

- Always activate the virtual environment before working: `source venv/bin/activate`
- Install new packages inside venv: `pip install package-name`
- Update requirements.txt after adding packages: `pip freeze > requirements.txt`
- Don't commit the venv folder to git (add to .gitignore)
