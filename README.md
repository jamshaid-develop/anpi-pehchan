# 🪪 APNI PEHCHAN — Personal Identity Builder System

> A full-stack SaaS web platform to build your professional CV and portfolio website — all from one place.

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Flask](https://img.shields.io/badge/Flask-3.0-green)
![SQLite](https://img.shields.io/badge/Database-SQLite-orange)
![ReportLab](https://img.shields.io/badge/PDF-ReportLab-red)
![License](https://img.shields.io/badge/License-MIT-purple)

---

## 📌 What is APNI PEHCHAN?

**APNI PEHCHAN** (meaning *"Your Identity"* in Urdu) is a personal identity builder system that allows users to:

- ✅ Register and login securely
- ✅ Fill their professional profile step-by-step
- ✅ Generate a **professional PDF CV** (downloadable)
- ✅ Generate a **live animated portfolio website**
- ✅ Share portfolio via public URL
- ✅ Edit and update everything anytime

---

## ✨ Features

### 📄 CV Generator
- Professional A4 PDF output via ReportLab
- Only filled sections appear — empty sections auto-hidden
- Sections: Summary, Skills, Experience, Education, Projects, Certificates, Languages
- Instant download — no file saved to disk

### 🌐 Portfolio Website
- Live animated website with glassmorphism design
- Dark mode + Light mode toggle
- Smooth scroll reveal animations
- Animated skill progress bars
- Experience timeline
- Shareable public URL: `/portfolio/public/<user_id>`
- Fully mobile responsive

### 🔐 Authentication
- Secure register and login
- Passwords hashed with Werkzeug (PBKDF2-SHA256)
- Session-based authentication
- Protected routes with `@login_required`

### 📊 Dashboard
- Profile completion tracker
- Quick edit cards for all sections
- One-click access to CV and Portfolio

---

## 🏗️ Project Structure

```
apni_pehchan/
│
├── app.py                          ← Main Flask app (models, routes, PDF engine)
├── requirements.txt                ← Dependencies
├── README.md                       ← This file
├── .gitignore                      ← Git exclusions
│
├── static/
│   ├── css/
│   │   └── style.css               ← Complete dark theme CSS
│   ├── js/
│   │   └── main.js                 ← Theme toggle, animations, mobile menu
│   └── uploads/
│       ├── avatars/                ← Profile photo uploads
│       ├── projects/               ← Project image uploads
│       └── certificates/           ← Certificate file uploads
│
└── templates/
    ├── base.html                   ← Navbar, footer, theme toggle
    ├── landing.html                ← Public landing page
    ├── auth/
    │   ├── login.html              ← Login form
    │   └── register.html           ← Registration form
    ├── dashboard/
    │   ├── dashboard.html          ← Main dashboard
    │   ├── profile.html            ← Profile editor
    │   ├── skills.html             ← Skills editor
    │   ├── education.html          ← Education editor
    │   ├── experience.html         ← Experience editor
    │   ├── projects.html           ← Projects editor
    │   ├── certificates.html       ← Certificates editor
    │   └── languages.html          ← Languages editor
    ├── cv/
    │   └── preview.html            ← CV preview page
    └── portfolio/
        └── portfolio.html          ← Full live portfolio website
```

---

## 🧰 Tech Stack

| Layer        | Technology          | Purpose                          |
|--------------|---------------------|----------------------------------|
| Backend      | Python + Flask      | Web framework and routing        |
| Database     | SQLite + SQLAlchemy | Data storage and ORM             |
| PDF          | ReportLab           | Professional CV generation       |
| Auth         | Werkzeug            | Password hashing and security    |
| Templates    | Jinja2              | Dynamic HTML rendering           |
| Frontend     | HTML5 + CSS3 + JS   | UI, animations, responsiveness   |
| Fonts        | Syne + DM Sans      | Premium typography                |
| Deployment   | Gunicorn + Render   | Production WSGI server           |

---

## ⚙️ Setup Instructions (PyCharm)

### Step 1 — Clone the project

```bash
git clone https://github.com/YOUR_USERNAME/apni-pahchan.git
cd apni-pahchan
```

### Step 2 — Create virtual environment

```bash
# In PyCharm terminal
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Activate (Mac/Linux)
source .venv/bin/activate
```

### Step 3 — Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Run the application

```bash
python app.py
```

### Step 5 — Open in browser

```
http://localhost:5000
```

> The SQLite database `apni_pehchan.db` is created automatically on first run.
> Upload folders are also created automatically.

---

## 🗄️ Database Models

| Model       | Key Fields                                      |
|-------------|------------------------------------------------|
| User        | id, name, email, password (hashed)             |
| Profile     | title, summary, city, phone, github, linkedin  |
| Project     | name, description, tech_stack, live_link       |
| Education   | institute, degree, batch, city                 |
| Experience  | role, description, year                        |
| Certificate | name, link, file                               |
| Skill       | name, level (0–100)                            |
| Language    | name, level (Native/Fluent/etc)                |

---

## 🌐 All Routes

| Route                      | Method   | Auth | Description                    |
|----------------------------|----------|------|--------------------------------|
| `/`                        | GET      | No   | Landing page                   |
| `/register`                | GET/POST | No   | User registration              |
| `/login`                   | GET/POST | No   | User login                     |
| `/logout`                  | GET      | Yes  | Clear session                  |
| `/dashboard`               | GET      | Yes  | Main dashboard                 |
| `/profile`                 | GET/POST | Yes  | Edit profile and contacts      |
| `/skills`                  | GET/POST | Yes  | Edit skills                    |
| `/education`               | GET/POST | Yes  | Edit education                 |
| `/experience`              | GET/POST | Yes  | Edit experience                |
| `/projects`                | GET/POST | Yes  | Edit projects                  |
| `/certificates`            | GET/POST | Yes  | Edit certificates              |
| `/languages`               | GET/POST | Yes  | Edit languages                 |
| `/cv/preview`              | GET      | Yes  | Preview CV                     |
| `/cv/download`             | GET      | Yes  | Download PDF CV                |
| `/portfolio`               | GET      | Yes  | View your portfolio            |
| `/portfolio/public/<id>`   | GET      | No   | Public shareable portfolio URL |

---

## 🚀 Deploy on Render (Free)

### Step 1 — Push to GitHub first (see below)

### Step 2 — Go to [render.com](https://render.com)

1. Click **New +** → **Web Service**
2. Connect your GitHub repo
3. Set **Build Command:**
   ```
   pip install -r requirements.txt
   ```
4. Set **Start Command:**
   ```
   gunicorn app:app
   ```
5. Add **Environment Variable:**
   ```
   SECRET_KEY = your-strong-random-secret-key
   ```
6. Click **Create Web Service**

Your app goes live at:
```
https://apni-pahchan.onrender.com
```

---

## 📤 Push to GitHub

```bash
# Initialize git (if not done already)
git init

# Stage all files
git add .

# First commit
git commit -m "Initial commit: APNI PEHCHAN v1.0"

# Add GitHub remote (create repo on github.com first)
git remote add origin https://github.com/YOUR_USERNAME/apni-pahchan.git

# Push
git branch -M main
git push -u origin main
```

> ✅ The `.gitignore` already excludes:
> - `apni_pehchan.db` — database file
> - `static/uploads/` — user uploaded files
> - `.venv/` — virtual environment
> - `__pycache__/` — Python cache

---

## 🔐 Security Notes

- Passwords are **never stored in plain text** — hashed with PBKDF2-SHA256
- API keys and secrets stored in **environment variables** — never in code
- File uploads validated with **extension whitelist** and `secure_filename()`
- All dashboard routes protected with `@login_required` decorator
- SQLAlchemy ORM prevents SQL injection with parameterized queries

---

## 🔮 Future Enhancements

- [ ] Multiple CV templates (minimal, modern, creative)
- [ ] CSRF protection with Flask-WTF
- [ ] Email verification on registration
- [ ] Contact form with email delivery
- [ ] PostgreSQL for production database
- [ ] AI-powered summary generator (Groq API)
- [ ] LinkedIn profile import
- [ ] Custom domain support

---

## 👨‍💻 Developer

**Jamshaid Nawaz**
ML Engineer & Full Stack AI Developer

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

*Build Your Identity. Own Your Story. — APNI PEHCHAN*