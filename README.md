# Parasuram Portfolio 🚀

A bespoke, full-stack personal portfolio built with Django, vanilla JS, and custom CSS variables. Features dynamic SVG animations, Intersection Observers, AJAX forms, and an advanced dark-themed bento UI.

## 🛠️ Local Setup

Follow these steps to run the project locally:

1. **Clone and setup virtual environment:**
```bash
git clone <your-repo-url>
cd parasuram_portfolio
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Setup environment variables:**
Rename `.env.example` to `.env` (or create a new `.env` file) and add:
```env
DEBUG=True
SECRET_KEY=your-local-secret-key-123
ALLOWED_HOSTS=*
```

4. **Run migrations and collect static files:**
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
```

5. **Seed the database (Optional but recommended):**
To populate the site with the default structured data (Experience, Projects, Skills):
```bash
python manage.py seed_parasuram
```

6. **Start the development server:**
To avoid browser caching issues with HTTPS on localhost, run the server on a specific loopback IP:
```bash
python manage.py runserver 127.0.0.2:8000
```
Visit `http://127.0.0.2:8000` to view the site!

---

## 👨‍💻 Admin Setup

To access the Django Admin panel and modify your data dynamically:

1. Create a superuser account:
```bash
python manage.py createsuperuser
```
2. Follow the prompts for username, email, and password.
3. Visit `http://127.0.0.2:8000/admin` and log in.

---

## 📝 How to Update Content (Customisation)

The entire portfolio is fully decoupled from the HTML. You do **not** need to touch the code to update your content! 

1. **Log into the Admin Panel** (`/admin`).
2. **Profile**: Update your bio, tagline, resume, and profile photo.
3. **Skills**: Add new skills. Ensure you assign a FontAwesome class (e.g., `fa-brands fa-python`). Check the `highlight` box to feature the skill on the hero banner.
4. **Projects**: Add thumbnail images, comma-separated `tech_stack` items, and toggle `is_featured` to put them in the top Bento Grid.
5. **Journey**: Add to your Experience, Education, Certifications, and Achievements. The frontend handles timelines and formatting automatically.

---

## 🚀 Deploy to Railway

The project is already configured for production deployment using `gunicorn` and `whitenoise`.

1. **Push your code to GitHub.**
2. **Create a new Railway project** and select "Deploy from GitHub repo".
3. **Add Environment Variables** in Railway:
   - `PORT`: `8000`
   - `DEBUG`: `False`
   - `SECRET_KEY`: `<generate a secure random string>`
   - `ALLOWED_HOSTS`: `<your-railway-app-url.up.railway.app>`

Railway will automatically detect the `Procfile` and `runtime.txt`, install requirements, run collectstatic via Django hooks, and start the `gunicorn` server.

---

## 🔑 Environment Variables

| Variable | Description | Default (Local) | Production |
|----------|-------------|-----------------|------------|
| `DEBUG` | Enables detailed error pages & local static serving | `True` | `False` |
| `SECRET_KEY` | Cryptographic key for sessions/tokens | `django-insecure-...` | Secure Random String |
| `ALLOWED_HOSTS` | Domains permitted to serve the app | `*` | Your actual domain |

---
*Designed & Engineered by Mannem Parasuram.*
