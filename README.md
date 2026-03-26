# EagleMart - Student Marketplace
**CSC 489 - Web Application Security | Spring 2026**
**Team Cipher**

EagleMart is a campus marketplace where students can buy and sell items like textbooks, electronics, furniture, and more. The platform features user authentication, listing management, search, and messaging — built with intentional security vulnerabilities for educational penetration testing.

## Setup

### Prerequisites

- **Node.js** v18+
- **Python** 3.8+

### 1. Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate      # macOS/Linux
# OR venv\Scripts\activate    # Windows

pip install -r requirements.txt
python app.py
```

Runs on `http://localhost:5000`

### 2. Frontend

```bash
cd frontend
npm install
npm run dev
```

Runs on `http://localhost:3000`

### Default Credentials

| Username | Password  | Role  |
|----------|-----------|-------|
| admin    | admin123  | admin |

## Tech Stack

| Layer    | Technology                        |
|----------|-----------------------------------|
| Frontend | Next.js 14, React 18, Lucide Icons |
| Backend  | Flask 3.0, Python                 |
| Database | SQLite 3                          |

## Frontend Architecture

```
frontend/
├── public/
│   └── logo.svg                        # EagleMart logo
│
├── app/
│   ├── globals.css                     # Global styles (black/white/gold theme)
│   ├── layout.jsx                      # Root layout — wraps all pages
│   ├── page.jsx                        # / — Landing page (hero, categories, recent listings)
│   │
│   ├── components/
│   │   └── Navbar.jsx                  # Sticky nav — logo, links, auth state
│   │
│   ├── login/
│   │   └── page.jsx                    # /login — Sign-in form
│   │
│   ├── register/
│   │   └── page.jsx                    # /register — Registration form
│   │
│   ├── listings/
│   │   ├── page.jsx                    # /listings — Browse all, filter by category
│   │   └── [id]/
│   │       └── page.jsx                # /listings/:id — Detail view, contact seller
│   │
│   ├── create-listing/
│   │   └── page.jsx                    # /create-listing — Post a new item
│   │
│   ├── profile/
│   │   └── [id]/
│   │       └── page.jsx                # /profile/:id — User profile + their listings
│   │
│   └── search/
│       └── page.jsx                    # /search — Search with quick filters
│
├── package.json
└── next.config.js
```

### Page Flow

```
Landing (/)
  ├── Browse Listings (/listings)
  │     └── Listing Detail (/listings/:id)
  │           └── Contact Seller (form)
  ├── Search (/search)
  │     └── Listing Detail (/listings/:id)
  ├── Create Listing (/create-listing)  [auth required]
  ├── Profile (/profile/:id)
  ├── Login (/login)
  └── Register (/register)
```

### Data Flow

```
┌─────────────┐       fetch()        ┌──────────────┐      raw SQL      ┌──────────┐
│   Next.js   │ ──────────────────►  │  Flask API   │ ────────────────► │  SQLite  │
│  (port 3000)│ ◄──────────────────  │ (port 5000)  │ ◄──────────────── │   (.db)  │
└─────────────┘       JSON           └──────────────┘     results       └──────────┘
       │
       ├── localStorage (auth token, user object)
       ├── No CSRF tokens
       └── dangerouslySetInnerHTML (XSS surface)
```

## Troubleshooting

**Frontend won't start:**
```bash
cd frontend && rm -rf node_modules package-lock.json && npm install && npm run dev
```

**Backend won't start:**
```bash
cd backend && source venv/bin/activate && pip install -r requirements.txt && python app.py
```

**Database errors:** Delete `backend/database.db` and restart Flask — it auto-recreates.

**Port in use:**
```bash
lsof -i :5000   # find PID
kill -9 [PID]
```
