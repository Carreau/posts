<!-- 
.. title: Planning an early death for Python 2
.. slug: planning-an-early-death-for-python-2
.. date: 2015-09-24 10:00:00 UTC
.. tags: python, draft
.. category:
.. link: 
.. description: 
.. type: text
-->

Last Friday and Saturday the Data Structure for Data Science workshop was
happening at UC Berkeley BIDS. It was a productive two days of presentation,
discussion and working groups to push the bleeding edge of what data science
can do.

Despite having mostly Python developers, the workshop was welcoming for
developer of other communities like C, C++, Julia, R, etc.. as one of the goal
was to improve cross language operability. 

One of the things that though is still holding back datascience and the advance
of the tooling around it in the Python community is the old code which are
still requiring Legacy Python 2.7 . We thus decided hod a small working group
to plan a early death for Legacy Python.

## move over Legacy Python once and for all. 

In collaboration with many developers among @jiffyclub, @tacasswell, @kbarbary,
@teoliphant, @pzwang, @ogrisel, we discussed different options to push Legacy
Python more or less gently through the door. We understand
that some people are still requiring the use of Legacy Python in their code
base, or require some libraries which are still only available on Legacy Python
and don't blame them.  We understand that Legacy Python was a great language
and that it's hard to move over it.  Though the retirement of Legacy Python is
2020, you will ave to make the transition then, and it will be even harder to
transition at that point.

So what are the step we can do to push the transition forward.

## Choose your words. 

The choice of words you make on the internet and in real life will influence
the vision people have for Legacy Python vs Python. Assume that Python 3 is
just Python, and refer to Python 2 as legacy python.  IDEs and TwitterSphere is
[starting](https://twitter.com/astrofrog/status/646976176657932288) to [do
that](https://twitter.com/almarklein/status/645542438937980929), join the
movement. 

Refer to Legacy Python in the past tense. It will reinforce the old and
deprecated state of Legacy Python. I still don't understand why people would
like to stay with a language which that many defects:

  - it did not protect you from mixing Unicode and bytes, 
  - tripped you with integer division
  - did not allow you to replace the printing function
  - had a range object which is not memory efficient
  - did not permit to re-raise exception
  - had a bad asynchronous support, without yield from
  - forced you to repeat the current class in `super()` call.
  - let you mix tab and space.
  - did not support function annotations

Legacy Python was missing many other feature which are now part of Python.

Do not state what's better in Python 3, state that it was missing/broken in
Legacy Python.  Like the missing matrix multiplication operator was missing
multiplication operator. Legacy Python was preventing people to use efficient
numeric library which are relying on the numerical operator.

## Don't respond to "and on Python 2"

Personally during talks I plan to not pay attention to question regarding
legacy Python, and will treat questions such questions as someone asking whether
I support windows Vista. Next question please. The less you talk about Legacy Python
the more you imply Legacy Python  is not a thing anymore.


## Drop support for Legacy Python (at least on paper)

If you a library author, you have probably had to deal with user trying your
software on Legacy Python, and spend lot of time making your codebase
compatible with both Python 3 and legacy Python.  There are a few step you can
take to push user toward Python 3.

### Make your examples/documentation Python 3 only

Or at least do not make effort to have examples that work using Legacy Python.
Sprinkle with function annotation, and `async`/`await` keyword can help with
communicating your example are Python 3 only.

You can even avoid mention of Legacy Python in your documentation and assume
your users are using Python 3, this will make writing documentation much easier
to get right.


### Ask user to reproduce but on up-to-date Python version. 

Have you ever had a bug report where you ask users to upgrade your libraries
dependencies ? Do the same with Python. If a user make a bug report with Python
2.7 ask them if they can reproduce with an up-to date version of Python, even
if the bug is obviously from your side.  If they really can't upgrade they will
know, if they do and can reproduce, then you'll have at least converted one
user from Legacy Python (and in the meantime you might have already corrected the bug).


### Defer 2.7 support to companies like Continuum

This is already what some [Nick Coghlan
recommands](http://www.curiousefficiency.org/posts/2015/04/stop-supporting-python26.html)
for Python 2.6, and that's what you can do for Legacy Python fix only. If you
have a sufficient number of user which are asking for 2.7 support, accept the
bug report, but as an open source maintainer do not work on it. You can partner
with companies like Continuum or Enthought, from which user would "buy" 2.7 support
for your libraries, in exchange of which the Companies could spend some of their 
developer time fixing your Legacy Python bugs. 

After a quick discussion with Peter Wang, it would be possible, but details
need to be worked on.


## Make Python 3 attractive

### Create new features

Plan you new features explicitly for Python 3, even if the feature would be
simple to make Legacy Python compatible, disable it on old platforms, and issue
a warning indicating that the feature is not available on Legacy Python
install. 

You will be able to use all the shiny Python features which are lacking on Legacy Python
like Unicode characters!

### Create new Python packages

Make new packages Python 3 only, and make all the design decision you didn't do
on your previous package. Pure python libraries are much easier to create and
[build](http://flit.readthedocs.org/en/latest/)  once you are not hold back by
legacy Python.


## Helping Other project

Despite all the good will in the world the Migration path from Legacy Python
can be hard.  There are still a lot of things that can be done to help current
and new project to push forward the adoption of Python.

### Testing

Make sure that all the project you care about have continuous integration on
Python 3, if possible even the documentation building done with Python 3, help
to make Python 3 the default. 

With continuous integration, check that your favorites projects are tested on
Python Nightly, most CI provider allow the tests to be ran on nightly, but do
not make the status of the project turn red if the test are failing. See 
[`allow_faillure`](http://docs.travis-ci.com/user/customizing-the-build/#Rows-that-are-Allowed-to-Fail)
on Travis-CI for example.

### Porting C-extensions, move to Cython

The path to migrate C-extension is not well documented, the preferred approach
is to use CFFI, but there is still alack of well written centralised, document
on how to integrate with Python 3. IF you are knowledgeable on this domain, your help is welcomed. 



## the things we will (probably) not do. 

Make a twitter account that shame people that use Legacy Python, though we
might do a Parody account which say funny things, and push people toward Python 3.

Slow code on purpose and obviously on Legacy Python:

```python
import sys
if sys.version_info[0] < 3:
    import time
    time.sleep(1)
```

Though it would be fun.

Ask user at IDE/CLI startup time if they want to upgrade to Python3:

```bash
$ python2
Python 2.7.10 (default, Jul 13 2015, 12:05:58)
Type "help", "copyright", "credits" or "license" for more information.

Warning you are starting a Legacy Python interpreter. Aren't you sure you don't
want not to upgrade to a newer version ? [y]:_

```

Delay Legacy Python packages releases by a few weeks to incentive people to
migrate, or should we actually consider the people on Python 2 as guinea pig
and release nightly ?


# End word

Remember, Legacy Python is responsible for global warming, encourage people to
stay with IE6, and is voting for Donald Trump.


As usual my English is far from perfect, so Pull Request welcomed on this blog
post. 



