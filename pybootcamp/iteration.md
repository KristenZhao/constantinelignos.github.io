---
layout: bare
title: Control flow - Python Bootcamp
analytics: pybootcamp
---
<div class="titleblock">
  <h1>{{ page.title }}</h1>
  <h3><a href="..">Constantine Lignos</a></h3>
</div>

# Contents
{:.no_toc}
1. TOC
{:toc}

# Basic conditionals

The previous example brought up the basic structure of a Python
conditional. It looks like this:

```python
def test(x):
    """Print whether the argument evaluates as True or False."""
    if x:
        print('Evaluated as True')
    else:
        print('Evaluated as False')
```

Python has two built-in boolean constants `True` and `False`, but you
usually don't need to compare directly against them. You can specify
"else if" clauses using `elif`.

# `while` loops

Sometimes you are not sure when you'll be done processing data. For
example, let's say you want to process data until some falg is set,
but you don't have a list of it at the beginning. The solution is to
use a `while` loop. Assume for the moment you have a variable `done`
that you will use to record whether you're done:


```python
while not done:
    # Call a magic function to do work
    result = perform_work()
    # Set done if appropriate
    done = is_good_enough(result)
```

This loop will automatically stop running when `done` is set to `True`.


# Iteration tricks

Some things we didn't mention earlier:

- You can use the `break` keyword to exit from loop prematurely. For
example, if you were looking for one thing and you
found it, you might `break` rather than wasting time processing the
rest of the entries.
- You can also use an `else` clause in a `for` loop to give an action
to be performed when iteration is complete.

Here's an example using both. Let's say we want to find the index of
the first negative item in a list. We iterate over the list and return
the index when we find one.


```python
for idx, item in enumerate(alist):
    if item < 0:
        result = idx
        break
else:
    result = None
```

Also, you can use `continue` to skip to the next iteration. For
example, if you only want to process positive numbers, you might check
each item and skip some.


```python
for item in items:
    # Skip any non-positive items
    if item <= 0:
        continue

    do_something(item)
```

# Exceptions

- An exception is raised when something goes wrong.
- If an exception is unhandled, it will crash your program.
- If an exception is handled, your program can take some corrective action and continue.
- So any exceptions that you expect to occur during the normal operation of your program should be handled.

Handling is accomplished with a try…except block:

```python
try:
    # Do something risky here
except <name of exception to catch>:
    # Take some non-risky corrective action
```
