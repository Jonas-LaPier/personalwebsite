# Editing the website

You can maintain the entire site from GitHub without installing anything.

## Profile and About page

- Edit `_config.yml` to change your name, tagline, email, location, social links, portrait, or résumé link.
- Edit `index.md` to change the About text.
- Upload a portrait to `assets/images/`, then set `portrait: /assets/images/your-photo.jpg` in `_config.yml`.
- Upload a PDF résumé to `assets/files/`, then set `resume_url: /assets/files/your-resume.pdf`.

## CV

Edit `_data/cv.yml`. Copy an existing section or item, preserve its indentation, and change the values. Sections and entries appear in the same order as the file.

## Blog posts

1. Open `_posts` and choose **Add file → Create new file**.
2. Name it `YYYY-MM-DD-short-title.md`.
3. Copy the front matter from the example post and write beneath it using Markdown.
4. To use a cover image, upload it to `assets/images/` and add these lines between the `---` markers:

```yaml
cover_image: /assets/images/my-cover.jpg
cover_alt: A useful description of the image
```

5. Commit the file to publish it. To keep a draft, store it in a `_drafts` folder instead; GitHub Pages will not publish it.

## Preview and publishing

After each commit, open the repository's **Actions** tab to watch the Pages build. Published changes may take several minutes to appear. For an unpublished preview, create a branch, make your edits there, and merge it into `main` when ready.

