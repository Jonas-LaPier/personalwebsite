---
layout: default
title: Writing
nav: blog
permalink: /blog/
---
<header class="page-head">
  <p class="eyebrow">Notes & ideas</p>
  <h1>Writing</h1>
  <p class="tagline">Occasional thoughts, field notes, and longer essays.</p>
</header>

<section class="post-grid">
{% for post in site.posts %}
  <article class="post-card">
    {% if post.cover_image %}<a href="{{ post.url | relative_url }}"><img src="{{ post.cover_image | relative_url }}" alt="{{ post.cover_alt | default: '' }}"></a>{% endif %}
    <div>
      <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %-d, %Y" }}</time>
      <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
      <p>{{ post.excerpt_text | default: post.excerpt | strip_html | truncatewords: 28 }}</p>
      <a class="read" href="{{ post.url | relative_url }}">Read article →</a>
    </div>
  </article>
{% else %}
  <div class="empty"><h2>The first post is taking shape.</h2><p>Posts added to <code>_posts</code> will appear here.</p></div>
{% endfor %}
</section>

