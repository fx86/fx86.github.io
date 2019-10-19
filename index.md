---

title: ""
layout: single
classes:
    wide
permalink: /
author_profile: true
header:
    overlay_image: /assets/images/splash.jpg
    overlay_filter: 0.3
    image_description: ''

---

{% for post in site.posts %}
  {% include archive-single.html %}
{% endfor %}