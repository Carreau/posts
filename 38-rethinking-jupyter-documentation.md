<!-- 
.. title: Rethinking Jupyter Interactive Documentation
.. slug: 38-rethinking-jupyter-documentation
.. date: 2020-04-29 11:59 UTC
.. tags: python, open-source, documentation
.. category: 
.. link: 
.. description: 
.. type: markdown
-->

Jupyter Notebook first release was 8 years ago – they were then names IPython
Notebook. Even if notebooks were not invented by Jupyter; they were definitely
democratized by it ; at least in the (Scientific) Python Ecosystem. Being Web
powered also democratized a number of other changes in Datascience world; many
objects now expose rich representation; from Pandas dataframe with their
representation as html tables, to more recent Scikit-learn model.

Today I want to look into a topic that has not evolved much since, and I believe
could use an upgrade.

I will invite you to try to think "outside the box", that is to say to try to
remove all presupposition you have a bout a topic and think about what you would
expect today. There will likely be comparison to current state of things, and
other projects, and let me be upfront: the requirements and possibilities
_today_ are much different than they were a few ears ago. Storage is much
cheaper and access to a permanent connection to the internet is almost
universal. The power of personal computer have dramatically increased and it's
not uncommon to use a cluster interactively. That is in this framework that I
want to break out the boundary that are (likely)  the one we are in today. 

So stop reading for a minute or so and think about the following questions:

- As either an author, or consumer of the documentation when in an interactive
  Jupyter Session, what are the elements you are missing and the one you'd like
  to change ? What are the features missing that are available in other
  documentations ?

# The current limitation of IPython/Jupyter

The current documentation of IPython and Jupyter come in a few similar form. 
The typical way to reach for help is to use the `?` operator. Depending on the
the frontend you are using it will bring a pager, or a panel that will display
some information about the current object. 

![numpy.linspace help in IPython]()

It can show some information about the current object (signature, file,
sub/super classes) and the docstring of the object. 

If you have done your due diligence, installed the right sphinx extensions, are
in a notebook and enabled the right configuration options, you may be presented
with a nicer limited html rendering). 

You can scroll around but that's about it. 

For the neophyte, and even sometime the experienced user it can be hard (or at
least unpleasant) to read. 

Most of the formatting information for Sphinx is visible; Many directive are not
interpreted. There is no syntax highlighting, no images or plots, no rendering of
mathematical equations, no customisation possible.

Note that as well no other documentation than doc strings are available. Project
often ship with Tutorials, how to and examples, but there are no way to read
those from Jupyter Either.


# The effect on author

The limitation of the IPython/Jupyter documentation inspection have unseen
effect on documentation exhaustiveness and quality by putting an indirect
back pressure on authors.

As authors know their users may be exposed to the raw DocString
present in their code base they tend to use simplistic syntax. For example I'm
more likely to write the sort readable form:

```
    You can use ``np.einsum('i->', a)`` ...
```

Than the longer form that would provide an helpful link in Sphinx rendered docs.

```
    You can use :py:func:`np.einsum('i->', a) <numpy.einsum>` ...
```

This also lead to long discussion about which syntax to use in advance area,
like formulas in [Sympy's docstrings](https://github.com/sympy/sympy/issues/14964). 

I'm also more likely to implement dynamic docstring generation to (try to)
include all the parameter my function or class takes, than to use directive 
that would simply insert the parameter at render time. (search  matplotlib source
for `_kwdoc` for example.

This can make it relatively difficult for authors and contributors to properly
maintain and provide comprehensive docs.




