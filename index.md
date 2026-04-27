---
title: Sovereign Content Engine
description: Guías maestras para la optimización de hardware legado y soberanía tecnológica.
---

<link rel="stylesheet" href="/assets/css/custom.css">

<section class="hero">
  <h1>Sovereign<br><span class="text-gradient">Content Engine</span></h1>
  <p>Ingeniería de Optimización para Hardware Legado. Transformamos sistemas obsoletos en estaciones de trabajo eficientes.</p>
</section>

<div class="main-content">
  <h2 class="section-title">Guías de Alto Rendimiento</h2>
  
  <div class="guides-grid">
    {% for post in site.posts %}
      <a href="{{ post.url | relative_url }}" class="guide-card">
        <h3>{{ post.title }}</h3>
        <p>{{ post.excerpt | strip_html | truncate: 120 }}</p>
        <span class="read-more">Acceder al Manual</span>
      </a>
    {% endfor %}
  </div>
</div>

<footer class="footer">
  <p>© 2026 Sovereign Content Engine | Especialistas en Soberanía Tecnológica</p>
  <p style="margin-top: 1rem; opacity: 0.5; font-size: 0.7rem;">Sistemas de Optimización de Bajo Nivel & Software Libre</p>
</footer>
