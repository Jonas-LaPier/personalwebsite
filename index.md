---
layout: default
nav: about
---
<section class="hero">
  <div>
    <p class="eyebrow">Hello, I’m</p>
    <h1>{{ site.title }}.</h1>
    <p class="tagline">{{ site.tagline }}</p>
  </div>
  {% if site.portrait != '' %}
    <div class="portrait-wrap">
      <img class="portrait" src="{{ site.portrait | relative_url }}" alt="Portrait of {{ site.title }}">
    </div>
  {% else %}
    <div class="portrait placeholder" aria-hidden="true">{{ site.title | slice: 0 }}</div>
  {% endif %}
</section>

<div class="molecule-field" aria-hidden="true"></div>

<section class="about-grid">
  <h2>About me</h2>
  <div class="prose">
    <p>Write a short introduction here. Share what you do, what you care about, and what you are working toward.</p>
    <p>Edit this text directly in <code>index.md</code> from the GitHub website.</p>
  </div>
</section>

<figure class="life-banner">
  <img src="{{ '/assets/images/life-journey-banner.png' | relative_url }}" alt="Illustrated panorama connecting Spokane, Harvard, Pacific Northwest National Laboratory, chemistry research, and Stanford">
  <figcaption>AI's artistic representation of my CV</figcaption>
</figure>

<section class="contact-card">
  <div><p class="eyebrow">Let’s connect</p><h2>Have something in mind?</h2></div>
  <div class="links">
    {% if site.email != '' %}<a href="mailto:{{ site.email }}">Email me ↗</a>{% endif %}
    {% if site.linkedin_url != '' %}<a href="{{ site.linkedin_url }}">LinkedIn ↗</a>{% endif %}
    {% if site.github_url != '' %}<a href="{{ site.github_url }}">GitHub ↗</a>{% endif %}
  </div>
</section>
