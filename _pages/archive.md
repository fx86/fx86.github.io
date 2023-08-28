---

title: "Archive"
layout: single
classes: 
  - wide
  - landing
permalink: /archive
author_profile: true
header: 
    image: /assets/images/splash.jpg
    overlay_color: '#333'
    image_description: ''
    caption: "Photo credit: [**Unsplash**](https://unsplash.com/photos/uu0cOMPdM2g)"

---


{% for post in site.posts %}
  {% include archive-single.html %}
{% endfor %}