---
layout: default
title: Posts
---
#Posts

<div class="titleblock">
{% assign sortedpages = (site.pages | sort: 'title') %}
{% for post in sortedpages %}
{% if post.show  %}

  <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
  <p>Last updated: {{ post.date | date: '%B %d, %Y' }}<br />
  {{ post.summary }}</p>
{% endif %}
{% endfor %}
</div>
