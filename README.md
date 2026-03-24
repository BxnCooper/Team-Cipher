# Capstone Project Starter Template
CSC 489 - Web Application Security | Spring 2026

This is a minimal boilerplate template to get you started with your capstone project. It includes a Next.js frontend, Flask backend, and SQLite database.

## Quick Start

### Prerequisites

Make sure you have these installed:
- **Node.js** v18+ ([download](https://nodejs.org/))
- **Python** 3.8+ ([download](https://www.python.org/downloads/))

Check versions:
```bash
node --version
python --version  # or python3 --version
```

### Installation

**1. Setup Backend (Flask) with Virtual Environment**

```bash
cd backend

# Create virtual environment
python3 -m venv venv  # macOS/Linux
# OR
python -m venv venv   # Windows

# Activate virtual environment
source venv/bin/activate      # macOS/Linux
# OR
venv\Scripts\activate         # Windows

# You should see (venv) in your terminal

# Install dependencies
pip install -r requirements.txt

# Run backend
python app.py
```

Backend will run on: `http://localhost:5000`

**IMPORTANT:** Keep this terminal open and running!

---

**2. Setup Frontend (Next.js)** 

Open a **NEW** terminal window:

```bash
cd frontend

# Install dependencies
npm install

# Run frontend
npm run dev
```

Frontend will run on: `http://localhost:3000`

---

**3. Open in Browser**

Go to: [http://localhost:3000](http://localhost:3000)

You should see the starter page with a green "Connected" message.

## Project Structure

```
capstone-starter-template/
├── backend/                # Flask API
│   ├── app.py             # Main Flask application
│   ├── requirements.txt   # Python dependencies
│   ├── venv/              # Virtual environment (created by you)
│   ├── database.db        # SQLite database (auto-created)
│   └── README.md          # Backend documentation
│
├── frontend/              # Next.js UI
│   ├── app/               # Pages and components
│   │   ├── layout.jsx    # Main layout
│   │   └── page.jsx      # Home page
│   ├── package.json       # Node dependencies
│   ├── node_modules/      # Node packages (created by npm install)
│   └── README.md          # Frontend documentation
│
└── README.md              # This file
```

## Default Test User

The database comes with one test user:
- **Username:** `admin`
- **Password:** `admin123`

## Daily Workflow

### Starting Your Work Session

**Terminal 1 (Backend):**
```bash
cd backend
source venv/bin/activate  # Activate venv first!
python app.py
```

**Terminal 2 (Frontend):**
```bash
cd frontend
npm run dev
```

### Stopping Your Work Session

**Terminal 1:** Press `Ctrl+C` to stop Flask, then `deactivate` to exit venv

**Terminal 2:** Press `Ctrl+C` to stop Next.js

## What to Build

This template provides the basic structure. You need to:

1. **Design your application** - What will it do? Who uses it?
2. **Add features** - Login, profiles, posts, search, etc.
3. **Implement vulnerabilities** - SQL injection, XSS, CSRF, IDOR, etc.
4. **Document everything** - README, code comments, vulnerability notes

## Adding Features

### Backend (Flask)

Add new API endpoints in `backend/app.py`:

```python
@app.route('/api/your-endpoint', methods=['POST'])
def your_function():
    data = request.get_json()
    # Your logic here
    return jsonify({'message': 'Success!'})
```

### Frontend (Next.js)

Create new pages in `frontend/app/`:

```
frontend/app/
└── your-page/
    └── page.jsx
```

This creates the route: `http://localhost:3000/your-page`

## Resources

- **AI Prompt Library** (Canvas Files) - 50+ prompts to generate features
- **Vulnerability Guide** (Canvas Files) - Code examples for each vulnerability type
- **Quick Reference** (Canvas Files) - Troubleshooting and commands
- **Next.js Docs:** https://nextjs.org/docs
- **Flask Docs:** https://flask.palletsprojects.com/

## Troubleshooting

**"externally-managed-environment" error (macOS/Linux):**
```bash
# You forgot to activate venv!
cd backend
source venv/bin/activate
pip install -r requirements.txt
```

**Backend won't start:**
```bash
# Make sure you're in the backend folder with venv activated
cd backend
source venv/bin/activate  # macOS/Linux
pip install --upgrade pip
pip install -r requirements.txt
python app.py
```

**Frontend won't start:**
```bash
# Make sure you're in the frontend folder
cd frontend
rm -rf node_modules package-lock.json
npm install
npm run dev
```

**"Backend not running" message:**
- Make sure Flask is running on port 5000
- Check for error messages in the Flask terminal
- Try restarting both servers

**Database errors:**
- Delete `backend/database.db` and restart Flask
- Database will auto-recreate with test user

**Port already in use:**
```bash
# Find and kill process on port 5000
lsof -i :5000
kill -9 [PID]

# Or use different port in app.py
app.run(debug=True, port=5001)
```

## Git/Version Control

### .gitignore File

Create `.gitignore` in your project root:

```
# Python
__pycache__/
*.pyc
*.pyo
*.db
venv/
env/

# Node
node_modules/
.next/
out/

# OS
.DS_Store
.env
```

**IMPORTANT:** Add `venv/` to `.gitignore` - never commit your virtual environment!

## Need Help?

- **In-class:** Tuesday & Thursday work sessions
- **Office Hours:** Tu-Th 3:00-3:55 PM, TEC 380
- **Email:** oluseyi.olukola@usm.edu

---

**You're ready to start building! 🚀**

Customize this template, add your features, and implement your vulnerabilities.

Good luck!
