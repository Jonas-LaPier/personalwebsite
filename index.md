---
layout: default
nav: about
---
<section class="hero">
  <div class="chemistry-notes" aria-hidden="true">
    <span class="reaction-note">H₂O ⇌ H⁺ + OH⁻</span>
    <svg class="molecule-mark" viewBox="0 0 160 140" role="presentation">
      <path d="M80 12 136 44 136 98 80 130 24 98 24 44Z M80 12V0 M136 44l12-7 M136 98l12 7 M80 130v10 M24 98l-12 7 M24 44l-12-7"/>
      <circle cx="80" cy="12" r="5"/><circle cx="136" cy="44" r="5"/><circle cx="136" cy="98" r="5"/><circle cx="80" cy="130" r="5"/><circle cx="24" cy="98" r="5"/><circle cx="24" cy="44" r="5"/>
    </svg>
  </div>
  <div>
    <p class="eyebrow">Hello, I’m</p>
    <h1>{{ site.title }}.</h1>
    <p class="tagline">{{ site.tagline }}</p>
  </div>
  {% if site.portrait != '' %}
    <div class="portrait-wrap">
      <img class="portrait" src="{{ site.portrait | relative_url }}" alt="Portrait of {{ site.title }}">
      <span class="element-tile" aria-hidden="true"><small>35</small><strong>Br</strong><span>Bromine</span></span>
    </div>
  {% else %}
    <div class="portrait placeholder" aria-hidden="true">{{ site.title | slice: 0 }}</div>
  {% endif %}
</section>

<section class="about-grid">
  <h2>About me</h2>
  <div class="prose">
    <p>Write a short introduction here. Share what you do, what you care about, and what you are working toward.</p>
    <p>Edit this text directly in <code>index.md</code> from the GitHub website.</p>
  </div>
</section>

<section class="contact-card">
  <div><p class="eyebrow">Let’s connect</p><h2>Have something in mind?</h2></div>
  <div class="links">
    {% if site.email != '' %}<a href="mailto:{{ site.email }}">Email me ↗</a>{% endif %}
    {% if site.linkedin_url != '' %}<a href="{{ site.linkedin_url }}">LinkedIn ↗</a>{% endif %}
    {% if site.github_url != '' %}<a href="{{ site.github_url }}">GitHub ↗</a>{% endif %}
  </div>
</section>
