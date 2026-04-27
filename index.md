---
layout: default
title: Sovereign Content Engine
description: Guías maestras para la optimización de hardware legado y soberanía tecnológica.
---

<section class="hero">
  <h1>Sovereign<br><span class="text-gradient">Content Engine</span></h1>
  <p>Ingeniería de Optimización para Hardware Legado. Transformamos sistemas obsoletos en estaciones de trabajo eficientes.</p>
</section>

<div class="main-content">
  <h2 class="section-title">Guías de Alto Rendimiento</h2>
  
  <div class="guides-grid">
    {% for post in site.posts %}
      <a href="{{ post.url | relative_url }}" class="guide-card">
        <img src="{{ post.image | default: 'https://images.unsplash.com/photo-1550751827-4c39ad817773?auto=format&fit=crop&w=600&q=80' }}" class="card-image" alt="{{ post.title }}">
        <div class="card-body">
          <h3>{{ post.title }}</h3>
          <p>{{ post.excerpt | strip_html | truncate: 120 }}</p>
          <span class="read-more">Acceder al Manual</span>
        </div>
      </a>
    {% endfor %}
  </div>
</div>
EOF
