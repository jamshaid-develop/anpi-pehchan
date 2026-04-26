# ============================================================
# app.py — APNI PEHCHAN | Complete Single-File Flask App
# ============================================================
from flask import (Flask, render_template, request, redirect,
                   url_for, session, send_file)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from functools import wraps
import os, json, io, base64
from datetime import datetime

# ── STEP 1: APP CONFIG ──
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "apni-pehchan-secret-2024")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///apni_pehchan.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024
UPLOAD_FOLDER = os.environ.get("UPLOAD_PATH", os.path.join("static", "uploads"))
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
db = SQLAlchemy(app)

@app.template_filter("from_json")
def from_json_filter(value):
    try: return json.loads(value) if value else []
    except: return []

# ── STEP 2: MODELS ──
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    profile = db.relationship("Profile", backref="user", uselist=False, cascade="all, delete-orphan")
    projects = db.relationship("Project", backref="user", cascade="all, delete-orphan")
    educations = db.relationship("Education", backref="user", cascade="all, delete-orphan")
    experiences = db.relationship("Experience", backref="user", cascade="all, delete-orphan")
    certificates = db.relationship("Certificate", backref="user", cascade="all, delete-orphan")
    skills = db.relationship("Skill", backref="user", cascade="all, delete-orphan")
    languages = db.relationship("Language", backref="user", cascade="all, delete-orphan")
    def set_password(self, pw): self.password = generate_password_hash(pw)
    def check_password(self, pw): return check_password_hash(self.password, pw)

class Profile(db.Model):
    __tablename__ = "profiles"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    title = db.Column(db.String(150)); summary = db.Column(db.Text)
    city = db.Column(db.String(100)); phone = db.Column(db.String(30))
    whatsapp = db.Column(db.String(30)); email = db.Column(db.String(150))
    github = db.Column(db.String(200)); linkedin = db.Column(db.String(200))
    portfolio = db.Column(db.String(200)); facebook = db.Column(db.String(200))
    instagram = db.Column(db.String(200)); telegram = db.Column(db.String(200))
    twitter = db.Column(db.String(200)); avatar = db.Column(db.Text)
    services = db.Column(db.Text)

class Project(db.Model):
    __tablename__ = "projects"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    name = db.Column(db.String(200)); description = db.Column(db.Text)
    tech_stack = db.Column(db.String(300)); live_link = db.Column(db.String(300))
    github_link = db.Column(db.String(300)); image = db.Column(db.Text)
    challenges = db.Column(db.Text); order = db.Column(db.Integer, default=0)

class Education(db.Model):
    __tablename__ = "educations"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    institute = db.Column(db.String(200)); degree = db.Column(db.String(200))
    batch = db.Column(db.String(50)); city = db.Column(db.String(100))
    order = db.Column(db.Integer, default=0)

class Experience(db.Model):
    __tablename__ = "experiences"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    role = db.Column(db.String(200)); description = db.Column(db.Text)
    year = db.Column(db.String(50)); order = db.Column(db.Integer, default=0)

class Certificate(db.Model):
    __tablename__ = "certificates"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    name = db.Column(db.String(200)); link = db.Column(db.String(300))
    file = db.Column(db.Text); order = db.Column(db.Integer, default=0)

class Skill(db.Model):
    __tablename__ = "skills"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    name = db.Column(db.String(100)); level = db.Column(db.Integer, default=80)

class Language(db.Model):
    __tablename__ = "languages"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    name = db.Column(db.String(100)); level = db.Column(db.String(50), default="Fluent")

# ── STEP 3: HELPERS ──
ALLOWED = {"png","jpg","jpeg","gif","webp","pdf"}
def allowed_file(f): return "." in f and f.rsplit(".",1)[1].lower() in ALLOWED


def save_upload(file, sub):
    print(f"save_upload called: file={file}, filename={file.filename if file else 'None'}")
    if file and file.filename and allowed_file(file.filename):
        fname = secure_filename(file.filename)
        folder = os.path.join("static", "uploads", sub)
        os.makedirs(folder, exist_ok=True)
        path = os.path.join(folder, fname)
        file.save(path)
        print(f"File saved to: {path}")
        return "/" + path.replace("\\", "/")
    print("save_upload returning None")
    return None
