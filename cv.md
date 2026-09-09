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
    {% for item in section.items limit: 3 %}{% include cv-item.html item=item %}{% endfor %}
    {% if section.items.size > 3 %}
    <details class="cv-more">
      <summary>Show {{ section.items.size | minus: 3 }} more</summary>
      {% for item in section.items offset: 3 %}{% include cv-item.html item=item %}{% endfor %}
    </details>
    {% endif %}
  </div>
</section>
{% endfor %}

<figure class="life-banner cv-banner">
  <img src="{{ '/assets/images/life-journey-banner.png' | relative_url }}" alt="Illustrated panorama connecting Spokane, Harvard, Pacific Northwest National Laboratory, chemistry research, and Stanford">
  <figcaption>AI's artistic representation of my CV... only a little bit disturbing</figcaption>
</figure>
