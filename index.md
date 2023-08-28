---

title: ""
layout: single
permalink: /
classes: 
  - wide
  - landing
author_profile: true
header: 
    image: /assets/images/splash.jpg
    image_description: ''
    caption: "Photo credit: [**Unsplash**](https://unsplash.com/photos/uu0cOMPdM2g)"

---

{% for post in site.posts %}
  {% include archive-single.html %}
{% endfor %}