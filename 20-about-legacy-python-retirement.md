<!-- 
.. title: About Legacy Python retirement
.. slug: 20-about-legacy-python-retirement
.. date: 2015-11-29 20:00:00 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
-->

> Note, I started this writing in September, it took me a while to finish, 
> so things might have changed a bit during the writing.

This is a follow on previous post about retiring Legacy Python.  I got some
response, in particular thanks to Konrad Hinsen who took the time to ping me on
Twitter, and who responded in a [GitHub
issue](https://github.com/Carreau/carreau.github.io/issues/4).

First I want to apologize if the post felt condescending, it was not my
intention, by re-reading it I still do not feel it. Maybe this is because I'm
still not skilled enough with words in English, and this is typically the kind
of feedback I appreciate.

## Don't break user code

One other thing that seem to leek through my post was the impression I was
advocating breaking user code. What I am advocating is to make a step
forward, by actually dropping compatibility with previous version.  I really
like [semantic versioning](http://semver.org/), and as a tool maintainer, I
would not drop support for APIs in between minor revisions. Keeping backward
compatibility, is not always the easier job, and in a lot of case I fought hard
and complain about changes that shouldn't have happen, and even reverted 
pull requests. As a **developper** I would have like these changes to go in though.

What I am advocating or is for libraries to start thinking of **new** API that
would be Python 3 only.  And potentially consider new **major** revision that
does not support Legacy Python, or at least do not make efforts to support it.
This is already the path that a growing number of tools are going through.
[Nikolas](https://getnikola.com/) developers [have
decided](https://getnikola.com/blog/env-survey-results-and-the-future-of-python-27.html)
that the next version (8.0) would be Python 3 only ([more
background](http://ralsina.me/weblog/posts/floss-decision-making-in-action.html)).
I suppose the necessary modification would be minimal, but the overhead and
developer time  to support Legacy Python at the same time was too much.
Scikit-Bio is
[envisaging](https://github.com/biocore/scikit-bio-rfcs/blob/master/active/002-py3-only.md)
the same thing: whether or not they should stop trying to support python 2.
Some project have even already started [active
removal](https://github.com/janelia-flyem/gala/pull/61) of Legacy Python
compatibility layer.

Last version of [anaconda](https://www.continuum.io/downloads) can be installed
with the default root environment being Python 3.5. Some people do really
[awesome tools](https://github.com/scopatz/xonsh) which are Python 3.4+ only.

An increasing number of distribution also now come with Python 3, and python
3.5 is now considered as default installed Python more and more.  Ubuntu is
considering having Legacy Python as [persona non
grata](https://wiki.ubuntu.com/Python/FoundationsXPythonVersions) on next
stable release, and so does
[Fedora](http://news.softpedia.com/news/fedora-24-linux-operating-system-to-switch-to-python-3-5-by-default-493246.shtml)
apparently. 

Changing **major library versions** would not break old code. Or at least not
more than any other upgrade of major versions. User would still be able to pin
version of the libraries in use, and if there are dependencies conflict, your
package manager i there to resolve them. There is a specific
[`requires_python`](http://martin-thoma.com/analyzing-pypi-metadata/) metadata
that you can give to your package to indicate whether or not it's Python2/3
compatible (including minor versions), which would just prevent non-compatible
version to be installed, though it is not commonly use.  This is one the reason
the Py2/Py3 transition might look complicated to some people.  One example is
`fabric`, which is not compatible Python3, but will accept to install in a
Python3 environment. In a perfect world you would just pip install your package
and get the last compatible version without worrying about the Legacy
Python/Python 3 compatibility, but we venture in Packaging, so here be dragons.

## Python 3 does improve on Python 2

Even if, as a scientist, you might see Python as only a tool; this tool rely on
a lot of work done by other. You might not feel the difference on the day to
day basis when using Python, but , the feature that Python 3 provide do make a
difference for the developers of software stack you use. During the last few
month, we had the chance to get a new release of
[NumPy](http://docs.scipy.org/doc/numpy/release.html#numpy-1-10-0-release-notes)
that support the new python 3 `@` (aka `__matmul__`) operator, and a recent
release of Pandas, that now support more operation with `nogil`. [Matplotlib]
[released its 1.5 version](http://matplotlib.org/users/whats_new.html) and
should relatively soon release the 2.0 version that change the default [color
scheme](http://matplotlib.org/style_changes.html). These are only some of the
core packages that support the all Scientific Python infrastructure, and the
support of both Legacy Python and Python 3 is a huge pain on developers.  The
support of a single major Python version for a code base make the life of
maintainers much more easier, and Python 2.x branch is coming to end of life in
2020, we can do our best to allow these maintainer to drop the 2.x branch.

I really think that the features offered by Python 3 make maintaining packages
easier, and if it takes me 10 minutes less to track a bug down because I can
re-raise exceptions, or even get a bug report with a multiple-stage exception,
it give me 10 more minutes to answer questions.

As a side note, If you think I'm exaggerating that Legacy Python support can be a
huge overhead, I I've already spend a day [on this
bug](https://github.com/jupyter/notebook/issues/646) and I'm giving up on
writing a test that work on Python 2.

Also, for the record, re-raising exceptions, `yield`, keyword-only arguments
are things that make the science I did during my PhD easier. Maybe no better,
but easier for sure. I playing more and more with `yield from`, Python 3 Ast,
generic unpacking since then, and they also do help (understand I wish they
were there or I knew how to use them at the time). I strongly believe that the
quality and the speed at which you do science is influenced by your
environment, and Python 3 is a much nicer environment than Python 2 was. Of
course there is a learning curve, and yes it is not easy: I went through it
more than a year ago when it was harder than today. It was not fun nor was I
convince after a week, but after spending some time with Python 3, I really
feel impaired when having to go back to Legacy Python.

## Just one Python

So while not all scientist are seeing the immediate effect of Python 3, I would
really hope for all the core packages to be able to just forget about Legacy
Python compatibility and have the ability to focus their energy on only pushing
their library forward. It would really help improving the scientific stack
forward if the all SciPy related libraries could be released more often. And
one of the way to help that is to push Python 3 forward. We won't get end-user
to migrate to Python 3 if the list of available features of package are
identical. The carrots are new features.

Mostly what I would like is **only one Python**. I honestly don't think that
Python 2 has a long term future. New distribution

For the in house legacy code that scientist cannot update, I'm really sorry for
them, and it would be nice to find a solution. Maybe something close to
[PyMetabiosis](https://github.com/rguillebert/pymetabiosis) that would allow to
run Legacy Python modules inside Python 3 ? I understand the lack of funding
and/or technical competence/time to do the migration. Though asking a
volunteers based project which also lack funding to maintain backward
compatibility indefinitely seem also unreasonable. Not all project have finding
like IPython/Jupyter, and even though, those which get funding, also have
deliverable, if we don't ship the new feature we promise to our [generous
sponsors](http://blog.jupyter.org/2015/07/07/jupyter-funding-2015/), we will
likely not get out grants renewed. More generally this lead toward the question
on software sustainability in science. Is it unreasonable to ask a specific
software to work only in a restricted environment ? It is definitively convenient,
and that's why many papers now rely on VMs for results to be reproduced. But if
you want your software to be used you have to make it work on new hardware, on
new OS, which often means drivers, newer library, so why not new version of the
language you use ? How many user are still not upgrading from XP? Is it
unreasonable to ask then to install the version of libraries that were
distributed at that time?

A good single resource on how to operate the Python2 to 3 transition is likely
needed.  Matt Davis created an [example
repository](https://github.com/jiffyclub/cext23) on how to write a Python2 and
3 compatible extension. CFFI is in general something we should point user to as
it is seem to become the way which, in the long term, will lead to the less
pain for future upgrades, and even for more backward compatibility with 2.6.
[Cython](http://cython.org/) also allows to write pseudo-python that can run
closer to C-Speed. Cython also have a [pure
python](http://docs.cython.org/src/tutorial/pure.html) mode, which I think is
under-used.  I suppose that with Python 3 type-hinting, function annotation
could be used in the same way that Cython Pure Python mode [magics
atributes](http://docs.cython.org/src/tutorial/pure.html#magic-attributes)
work. This to provide Cython with some of the needed type annotations to
generate fast efficient code.  How to tackle the human problem is more
complicated. It is hard to organize a community to help scientific software
being ported to Python 3, as everyone is missing time and/or money. There is a
need to realise that in-house software written has a cost, and this cost at
some point need to be financed by institution. The current  cost is partially
hidden as it goes into Graduate student and Post-Doc time, who in the end will
write the software. The Graduate and Post-doc  often lack the best practices of
a good software engineer which leads to technical dept accumulation.

### Which path forward

The Python Scientific community is still growing. Laboratories are still
starting to adopt Python. Wether or not it is a good thing, Python 2 will reach
it's end of life is a couple of year. And despite the many in-house libraries
that still haven't been ported to Python 3, it is still completely possible and
reasonable to do science with only a Python 3 stack. It is important to make
this new generation of Python programmers to understand that the Python 3
choice is perfectly reasonable. In a perfect world the question of which python
to use should get an obvious answer, which is Python 3. Of course with time
passing, we will always have some necessity fro developers speaking Legacy
Python,  in the same way that [Nasa is looking for programmer fluent in 60
Years-old
languages](http://www.popularmechanics.com/space/a17991/voyager-1-voyager-2-retiring-engineer/)

# Alternatives

## Reviving Python 2.7

I'm Playing devil advocate here, to try to understand how this could go
forward. The scientific community is likely not the only one to use old version
of Python. Google [recommend to install Python
1.6](https://developers.google.com/google-apps/realtime/realtime-quickstart#prerequisites)
to run it's Real-time Google drive collaboration examples. So once 2.7 support
will be officially dropped by the PSF, one can imagine trying to have Google
(or any other company) taking over. I am not a lawyer, but I guess in a case of
language revival, trademark might be an issue, so this new version might need
to change name.

It is not the first time a fork of a project have became successful. From the
top of my head I can think of Gnome 2, that gave birth to Mate,  Gcc that was
forked to Egcs, (which in the end was re-named Gcc), as well as Libre
Office, successful alternative to it's "Open" sibling.

Seeing that the Scientific community has already a lack of time and funding, I
find the chance of this happening slim. 

## Leapfrog

One of the main pain in the transition to Python 3 is keeping compatibility
with both Python. Maybe one of the solution that will come up is actually
jumping over all this Python 2/3 problem to an alternative interpreter like
PyPy, which got a [brand new
release](http://morepypy.blogspot.com/2015/10/pypy-400-released-jit-with-simd.html).
The promises of PyPy is to make your Python code as fast as C, removing most of
the need to write lower level languages. Other alternative interpreter like
[Pyston](https://github.com/dropbox/pyston) and
[Pyjion](https://github.com/Microsoft/Pyjion) are also trying to use
Just-In-Time compilation to improve Python performance.  For sure it still need
some manual intervention, but if it can highly decrease the amount of work
needed.  I'm still unsure that this is a good solution as C-API/ABI
compatibility CPython 2.x is a complex task that does hinder language
development.  More generally, CPython implementation details, do leak into the
language definitions and make alternative implementation harder.


## Conversion tools

The Julia community dealt with migrating code from Fortran by writing a
[Fortran-to-julia
transpiler](http://thisweekinjulia.github.io/julia/2014/10/10/October-10.html),
Python have the [2to3](https://docs.python.org/3.6/library/2to3.html) and now
[python-modernize](https://github.com/mitsuhiko/python-modernize) tools, it might be
possible to write better conversion tools that handle common use
case more seamlessly, or even import-hooks that would allow to import packages cross versions ?
Maybe having a [common AST](https://github.com/almarklein/commonast) module for
all version of Python and have tools [working more
together](https://github.com/davidhalter/jedi/issues/630) is the way forward. 



# Step forward

Make Python 3 adoption easier, or make it clearer what is not Python 3
compatible, both for humans and machine. There are some simple steps that can
be taken: Make sure you favorite library run tests on latest python version,
it's often [not too much
work](https://twitter.com/RipLegacyPython/status/663054068961538049).

Point the default docs at Python 3 using canonical links. I too often come
across example that point to Python 2 docs, because they are better referenced
by Google.  Often the difference LPy/Py3 is small enough that example works,
but when it does not, it give the impression that Python 3 is broken.



Tell us what you think, what you use, what you want, what you need, what you
can't do.


