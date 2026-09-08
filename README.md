# Personal website

A clean Django portfolio with an editable About page, flexible CV sections, and a draft/publish blog with image uploads.

## Start locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/`. Sign in at `http://127.0.0.1:8000/admin/` to edit everything.

## How editing works

- **About:** edit the single Site Profile, including portrait, bio, contact links, and downloadable résumé.
- **CV:** create headings under CV Sections, then add and reorder entries inside each heading.
- **Blog:** create a Blog Post, upload an optional cover image, leave it as Draft while writing, then set a publication date and choose Published.

## Deploy on Render

This repository includes a Render Blueprint. It provisions a Django web service and a 1 GB persistent disk so blog images, your résumé, profile image, and SQLite database survive redeploys.

1. Sign in to Render and choose **New → Blueprint**.
2. Connect the GitHub repository and select `Jonas-LaPier/personalwebsite`.
3. Render finds `render.yaml`. Before applying it, set `CSRF_TRUSTED_ORIGINS` to the eventual HTTPS URL, such as `https://personalwebsite.onrender.com`.
4. Apply the Blueprint and wait for the health check to turn green.
5. In the service's **Shell**, run `python manage.py createsuperuser`.
6. Visit `/admin/`, sign in, and replace the placeholder profile content.

The persistent disk requires a paid Render web-service plan. A free service has an ephemeral filesystem, so admin edits and uploaded files would be lost during restarts or redeployments.

## Verify a deployment

1. Open `/healthz/` and confirm it displays `{\"status\": \"ok\"}`.
2. Open `/admin/`, create a CV section and entry, and confirm they appear at `/cv/`.
3. Create a draft blog post and confirm it is hidden from `/blog/`.
4. Publish it, upload a cover image, and confirm both the listing and article page work.
5. Trigger **Manual Deploy → Deploy latest commit** in Render and confirm the content and uploads remain afterward.
6. Check the About, CV, Writing, and article pages at desktop and mobile widths.

Every push to `main` triggers an automatic Render deployment. Deployment status and logs are available on the service's **Events** and **Logs** tabs.
