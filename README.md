# Jonas LaPier — personal website

This repository contains the content for my personal website. Most routine updates can be made directly on GitHub without installing anything.

## Publishing a Science post

1. Open the [`_science`](./_science) folder.
2. Click **Add file → Create new file**.
3. Name the file `YYYY-MM-DD-short-title.md`, using lowercase words separated by hyphens. Example: `2026-10-15-clean-water-electrochemistry.md`.
4. Begin the file with this front matter:

```yaml
---
layout: science-post
title: Your post title
date: 2026-10-15
excerpt_text: A one- or two-sentence preview shown on the Science page.
---
```

5. Write the article beneath the closing `---` using Markdown.
6. Select **Commit changes** to publish it.

The post will appear automatically on the [Science page](https://jonas-lapier.github.io/personalwebsite/science/), with the newest date first.

## Publishing an Extras post

Follow the same process in the [`_extras`](./_extras) folder, but use this front matter:

```yaml
---
layout: extras-post
title: Your post title
date: 2026-10-15
excerpt_text: A short preview shown on the Extras page.
---
```

Extras posts appear only on the dark-themed [Extras page](https://jonas-lapier.github.io/personalwebsite/extras/). Science and Extras are separate collections, so the folder and `layout` value should match.

## Writing with Markdown

```markdown
## Section heading

Normal paragraph text with **bold**, *italics*, and a [link](https://example.com).

- A bulleted item
- Another item

1. A numbered item
2. Another item

> A quotation or highlighted statement.
```

Leave a blank line between paragraphs, headings, lists, and images.

## Adding a cover image

1. Upload the image to [`assets/images`](./assets/images) using **Add file → Upload files**.
2. Use a concise filename without spaces, such as `pfas-reactor.jpg`.
3. Add these fields to the post’s front matter:

```yaml
cover_image: /assets/images/pfas-reactor.jpg
cover_alt: Glass electrochemical reactor on a laboratory bench
```

`cover_alt` should briefly describe the image for visitors using screen readers. JPG or WebP is usually best for photographs, while PNG is useful for diagrams and illustrations.

To place an image inside a post, use:

```markdown
![A useful description]({{ site.baseurl }}/assets/images/pfas-reactor.jpg)
```

## Saving a draft

Only files inside `_science` and `_extras` are published. To keep a draft:

1. Create or edit the post on a separate GitHub branch, or keep the Markdown file outside those two folders.
2. Preview the changes in GitHub’s editor.
3. Move the finished file into the appropriate collection and commit it to `main` when ready.

## Editing or removing a post

- To edit: open the Markdown file, click the pencil icon, make changes, and commit.
- To unpublish without deleting: move the file outside `_science` or `_extras`.
- To delete: open the file, use the file menu to delete it, and commit the deletion.
- To change the displayed order: edit the `date` in the front matter.

Changing a filename changes that post’s URL. Avoid renaming published posts unless necessary, because existing links may stop working.

## Updating the CV

Edit [`_data/cv.yml`](./_data/cv.yml). Each section contains an `items` list. A typical entry looks like:

```yaml
- title: Your position, degree, publication, or award
  organization: Organization or citation details
  location: City, State
  start_date: "2025"
  end_date: Present
  description: A concise description
  details:
    - Optional bullet point
    - Another optional bullet point
  link: https://example.com
```

Important details:

- Preserve the indentation—YAML uses spaces to understand the structure.
- Put quotation marks around years when useful, especially a value such as `"2025"`.
- Use `""` for an intentionally blank field.
- Entries appear in file order.
- Only the first three entries in each section show initially; remaining entries appear under **Show more**.
- Copy an existing entry before editing it to reduce formatting mistakes.

## Replacing the downloadable CV

1. Open [`assets/files`](./assets/files).
2. Upload the new PDF using the existing filename `LaPier_CV.pdf` so the link does not need to change.
3. If the filename changes, update `resume_url` in [`_config.yml`](./_config.yml).

## Editing the homepage

- Edit [`index.md`](./index.md) to change the About text or contact-section wording.
- Edit [`_config.yml`](./_config.yml) to change the name, tagline, email, location, LinkedIn address, portrait, or résumé link.
- Replace `assets/images/jonas-lapier.webp` to update the portrait without changing the configuration.
- The illustrated CV banner is referenced near the bottom of [`cv.md`](./cv.md).

## Checking an update

After committing a change:

1. Open the repository’s **Actions** tab.
2. Wait for the Pages build to complete successfully.
3. Open the relevant page and refresh it.
4. Check the page at both desktop and phone widths, especially after adding a long title or large image.

Publishing normally takes a few minutes. If a build fails after editing YAML or front matter, check indentation, paired quotation marks, and the opening and closing `---` lines first.
