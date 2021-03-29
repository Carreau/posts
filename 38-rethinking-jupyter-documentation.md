<!-- 
.. title: Rethinking Jupyter Interactive Documentation
.. slug: 38-rethinking-jupyter-documentation
.. date: 2021-03-30 11:59 UTC
.. tags: python, open-source, documentation
.. category: 
.. link: 
.. description: 
.. type: markdown
-->

Jupyter Notebook first release was 8 years ago –  under the IPython Notebook
name at the time. Even if notebooks were not invented by Jupyter; they were
definitely democratized by it. Being Web powered allowed development of many
changes in Datascience world. Objects now often expose rich representation; from
Pandas dataframe with as html tables, to more recent [Scikit-learn model](https://github.com/scikit-learn/scikit-learn/pull/14180).

Today I want to look into a topic that has not evolved much since, and I believe
could use an upgrade. Accessing interactive Documentation when in a Jupyter
session.

# The current limitation for users

The current documentation of IPython and Jupyter come in a few forms, but mostly
have the same limitation. 
The typical way to reach for help is to use the `?` operator. Depending on the
the frontend you are using it will bring a pager, or a panel that will display
some information about the current object. Here is the documentation for
``numpy.linspace``

![numpy.linspace help in IPython](../img/numpy-linspace-current.png)

It can show some information about the current object (signature, file,
sub/super classes) and the raw docstring of the object. 

You can scroll around but that's about it; in terminal or Notebooks.

Compare it to the numpy website:

![numpy.linspace on numpy.org](../img/numpy-linspace-website.png)

Compared to online documentation jupyter documentation is:
 - Hard to read, 
 - Has no navigation
 - RST Directives have not been interpreted.
 - No inline graph or rendered math.

There is no access to non-docstring based documentation, narrative, tutorials or
image gallery, no search, no syntax highlighting, no way to interact or modify
documentation to test effects.

# Limitation for authors

Due to Jupyter and IPython limitations authors are often contained to document
functions.

Syntax in docstrings is often kept simple for readability, this first version is
often preferred:

```rst
You can use ``np.einsum('i->', a)`` ...
```

While the longer form that would provide an helpful link in Sphinx rendered
docs, it is shun as difficult to read.

```rst
You can use :py:func:`np.einsum('i->', a) <numpy.einsum>` ...
```

This also lead to long discussion about which syntax to use in advance area,
like formulas in [Sympy's docstrings](https://github.com/sympy/sympy/issues/14964). 

Many project have to implement dynamic docstrings; for example to include all
the parameter a function or class, would pass down using ``**kwargs``, (search
matplotlib source for `_kwdoc` , or pandas DataFrame for example.

This can make it relatively difficult for authors and contributors to properly
maintain and provide comprehensive docs.

# Stuck between a Rock and a Hard place

While Sphinx and related project are great at offering hosted HTML
documentation; extensive usage of those make interactive documentation harder to
consume;

While It is possible to [run Sphinx on the fly when rendering
docstrings](https://github.com/spyder-ide/docrepr), most Sphinx features
only work when building a full project; with the proper configuration and
extension and can be computationally intensive. This make running Sphinx locally
impractical.

Hosted website often may not reflect locally installed version of the
libraries and requires careful linking, deprecation and narrative around
platform or version specific features.

# This is fixable

For the past few month I've been working on rewriting how IPython (and hence
Jupyter) can display documentation. It works both in terminal and html context
with proper rendering, and currently understand most directive; and could be
customize to understand any new ones:

![papyri1](../img/papyri-1.png)

Above is the (terminal) documentation of `scipy.polynomial.lagfit`, see how the
single backticks are properly understood and refer to known parameter, and ``
`n` `` is incorrect as it should have double backticks; notice the rendering of
the math even in terminal. For that matter technically this does not care as to
whether the DocString is written in RST or Markdown; though I need to implement
the later part.

![papyri navigation](../img/papyri-nav.gif)

It support navigation – here in terminal – where clicking or pressing enter on a
link would bring you to the target page. In above gif you can see that many
token of code example are automatically type inferred (thanks Jedi), and are also
clickable to o to their corresponding page.

![papyri terminal-fig](../img/papyri-terminal-fig.png)

Images are included, even in terminal when they are not inline but replaced by
a button to open then in your preferred viewer.


I'm working on a number of other features, in particular :

 - rendering of narrative docs – for which I have a prototype,
 - automatic indexing of all the figures and plots –  working but slow.
 - proper cross library reference and indexing without the need for intersphinx
 
    - It is possible from the `numpy.linspace` page to see all page that
      reference it, or use it in an example (see previous image).

And many others, like showing a graph of the local references between functions,
search, and preference configure ability. I think this could also support many
other desirable features, like user preferences (hide/show type annotation,
deprecated directives,and custom coloration/syntax), though haven't started
working on these, and I have some ideas on how this could be uses to provide
translations as well.

Right now is it now as fast as efficient as I would like to – though it's faster
than running sphinx on the fly – but required some ahead of time processing. And
crash in many places, so I'm not going to link to it here yet;

I though encourage you to think about what features you are missing when using
documentation from withing Jupyter and let me know.







