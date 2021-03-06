---
layout: bare
title: Home - Python Bootcamp for Researchers
analytics: pybootcamp
---
<div class="titleblock">
  <h1>{{ page.title }}</h1>
  <h3><a href="..">Constantine Lignos</a></h3>
</div>

# Tutorials

## Basics
1. [Introduction](introduction.html)
1. [Writing your first program](firstprogram.html)
1. [Basic data structures](structures.html)
1. [Iteration](iteration.html)
1. [Exercises](exercises.html)

## Intermediate
1. [More on iteration](iteration2.html)
1. [Anti-patterns](http://lignos.org/py_antipatterns/)
1. [Classes](classes.html)
1. [Odds and ends](odds-ends.html)
1. [Exercises](exercises2.html)

## Basic data analysis
1. [Introductory notebooks](intro-notebooks.html)

## Examples
1. [CSV](csv.html)
1. [Introductory IPython notebooks](notebooks.html)

---

# Examples

1. [cat](examples/cat.py): A simple version of the `cat` utility that
concatenates files given as arguments, such as chapters
[one](examples/pp_ch1.txt) and [two](examples/pp_ch2.txt) of Jane
Austen's _Pride and Prejudice_.
Run:  
`python cat.py pp_ch1.txt pp_ch2.txt`
1. [make_wordlist](examples/make_wordlist.py): Create a
frequency-sorted wordlist from a tokenized text file. Use the
[tokenized version of chapters 1-2 of _Pride and
Prejudice_](examples/pp_ch1-2_tokenized.txt) as input.
Run:  
`python make_wordlist.py pp_ch1-2_tokenized.txt > wordlist.txt`
1. [totaldict](examples/totaldict.py): Demonstrates inheritance from a
built-in class.
1. [concordance](examples/concordance.py): Builds a concordance from a
text file, such as [the first chapter of _Pride and
Prejudice_](examples/pp_ch1.txt) and report statistics for a word in
it.
Run:  
`python concordance.py pp_ch1.txt wife`

---

# Resources

1. [Dive Into Python (Mark
Pilgrim)](http://www.diveintopython.net/): This is by
far my favorite introduction to Python, and this is how I learned
Python myself. It doesn't go much into details, but it gives you the
key insights and walks you through the most important things in the
language. You get the most benefit if you've worked with a lot of
other programming languages (as he compares to them frequently), but
if you haven't this is still valuable.
1. [Non-Programmer's Tutorial for Python
2.6](http://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_2.6)
This is the best resource I've seen for new programmers learning
Python. The examples are simple and engaging, and it's quite easy to
read.
1. [Python
Tutorial](http://docs.python.org/release/2.7.2/tutorial/index.html): The
Python Tutorial is a little dry at times, but it's more comprehensive
than Dive into Python, and since it doesn't try as hard to dumb things
down it's a very accurate description of the language.
1. [Learning Python (Mark Lutz)](http://proquestcombo.safaribooksonline.com/book/programming/python/9780596805395?bookview=overview):
While the organization of the chapters will only make sense to
seasoned programmers, the content can be a bit more approachable. A
good, well-rounded introduction. (This link only works on Penn's
network.)
