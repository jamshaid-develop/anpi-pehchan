# 📋 SKILLS.md — CV & Portfolio Sections Reference Guide
# APNI PEHCHAN — Personal Identity Builder System

This file documents every section available in the CV and Portfolio,
what data each section needs, and how to fill them correctly.

---

## 📄 CV SECTIONS

### 1. Header (Always Shown)
| Field    | Required | Example                        |
|----------|----------|-------------------------------|
| Name     | ✅ Yes   | Jamshaid Nawaz                |
| Title    | ✅ Yes   | ML Engineer & Python Developer |
| Email    | ✅ Yes   | jamshaid@email.com            |
| City     | Optional | Lahore, Pakistan              |

---

### 2. Professional Summary
| Field   | Required | Notes                              |
|---------|----------|------------------------------------|
| Summary | Optional | 3–4 lines about yourself and goals |

> If empty → section is hidden in CV

---

### 3. Contact Section
| Field     | Required | Example              |
|-----------|----------|---------------------|
| Email     | ✅ Yes   | jamshaid@email.com  |
| Phone     | ✅ Yes   | +92 300 1234567     |
| WhatsApp  | ✅ Yes   | +92 300 1234567     |
| GitHub    | Optional | github.com/username |
| LinkedIn  | Optional | linkedin.com/in/... |
| Facebook  | Optional | facebook.com/...    |
| Instagram | Optional | instagram.com/...   |
| Telegram  | Optional | t.me/username       |
| Twitter   | Optional | x.com/username      |
| Portfolio | Optional | yoursite.com        |

> Only filled fields appear in CV and Portfolio

---

### 4. Education Section
| Field         | Required | Example              |
|---------------|----------|---------------------|
| Institute     | Optional | University of Punjab |
| Degree        | Optional | BS Computer Science  |
| Batch Year    | Optional | 2020 – 2024         |
| City          | Optional | Lahore               |

> At least one entry needed for section to appear
> Add multiple entries using "+ Add Education" button

---

### 5. Skills Section
| Field  | Required | Notes                      |
|--------|----------|---------------------------|
| Name   | Optional | Python, Flask, ML, SQL     |
| Level  | Optional | Slider 10% – 100%          |

> Comma-separated skills OR add one-by-one
> Shown as animated bars in portfolio
> If empty → section hidden

---

### 6. Projects Section
| Field       | Required | Example                          |
|-------------|----------|----------------------------------|
| Name        | ✅ Yes   | AI Python Assistant              |
| Description | Optional | What the project does            |
| Tech Stack  | Optional | Python, Flask, Streamlit         |
| Live Link   | Optional | https://myapp.streamlit.app      |
| GitHub Link | Optional | https://github.com/user/repo     |
| Image       | Optional | Upload project screenshot        |
| Challenges  | Optional | Problem this project solved      |

> If no projects → section hidden in CV and Portfolio

---

### 7. Certifications Section
| Field  | Required | Notes                              |
|--------|----------|------------------------------------|
| Name   | ✅ Yes   | Python for Data Science – Coursera |
| Link   | Optional | Verification URL                   |
| File   | Optional | Upload PDF certificate             |

> If empty → section hidden

---

### 8. Experience Section
| Field       | Required | Example                        |
|-------------|----------|-------------------------------|
| Role        | Optional | Python Developer – Freelance  |
| Description | Optional | What you did in this role     |
| Year        | Optional | 2023 – Present                |

> Shown as animated timeline in portfolio
> If empty → section hidden

---

### 9. Languages Section
| Field | Required | Options                                       |
|-------|----------|-----------------------------------------------|
| Name  | Optional | Urdu, English, Arabic                        |
| Level | Optional | Native / Fluent / Advanced / Intermediate / Basic |

> If empty → section hidden

---

## 🌐 PORTFOLIO-ONLY SECTIONS

### 10. Services Section
Select from these checkboxes in Profile → Services:

| Service           | Icon | Show When              |
|-------------------|------|------------------------|
| Python Automation | 🐍   | Checked in profile     |
| Machine Learning  | 🤖   | Checked in profile     |
| Web Development   | 🌐   | Checked in profile     |
| Database Design   | 🗄️   | Checked in profile     |
| API Development   | ⚡   | Checked in profile     |
| Data Analysis     | 📊   | Checked in profile     |
| UI/UX Design      | 🎨   | Checked in profile     |
| DevOps            | ⚙️   | Checked in profile     |

> If no services selected → Services section hidden from portfolio

---

### 11. Hero Section (Portfolio Only)
| Element        | Source             | Notes                        |
|----------------|--------------------|------------------------------|
| Name           | user.name          | Auto from registration       |
| Title          | profile.title      | Edit in Profile page         |
| Short Intro    | profile.summary    | First 200 chars shown        |
| Photo          | profile.avatar     | Upload in Profile page       |
| Hire Me Btn    | → scrolls #contact | Always shown                 |
| View Projects  | → scrolls #projects| Always shown                 |
| Download CV    | /cv/download       | Always shown                 |

---

### 12. About Section (Portfolio Only)
| Element    | Source          | Notes                          |
|------------|-----------------|-------------------------------|
| Bio text   | profile.summary | Full summary shown             |
| City       | profile.city    | Shown below bio                |
| Stats grid | Auto-counted    | Projects/Skills/Certs/Exp count|

---

## 🔒 VISIBILITY RULES SUMMARY

| Section        | CV  | Portfolio | Hidden When              |
|----------------|-----|-----------|--------------------------|
| Header         | ✅  | ✅        | Never hidden             |
| Summary        | ✅  | ✅        | summary field is blank   |
| Skills         | ✅  | ✅        | No skills added          |
| Experience     | ✅  | ✅        | No entries added         |
| Education      | ✅  | ✅        | No entries added         |
| Projects       | ✅  | ✅        | No projects added        |
| Certificates   | ✅  | ✅        | No certs added           |
| Languages      | ✅  | ✅        | No languages added       |
| Services       | ❌  | ✅        | No services selected     |
| Contact links  | ✅  | ✅        | Each field hides if blank|

---

## 💡 TIPS FOR BEST RESULTS

1. **Fill all required fields first** — Name, Title, Email, Phone
2. **Add at least 3 skills** — portfolio looks best with 6–8 skills
3. **Add at least 1 project** — with description and GitHub link
4. **Upload a profile photo** — makes portfolio much more professional
5. **Write a good summary** — 3–4 lines, mention your stack and goals
6. **Add batch years for education** — e.g. "2020 – 2024"
7. **Add tech stack for projects** — e.g. "Python, Flask, SQLite"
8. **Select services** — even 2–3 services improve portfolio quality
9. **Add languages** — even just "Urdu (Native), English (Fluent)"
10. **Preview CV before downloading** — check /cv/preview first

---

*APNI PEHCHAN — Build Your Identity. Own Your Story.*
*Developed by Jamshaid Nawaz*