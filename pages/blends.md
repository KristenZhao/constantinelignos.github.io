---
layout: bare
title: "Quantifying cronuts: Predicting the quality of blends"
permalink: /blends/
date: 2015-07-06
analytics: blends
show: true
summary: >
  What make "frenemy" better than "framily"? Here's a preview of
  ongoing research with Hilary Prichard regarding the characteristics of good
  and bad blends and how we can build a model of which blends people like.

---

{% assign imgpath = ' /assets/blends' %}

<div class="titleblock">
  <h1>{{ page.title }}</h1>
  <h3><a href="..">Constantine Lignos</a> and <a href="http://www.ling.upenn.edu/~hilaryp/">Hilary Prichard</a>| Last updated: {{ page.date | date: '%B %d, %Y' }}</h3>
  </div>

# Coverage

## Featured in TIME Magazine

This research is featured in the July 2015 TIME Answers issue:
[Why Did 'Frenemy' Stick? Academics are unraveling the mystery behind the success--and failure--of blended words](http://time.com/3935283/why-did-frenemy-stick/).

## Slides

Our first talk on this research was given at the LSA 2015 Annual
Meeting in Portland on January 11th, 2015.  Slides for our talk can be
viewed <a href="http://1drv.ms/1tWWdjG">on office online</a>.

# Quantifying cronuts

## We are all wordsmiths

Being a linguistic innovator is hard. Just ask Gretchen Wieners of *Mean Girls*:

![Gretchen, stop trying to make fetch happen! It's not going to happen!]({{ imgpath }}/fetch.png "Gretchen, stop trying to make fetch happen! It's not going to happen!")

While it's hard to make *fetch* happen, hope for the casual wordsmith
comes in the form of the blend. Simply put, word blends (AKA
portmanteaux) combine two words to make a new one. Some popular recent
innovative blends include *mansplain*, *frenemy*, and *sext*, and there are
always the classics like *brunch* and *spork*. It's pretty common to
see a novel blend appear in a comedy series:

![Mandatory fun activities. Funtivities!]({{imgpath }}/funtivities.jpg "Mandatory fun activities. Funtivities!")

But not all blends are created equal. *Frenemy* is a great and
instantly-recognizable blend. *Framily* sounds so bad that in the
marketing campaign that introduced it, there was a commercial
discussing how you "can't mush words together like that":

<iframe width="560" height="315" src="//www.youtube.com/embed/nUr3RMlHFI0" frameborder="0" allowfullscreen></iframe>

So, how do we tell good blends from bad ones? We're conducting a
research study at the University of Pennsylvania that tries to explain
why some blends are better than others and predict which blends people
will like.

## Types of blends

Before we move on, we need to define what a blend is. For the purpose
of this study we'll define a blend as follows:

1. A combination of two independent words
1. Either the sounds of the words overlap (e.g., "ro" in *bromance*
   belongs to both words) or parts of the words were deleted to make
   the blend (e.g., *sharknado*)

So what isn't a blend?

1. A combination of two words where no sounds were deleted and they
don't overlap (e.g., *manspreading*)
1. Words that use *libfixes*, or suffixes that may have once been half
   of a blend but have been "liberated" and can apply to pretty much
   any word. A good example is *-gate* (e.g., *gamergate*).

### Blend classes

So now we know what a blend is; let's define some categories of
blends. Before we go further, some quick terminology. Let's call the
two words in the blend *source words*, and number them 1 and 2, left
to right.

1. **Complete overlap**: The sounds of the two words overlap, and all
of the sounds in words 1 and 2 are included. These are usually the
best-sounding blends. Examples: *alcoholiday, bromance, guesstimate,
mathlete, palimony, warphan*
1. **Partial overlap**: The sounds of the two words overlap, but not
   all of the sounds are preserved, some are deleted. Examples:
   *affluenza, brony, facon, sext, shitticism*
1. **No overlap**: There's no overlap between the two words, and some
   sounds were deleted so they could be put together. Examples:
   *cosplay, fanzine, sharknado, zonkey*


## Our survey

To understand how people perceive these blends, we put together a
survey and asked people to rate 88 blends. We gave them an example of
a blend without telling them what words it's made from and asked them
to answer the following questions about it:

1. Do you understand what it means? If they said no, they could skip
straight to the next word.
1. Understandability: Is it easy to understand what words make up this blend?
1. Naturalness: Does this combination of words sound natural to you?

We knew in advance that it's not always easy to decide what the
difference between understandability and naturalness is; presumably,
difficult to understand blends are also unnatural. We're most
interested in the examples where those measures don't line up: which
blends are easy to understand but unnatural (and vice versa)? We'll
look at the difference between those two measures below. For
convenience, when giving average ratings we convert the 5-point Likert
scale participants used (Terrible, Poor, Fair, Good, Excellent) to a
1-5 scale. (Note for the quantitatively minded: in the actual modeling
we perform, we don't do this conversion and do not make the interval
assumption or any normality assumptions regarding the data.)

### The best and worst blends

We had 34 people rate 88 items and we analyzed the results to determine what
the best and worst blends are. The five most understandable blends
were:

<table class="data">
<tr> <th> Blend </th> <th>Source words</th> <th> Average rating (1-5)</th>  </tr>
  <tr> <td> mathlete </td> <td>math athlete</td> <td> 4.8 </td> </tr>
  <tr> <td> sexpert </td> <td>sex expert</td> <td> 4.8 </td> </tr>
  <tr> <td> guesstimate </td> <td>guess estimate</td> <td> 4.8 </td> </tr>
  <tr> <td> televangelist </td> <td>television evangelist</td> <td> 4.7 </td> </tr>
  <tr> <td> mockumentary </td> <td>mock documentary</td> <td> 4.7 </td> </tr>
</table>


So if someone makes a mockumentary about sexperts who were mathletes,
they'll have struck blend gold! The five least understandable blends
were:

<table class="data">
<tr> <th> Blend </th> <th>Source words</th> <th> Average rating (1-5)</th>  </tr>
  <tr> <td> fozzle </td> <td>fog drizzle</td> <td> 1.8 </td> </tr>
  <tr> <td> mizzle </td> <td>mist drizzle</td> <td> 2.3 </td> </tr>
  <tr> <td> brinkles </td> <td>bed wrinkles</td> <td> 2.3 </td> </tr>
  <tr> <td> wonut </td> <td>waffle donut</td> <td> 2.5 </td> </tr>
  <tr> <td> wegotism </td> <td>we egotism</td> <td> 2.6 </td> </tr>
</table>


It's unsurprising that some of the least understandable blends are
also not very common. There's a confound here that we cannot tease
apart: novel linguistic terms are more understandable if you hear them
more often. You're more likely to say them if they're easy to
understand. But if we were to say that people give the most popular
blends the highest understandability ratings and call it a day, we'd
just be begging the question.

Here's a visualization of a sample of the best and worst blends
below. This type of plot is called a "sliding bar graph" and shows how
often each blend got each understandability rating. The items are
ordered by their average rating for understandability, best at the top.

![Sliding bar graph of a sample of blend ratings]({{ imgpath }}/understandability_slidingbar.png "'Honestly, who didn't understand 'sharknado'?")

We collected ratings for naturalness and understandability for each
blend, mostly so we could see which blends were understandable but not
natural, and vice versa. Here's a visualization of each item and how
it rates on each scale. Items above the line are perceived as more
natural than understandable; items below are more understandable than
natural. It's hosted on <a href="http://plot.ly/">plot.ly</a>, which
allows for an interactive plot. You can hover over items to see the
full info, or zoom in to tease apart the overlapping words.

<iframe width="800" height="600" frameborder="0" seamless="seamless" scrolling="no" src="https://plot.ly/~constantine.lignos/83.embed?width=800&height=600"></iframe>

So, what causes an item to be an outlier here? The blends that people
understand but find unnatural are often created for marketing
purposes: *beerstro*, *coatigan*, *croissandwich*, etc. Many of the
ones that are more natural than understandable are very similar to the
second word of the blend: *brony*, *brogrammer*, *brinkles*, etc. So,
they seem to be rated as natural because they're about one sound away
from a "real" word.

### Predicting human ratings

So how can we predict how highly people rate a blend? There are more
details in our talk, but here's a preview.

Let's say you had to reconstruct a word with only part of the
information. What if you knew just the first sounds of the word, how
would you guess the rest of it?

Google has helped you with a similar problem every time you
search. Here's what happens if you just type "linguistics is" in the
search box. (PS: You can try "linguists are" for some more
entertaining results.)

![Google autocomplete for "linguistics is"]({{ imgpath }}/autocomplete.png "Linguistics, still trying to climb out of anthropology's shadow")

We believe that people are trying to do a similar kind of autocomplete
on the source words of a blend. In the case of perfect overlap, since
all of the sounds from the source words appear in the blend, it's
trivial to figure out the source words and the blend is very easy to
understand.

But take *brinkles* (*bed wrinkles*). How would you get *bed* just
from a *b*?  Likewise, in *wonut* or *cronut*, the *donut* part is
obvious, but can you guess *waffle* from *w* or *croissant* from *cr*?

In our talk, we discussed specific statistical measures that let us
estimate how hard it is to reconstruct blends. We can use the ratings
we collected to build a statistical model of how people rate blends,
something we call a *blendometer* . Our main finding is this: it's
easy to identify the characteristics of bad blends, but good blends
come in all sizes. Bad blends are generally difficult to reconstruct
from the sounds present from the first word (e.g., just the *w-* from
*wonut*). However, some blends that are just as hard to reconstruct
still do well. It's like the challenge of predicting what might go
viral; some blends have a certain *je ne sais quoi* that escapes our
model because it's hard to quantify.

Here's a visualization of how our model compares with human ratings of
how understandable a blend is, comparing the average human rating for
an item and the average rating predicted by our model. The trend line
is there to give you an idea of how the model sees the world, not the
best fit for the data. The items below the line are rated worse by
humans than our model predicts, the items above are rated
better. (Notes for the quantitatively-minded: the model is a
cumulative link mixed-effects regression, so it's tricky to show you
its complete understanding of the data, which includes things like
estimating how far apart "good" and "excellent" are from each
other. Its predictions minimize loss on the actual Likert scale the
participants used, not the 1-5 and 0-1 numerical representations we're
using for convenience.)

<iframe width="800" height="600" frameborder="0" seamless="seamless" scrolling="no" src="https://plot.ly/~constantine.lignos/78.embed?width=800&height=600"></iframe>

It's on the right track, but it's clear that it overestimates how some
of the worst blends do, like *brinkles*, *wonut*, and *lupper*. One of
our interests in future work is investigating why those blends are as
terrible as they are. We're also trying to improve the quality of our
model and trying to predict where two words should combine to make a
blend. For example, why is it *frenemy*, not *fenemy* or *friendemy*?
It's obvious which one sounds best, and we're trying to make that as
obvious to a computer as it is to any human.

---

<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" id="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.
