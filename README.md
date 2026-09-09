# Personal website

A lightweight Jekyll personal website built for GitHub Pages. It contains an About page, data-driven CV, and separate Science and Extras Markdown collections. No database, server, Python, Django, or paid hosting is required.

## Publish it

1. Open **Settings → Pages** in this repository.
2. Under **Build and deployment**, choose **Deploy from a branch**.
3. Select `main`, choose `/(root)`, and click **Save**.
4. Watch the first deployment in the **Actions** tab.
5. Visit `https://jonas-lapier.github.io/personalwebsite/`.

See [EDITING.md](EDITING.md) for instructions on editing the profile, CV, blog, images, and résumé.

## Local preview (optional)

Install Ruby and Bundler, then run:

```bash
bundle install
bundle exec jekyll serve
```

Open `http://127.0.0.1:4000/personalwebsite/`.
