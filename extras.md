---
layout: default
title: Extras
nav: extras
theme: dark-extras
permalink: /extras/
---
<div class="ufo-flyby" aria-hidden="true">
  <svg viewBox="0 0 180 90" role="presentation">
    <path class="ufo-beam" d="M52 58 25 88h130l-27-30Z"/>
    <ellipse class="ufo-rim" cx="90" cy="53" rx="72" ry="22"/>
    <path class="ufo-dome" d="M52 48c4-29 22-40 38-40s34 11 38 40Z"/>
    <ellipse class="ufo-body" cx="90" cy="51" rx="62" ry="16"/>
    <circle cx="52" cy="55" r="5"/><circle cx="76" cy="62" r="5"/><circle cx="104" cy="62" r="5"/><circle cx="128" cy="55" r="5"/>
  </svg>
</div>

<header class="page-head">
  <p class="eyebrow">Off the clock</p>
  <h1>Extras</h1>
  <p class="tagline">Everything else...</p>
</header>

{% assign extra_posts = site.extras | sort: 'date' | reverse %}
<section class="post-grid">
{% for post in extra_posts %}
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
  <div class="empty"><h2>Nothing strange here. Yet.</h2><p>Posts added to <code>_extras</code> will appear here.</p></div>
{% endfor %}
</section>

