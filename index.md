---
layout: default
nav: about
---
<section class="hero">
  <div>
    <p class="eyebrow">Hello, I’m</p>
    <h1>{{ site.title }}.</h1>
    <p class="tagline">Environmental chemistry, molecular chemistry, and occasionally UFOs</p>
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

<section class="contact-card">
  <div><p class="eyebrow">Let’s connect</p><h2>You can reach me here...</h2></div>
  <div class="links">
    {% if site.email != '' %}<a href="mailto:{{ site.email }}">Email ↗</a>{% endif %}
    {% if site.linkedin_url != '' %}<a href="{{ site.linkedin_url }}">LinkedIn ↗</a>{% endif %}
  </div>
</section>
