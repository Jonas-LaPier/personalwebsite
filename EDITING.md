# Editing the website

You can maintain the entire site from GitHub without installing anything.

## Profile and About page

- Edit `_config.yml` to change your name, tagline, email, location, social links, portrait, or résumé link.
- Edit `index.md` to change the About text.
- Upload a portrait to `assets/images/`, then set `portrait: /assets/images/your-photo.jpg` in `_config.yml`.
- Upload a PDF résumé to `assets/files/`, then set `resume_url: /assets/files/your-resume.pdf`.

## CV

Edit `_data/cv.yml`. Copy an existing section or item, preserve its indentation, and change the values. Sections and entries appear in the same order as the file.

## Science posts

1. Open `_science` and choose **Add file → Create new file**.
2. Name it `YYYY-MM-DD-short-title.md`.
3. Copy the front matter from the example science post, including `layout: science-post`, and write beneath it using Markdown.
4. To use a cover image, upload it to `assets/images/` and add these lines between the `---` markers:

```yaml
cover_image: /assets/images/my-cover.jpg
cover_alt: A useful description of the image
```

5. Commit the file to publish it.

## Extras posts

Follow the same process inside `_extras`, but begin each post with:

```yaml
---
layout: extras-post
title: Your post title
date: YYYY-MM-DD
excerpt_text: A short description for the Extras page.
---
```

Science and Extras are completely separate collections. A file added to `_science` appears only under Science; a file added to `_extras` appears only under Extras.

To keep an unpublished draft, store it outside `_science` and `_extras` until it is ready.

## Preview and publishing

After each commit, open the repository's **Actions** tab to watch the Pages build. Published changes may take several minutes to appear. For an unpublished preview, create a branch, make your edits there, and merge it into `main` when ready.
