---
layout: default
title: CV
nav: cv
permalink: /cv/
---
<header class="page-head">
  <p class="eyebrow">Background</p>
  <h1>Curriculum vitae</h1>
  {% if site.resume_url != '' %}<a class="button" href="{{ site.resume_url | relative_url }}">Download PDF</a>{% endif %}
</header>

{% for section in site.data.cv %}
<section class="cv-section">
  <h2>{{ section.title }}</h2>
  <div>
    {% for item in section.items %}
    <article class="cv-item">
      <div class="cv-date">{{ item.start_date }}{% if item.end_date != '' %} — {{ item.end_date }}{% endif %}</div>
      <div>
        <h3>{% if item.link != '' %}<a href="{{ item.link }}">{{ item.title }} ↗</a>{% else %}{{ item.title }}{% endif %}</h3>
        {% if item.organization != '' %}<p class="meta">{{ item.organization }}{% if item.location != '' %} · {{ item.location }}{% endif %}</p>{% endif %}
        {% if item.description != '' %}<p class="description">{{ item.description }}</p>{% endif %}
      </div>
    </article>
    {% endfor %}
  </div>
</section>
{% endfor %}

