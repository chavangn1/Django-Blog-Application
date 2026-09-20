# BlogHub — Django Blog Application

A full-stack blog platform built with Django, featuring custom user authentication with email activation, post creation with image uploads, and a commenting system.

![Uploading image.png…]()



## Features

- Custom user model with email-based login (no username field)
- Email activation flow — new accounts stay inactive until the user clicks a signed activation link sent to their inbox
- Blog post creation, editing, and deletion with photo uploads
- Commenting system with edit/delete for your own comments
- Search across blog posts
- Responsive UI built with Tailwind CSS

## Tech Stack

- **Backend:** Django 6.1
- **Database:** SQLite (dev)
- **Styling:** Tailwind CSS
- **Email:** Django's MAILERS setting — console backend in development, Gmail SMTP in production

## Getting Started

### Prerequisites
- Python 3.11+
- Node.js (for the Tailwind CLI build)

### Setup

1. Clone the repo and enter the project folder
   ```bash
   git clone https://github.com/chavangn1/Django-Blog-Application.git
   cd Django-Blog-Application
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

3. Install Python dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Install and build frontend assets
   ```bash
   npm install
   npm run build
   ```

5. Create a `.env` file in the project root with:
   ```
   SECRET_KEY=your-django-secret-key
   EMAIL_HOST_USER=your-gmail-address
   EMAIL_HOST_PASSWORD=your-gmail-app-password
   APP_BASE_URL=http://127.0.0.1:8000
   ```

6. Run migrations and start the server
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

7. Visit `http://127.0.0.1:8000` in your browser

### Notes
- In development (`DEBUG=True`), activation emails print to your terminal instead of sending for real — check your console for the activation link after registering.
- To test real email delivery, set `DEBUG=False` temporarily (this also disables Django's dev static file serving, so styling will look broken until you set it back or configure static serving separately).

## Project Structure
```
blog_main/      # Project settings, root URLs
accounts/       # Custom user model, auth views, activation flow
blogs/          # Blog post model, views, comments
templates/      # HTML templates
static/         # Tailwind source + compiled CSS
```

## License
This project is for portfolio/demonstration purposes.