def login_required(f):
    @wraps(f)
    def dec(*a,**kw):
        if "user_id" not in session: return redirect(url_for("login"))
        return f(*a,**kw)
    return dec

@app.context_processor
def inject_globals(): return {"year": datetime.now().year}

# ── STEP 4: PUBLIC ROUTES ──
@app.route("/")
def index():
    if "user_id" in session: return redirect(url_for("dashboard"))
    return render_template("landing.html")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        name=request.form.get("name","").strip()
        email=request.form.get("email","").strip().lower()
        pw=request.form.get("password","")
        cf=request.form.get("confirm","")
        if not all([name,email,pw]):
            return render_template("auth/register.html",error="All fields required.")
        if pw!=cf:
            return render_template("auth/register.html",error="Passwords do not match.")
        if User.query.filter_by(email=email).first():
            return render_template("auth/register.html",error="Email already registered.")
        u=User(name=name,email=email); u.set_password(pw)
        db.session.add(u); db.session.flush()
        db.session.add(Profile(user_id=u.id,email=email))
        db.session.commit()
        session["user_id"]=u.id; session["user_name"]=u.name
        return redirect(url_for("dashboard"))
    return render_template("auth/register.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        email=request.form.get("email","").strip().lower()
        pw=request.form.get("password","")
        u=User.query.filter_by(email=email).first()
        if not u or not u.check_password(pw):
            return render_template("auth/login.html",error="Invalid email or password.")
        session["user_id"]=u.id; session["user_name"]=u.name
        return redirect(url_for("dashboard"))
    return render_template("auth/login.html")

@app.route("/logout")
def logout(): session.clear(); return redirect(url_for("index"))

# ── STEP 5: DASHBOARD ROUTES ──
@app.route("/dashboard")
@login_required
def dashboard():
    u = db.session.get(User, session["user_id"])
    if not u:
        session.clear()
        return redirect(url_for("login"))
    return render_template("dashboard/dashboard.html",user=u,profile=u.profile)

@app.route("/profile", methods=["GET","POST"])
@login_required
def profile():
    u=db.session.get(User, session["user_id"])
    p=u.profile or Profile(user_id=u.id)
    if request.method=="POST":
        p.title=request.form.get("title",""); p.summary=request.form.get("summary","")
        p.city=request.form.get("city",""); p.phone=request.form.get("phone","")
        p.whatsapp=request.form.get("whatsapp",""); p.email=request.form.get("email","")
        p.github=request.form.get("github",""); p.linkedin=request.form.get("linkedin","")
        p.portfolio=request.form.get("portfolio",""); p.facebook=request.form.get("facebook","")
        p.instagram=request.form.get("instagram",""); p.telegram=request.form.get("telegram","")
        p.twitter=request.form.get("twitter","")
        p.services=json.dumps(request.form.getlist("services"))
        s = save_upload(request.files.get("avatar"), "avatars")
        if s:
            p.avatar = s
            db.session.commit()
            print("Avatar saved:", len(s), "chars")
        if not p.id: db.session.add(p)
        db.session.commit(); return redirect(url_for("profile"))
    return render_template("dashboard/profile.html",user=u,profile=p)

@app.route("/skills", methods=["GET","POST"])
@login_required
def skills():
    u=db.session.get(User, session["user_id"])
    if request.method=="POST":
        Skill.query.filter_by(user_id=u.id).delete()
        for n,l in zip(request.form.getlist("skill_name"),request.form.getlist("skill_level")):
            if n.strip(): db.session.add(Skill(user_id=u.id,name=n.strip(),level=int(l or 80)))
        db.session.commit(); return redirect(url_for("skills"))
    return render_template("dashboard/skills.html",user=u,skills=u.skills)

@app.route("/education", methods=["GET","POST"])
@login_required
def education():
    u=db.session.get(User, session["user_id"])
    if request.method=="POST":
        Education.query.filter_by(user_id=u.id).delete()
        ins=request.form.getlist("institute"); dg=request.form.getlist("degree")
        bt=request.form.getlist("batch"); ct=request.form.getlist("city")
        for i,inst in enumerate(ins):
            if inst.strip():
                db.session.add(Education(user_id=u.id,institute=inst.strip(),
                    degree=dg[i] if i<len(dg) else "",batch=bt[i] if i<len(bt) else "",
                    city=ct[i] if i<len(ct) else "",order=i))
        db.session.commit(); return redirect(url_for("education"))
    return render_template("dashboard/education.html",user=u,educations=u.educations)

@app.route("/experience", methods=["GET","POST"])
@login_required
def experience():
    u=db.session.get(User, session["user_id"])
    if request.method=="POST":
        Experience.query.filter_by(user_id=u.id).delete()
        ro=request.form.getlist("role"); de=request.form.getlist("description")
        yr=request.form.getlist("year")
        for i,role in enumerate(ro):
            if role.strip():
                db.session.add(Experience(user_id=u.id,role=role.strip(),
                    description=de[i] if i<len(de) else "",
                    year=yr[i] if i<len(yr) else "",order=i))
        db.session.commit(); return redirect(url_for("experience"))
    return render_template("dashboard/experience.html",user=u,experiences=u.experiences)

@app.route("/projects", methods=["GET","POST"])
@login_required
def projects():
    u=db.session.get(User, session["user_id"])
    if request.method=="POST":
        Project.query.filter_by(user_id=u.id).delete()
        nm=request.form.getlist("name"); de=request.form.getlist("description")
        tc=request.form.getlist("tech_stack"); lv=request.form.getlist("live_link")
        gh=request.form.getlist("github_link"); ch=request.form.getlist("challenges")
        im=request.files.getlist("image")
        for i,name in enumerate(nm):
            if name.strip():
                img=save_upload(im[i] if i<len(im) else None,"projects")
                db.session.add(Project(user_id=u.id,name=name.strip(),
                    description=de[i] if i<len(de) else "",tech_stack=tc[i] if i<len(tc) else "",
                    live_link=lv[i] if i<len(lv) else "",github_link=gh[i] if i<len(gh) else "",
                    challenges=ch[i] if i<len(ch) else "",image=img,order=i))
        db.session.commit(); return redirect(url_for("projects"))
    return render_template("dashboard/projects.html",user=u,projects=u.projects)

@app.route("/certificates", methods=["GET","POST"])
@login_required
def certificates():
    u=db.session.get(User, session["user_id"])
    if request.method=="POST":
        Certificate.query.filter_by(user_id=u.id).delete()
        nm=request.form.getlist("name"); lk=request.form.getlist("link")
        fi=request.files.getlist("file")
        for i,name in enumerate(nm):
            if name.strip():
                fp=save_upload(fi[i] if i<len(fi) else None,"certificates")
                db.session.add(Certificate(user_id=u.id,name=name.strip(),
                    link=lk[i] if i<len(lk) else "",file=fp,order=i))
        db.session.commit(); return redirect(url_for("certificates"))
    return render_template("dashboard/certificates.html",user=u,certificates=u.certificates)

@app.route("/languages", methods=["GET","POST"])
@login_required
def languages():
    u=db.session.get(User, session["user_id"])
    if request.method=="POST":
        Language.query.filter_by(user_id=u.id).delete()
        for n,l in zip(request.form.getlist("name"),request.form.getlist("level")):
            if n.strip(): db.session.add(Language(user_id=u.id,name=n.strip(),level=l or "Fluent"))
        db.session.commit(); return redirect(url_for("languages"))
    return render_template("dashboard/languages.html",user=u,languages=u.languages)

# ── STEP 6: CV ROUTES ──
@app.route("/cv/preview")
@login_required
def cv_preview():
    u=db.session.get(User, session["user_id"])
    return render_template("cv/preview.html",user=u,profile=u.profile)

@app.route("/cv/download")
@login_required
def cv_download():
    u=db.session.get(User, session["user_id"])
    buf=build_cv_pdf(u)
    return send_file(buf,as_attachment=True,
        download_name=u.name.replace(" ","_")+"_CV.pdf",mimetype="application/pdf")

# ── STEP 7: PORTFOLIO ROUTES ──
@app.route("/portfolio")
@login_required
def portfolio():
    u=db.session.get(User, session["user_id"]); p=u.profile; svcs=[]
    if p and p.services:
        try: svcs=json.loads(p.services)
        except: pass
    return render_template("portfolio/portfolio.html",user=u,profile=p,
        projects=u.projects,skills=u.skills,educations=u.educations,
        experiences=u.experiences,certificates=u.certificates,
        languages=u.languages,services=svcs,public=False)

@app.route("/portfolio/public/<int:uid>")
def public_portfolio(uid):
    u=User.query.get_or_404(uid); p=u.profile; svcs=[]
    if p and p.services:
        try: svcs=json.loads(p.services)
        except: pass
    return render_template("portfolio/portfolio.html",user=u,profile=p,
        projects=u.projects,skills=u.skills,educations=u.educations,
        experiences=u.experiences,certificates=u.certificates,
        languages=u.languages,services=svcs,public=True)

# ── STEP 8: PDF BUILDER — ATS FRIENDLY ──
def build_cv_pdf(user):
    from reportlab.lib.pagesizes import A4
    from reportlab.lib import colors
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import cm
    from reportlab.platypus import (SimpleDocTemplate, Paragraph,
                                    Spacer, HRFlowable)
    from reportlab.lib.enums import TA_CENTER, TA_LEFT

    buf = io.BytesIO()
    p   = user.profile
    W   = A4[0] - 3.6*cm

    doc = SimpleDocTemplate(
        buf, pagesize=A4,
        rightMargin=1.8*cm, leftMargin=1.8*cm,
        topMargin=1.2*cm,   bottomMargin=1.2*cm
    )

    BLACK  = colors.HexColor("#000000")
    DGRAY  = colors.HexColor("#333333")
    MGRAY  = colors.HexColor("#555555")
    LGRAY  = colors.HexColor("#888888")
    WHITE  = colors.white

    def st(n, **kw):
        return ParagraphStyle(n, **kw)

    # ── Styles ──
    NAME   = st("NM", fontName="Helvetica-Bold",   fontSize=20, textColor=BLACK,
                alignment=TA_CENTER, spaceAfter=2, leading=24)
    TITLE  = st("TL", fontName="Helvetica-Oblique", fontSize=11, textColor=DGRAY,
                alignment=TA_CENTER, spaceAfter=4)
    CONTACT= st("CT", fontName="Helvetica",         fontSize=8.5, textColor=DGRAY,
                alignment=TA_CENTER, spaceAfter=2, leading=13)
    SH     = st("SH", fontName="Helvetica-Bold",    fontSize=9, textColor=BLACK,
                spaceBefore=7, spaceAfter=2, leading=12)
    BODY   = st("BD", fontName="Helvetica",         fontSize=8.5, textColor=DGRAY,
                leading=13, spaceAfter=2)
    BULLET = st("BL", fontName="Helvetica",         fontSize=8.5, textColor=DGRAY,
                leading=13, leftIndent=10, spaceAfter=1)
    BOLD9  = st("B9", fontName="Helvetica-Bold",    fontSize=8.5, textColor=BLACK,
                leading=13, spaceAfter=1)
    SMALL  = st("SM", fontName="Helvetica",         fontSize=8, textColor=MGRAY,
                leading=12, spaceAfter=1)
    LINK   = st("LK", fontName="Helvetica",         fontSize=8, textColor=DGRAY,
                leading=12, spaceAfter=2)

    def HR(thick=0.5, space_before=3, space_after=4):
        return HRFlowable(
            width=W, thickness=thick,
            color=colors.HexColor("#cccccc"),
            spaceBefore=space_before, spaceAfter=space_after
        )

    def section(title):
        return [
            Spacer(1, 3),
            Paragraph(title, SH),
            HR(0.6, 1, 3),
        ]

    story = []

    # ════════════════════════════════
    # HEADER
    # ════════════════════════════════
    story.append(Paragraph(user.name.upper(), NAME))

    if p and p.title:
        story.append(Paragraph(p.title, TITLE))

    # Contact line
    contacts = []
    if p:
        if p.email:
            contacts.append(f'<a href="mailto:{p.email}" color="#000000">{p.email}</a>')
        if p.phone:
            contacts.append(p.phone)
        if p.github:
            contacts.append(f'<a href="{p.github}" color="#000000">{p.github.replace("https://","").replace("http://","")}</a>')
        if p.linkedin:
            contacts.append(f'<a href="{p.linkedin}" color="#000000">{p.linkedin.replace("https://","").replace("http://","")}</a>')
        if p.portfolio:
            contacts.append(f'<a href="{p.portfolio}" color="#000000">{p.portfolio.replace("https://","").replace("http://","")}</a>')
        if p.city:
            contacts.append(p.city)

    if contacts:
        story.append(Paragraph("  |  ".join(contacts), CONTACT))

    story.append(HR(1, 4, 4))

    # ════════════════════════════════
    # PROFESSIONAL SUMMARY
    # ════════════════════════════════
    if p and p.summary and p.summary.strip():
        story += section("PROFESSIONAL SUMMARY")
        story.append(Paragraph(p.summary, BODY))

    # ════════════════════════════════
    # TECHNICAL SKILLS
    # ════════════════════════════════
    if user.skills:
        story += section("TECHNICAL SKILLS")
        skill_str = "  •  ".join([s.name for s in user.skills])
        story.append(Paragraph(skill_str, BODY))

    # ════════════════════════════════
    # PROJECTS
    # ════════════════════════════════
    if user.projects:
        story += section("PROJECTS")
        for pr in sorted(user.projects, key=lambda x: x.order):
            story.append(Paragraph(pr.name, BOLD9))
            if pr.description:
                for line in pr.description.split('\n'):
                    if line.strip():
                        story.append(Paragraph(f"• {line.strip()}", BULLET))
            if pr.tech_stack:
                story.append(Paragraph(
                    f"Tech Stack: {pr.tech_stack}", SMALL))
            lks = []
            if pr.github_link:
                lks.append(f'GitHub: <a href="{pr.github_link}" color="#000000">{pr.github_link.replace("https://","")}</a>')
            if pr.live_link:
                lks.append(f'Live: <a href="{pr.live_link}" color="#000000">{pr.live_link.replace("https://","")}</a>')
            if lks:
                story.append(Paragraph("  |  ".join(lks), LINK))
            story.append(Spacer(1, 3))

    # ════════════════════════════════
    # EXPERIENCE
    # ════════════════════════════════
    if user.experiences:
        story += section("EXPERIENCE")
        for e in sorted(user.experiences, key=lambda x: x.order):
            role_year = f'<b>{e.role}</b>'
            if e.year:
                role_year += f'  <font color="#888888">{e.year}</font>'
            story.append(Paragraph(role_year, BODY))
            if e.description:
                for line in e.description.split('\n'):
                    if line.strip():
                        story.append(Paragraph(f"• {line.strip()}", BULLET))
            story.append(Spacer(1, 3))

    # ════════════════════════════════
    # EDUCATION
    # ════════════════════════════════
    if user.educations:
        story += section("EDUCATION")
        for e in sorted(user.educations, key=lambda x: x.order):
            story.append(Paragraph(f"<b>{e.degree}</b>", BODY))
            inst = e.institute or ""
            if e.city:    inst += f", {e.city}"
            if e.batch:   inst += f"  |  {e.batch}"
            if inst:
                story.append(Paragraph(inst, SMALL))
            story.append(Spacer(1, 3))

    # ════════════════════════════════
    # CERTIFICATIONS
    # ════════════════════════════════
    if user.certificates:
        story += section("CERTIFICATIONS")
        for c in sorted(user.certificates, key=lambda x: x.order):
            line = f"• {c.name}"
            if c.link:
                line += f'  —  <a href="{c.link}" color="#000000">{c.link.replace("https://","")}</a>'
            story.append(Paragraph(line, BODY))

    # ════════════════════════════════
    # LANGUAGES
    # ════════════════════════════════
    if user.languages:
        story += section("LANGUAGES")
        lang_str = "  •  ".join([
            f"{l.name} ({l.level})" for l in user.languages
        ])
        story.append(Paragraph(lang_str, BODY))

    # ════════════════════════════════
    # BUILD PDF
    # ════════════════════════════════
    doc.build(story)
    buf.seek(0)
    return buf

@app.route("/debug-upload", methods=["GET","POST"])
def debug_upload():
    if request.method == "POST":
        f = request.files.get("testfile")
        if f:
            return f"File received: {f.filename}, size: {len(f.read())} bytes"
        return "No file received"
    return '''
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="testfile">
        <button type="submit">Upload</button>
    </form>
    '''

# ── STEP 9: INIT DB AND RUN ──
# ── STEP 9: INIT DB AND RUN ──
with app.app_context():
    db.create_all()
    for f in ["avatars","projects","certificates"]:
        os.makedirs(os.path.join("static","uploads",f),exist_ok=True)

if __name__ == "__main__":
    app.run(debug=True,port=5000)