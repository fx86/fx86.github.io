---
title: "Data Science & AI Solutions | Fibinse Xavier"
layout: splash
permalink: /
date: 2025-04-28T00:00:00+05:30
header: false
feature_row:
  - image_path: assets/images/newsful_logo.png
    alt: "Newsful - Data Science Project"
    title: "Newsful AI"
    excerpt: "Uses generative AI to provide bite-sized summaries of top stories in business, finance, and global affairs."
    url: "https://newsful.ai"
    btn_label: "Explore!"
    btn_class: "btn--primary"
---


<div class="two-column-container">
  <!-- Left Column -->
  <div class="column">
    <h2 class="archive__item-title">Lab</h2>
    {% include feature_row %}
  </div>
  
  <!-- Right Column -->
  <div class="column">
    <h2 class="archive__item-title">Blog</h2>
    <ul class="post-list">
      {% assign recent_posts = site.posts | slice: 0, 10 %}
      {% for post in recent_posts %}
          <a href="{{ post.url }}">{{ post.title }}</a>
          <p class="page__meta">
            <i class="far fa-fw fa-calendar-alt" aria-hidden="true"></i>
            {{ post.date | date: "%B %d, %Y" }}
          </p>
      {% endfor %}
    </ul>
  </div>
</div>
