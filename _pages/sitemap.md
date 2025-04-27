---
layout: archive
title: "Sitemap"
permalink: /sitemap/
author_profile: false
---

This sitemap provides a complete overview of all content on the site. For search engines, an [XML version]({{ "sitemap.xml" | relative_url }}) is also available.

<div class="sitemap-section">
  <h2>Main Pages</h2>
  <ul class="sitemap-list">
    <li><a href="{{ '/' | relative_url }}">Home</a></li>
    <li><a href="{{ '/archive' | relative_url }}">Archive</a></li>
    <li><a href="{{ '/posts/' | relative_url }}">All Posts</a></li>
  </ul>
</div>

<div class="sitemap-section">
  <h2>Blog Posts</h2>
  <ul class="sitemap-list">
    {% for post in site.posts %}
      <li>
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
        {% if post.date %}<span class="sitemap-date">{{ post.date | date: "%B %d, %Y" }}</span>{% endif %}
      </li>
    {% endfor %}
  </ul>
</div>

<div class="sitemap-section">
  <h2>All Pages</h2>
  <ul class="sitemap-list">
    {% for page in site.pages %}
      {% if page.title and page.title != "Sitemap" %}
        <li>
          <a href="{{ page.url | relative_url }}">{{ page.title }}</a>
        </li>
      {% endif %}
    {% endfor %}
  </ul>
</div>

{% capture written_label %}'None'{% endcapture %}

{% for collection in site.collections %}
  {% unless collection.output == false or collection.label == "posts" %}
    {% capture label %}{{ collection.label }}{% endcapture %}
    {% if label != written_label %}
      <div class="sitemap-section">
        <h2>{{ label | capitalize }}</h2>
        <ul class="sitemap-list">
        {% capture written_label %}{{ label }}{% endcapture %}
    {% endif %}
    
    {% for post in collection.docs %}
      <li>
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
        {% if post.date %}<span class="sitemap-date">{{ post.date | date: "%B %d, %Y" }}</span>{% endif %}
      </li>
    {% endfor %}
    </ul>
  </div>
  {% endunless %}
{% endfor %}