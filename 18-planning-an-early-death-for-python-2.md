<!--
.. title: Planning an Early Death for (~~Python 2~~) Legacy Python 
.. slug: planning-an-early-death-for-legacy-python
.. date: 2015-09-24 10:00:00 UTC
.. tags: python
.. category:
.. link:
.. description:
.. type: text
-->

On September 18 and 19, 2015, the Data Structure for Data Science workshop
gathered at UC Berkeley's BIDS [Berkeley Institute for Data Science]. It was a
productive two days of presentation, discussion and working groups — a
collaborative effort aimed at expanding what data science can do.

Despite having mostly Python developers, the workshop reached out and included
members from many other programming communities (e.g., C, C++, Julia, R, etc.)
as the workshop's explicit goal was to improve cross language operability. In
particular, the goal was to enable python's scientific computing tools
(numpy, scipy, pandas, etc.) to have a consensus backbone data-structure that
would enable easier interaction with other programming languages.

Out of the discussion arose a topic that has long plagued the python community
at large: code that requires legacy Python 2.7 is holding back the development
of data-science toolsets and – by extension – the progress of data science as a
whole. Python 2.7 was an important part of the history of scientific computing,
but now it should be left as part of that history. Thus, we convened a small
working group to plan a early death for Legacy Python.

## Move over Legacy Python once and for all.

Together @jiffyclub, @tacasswell,
@kbarbary, @teoliphant, @pzwang, @ogrisel and I (@carreau) discussed different options to push Legacy Python more or less gently through the door. We understand that some people still require Legacy Python in their code base, or
that some libraries are only available on Legacy Python. We don't blame them. Legacy Python was a great language and it's hard to move past it.  But Legacy Python is 2020; you have less than 5 years and you will ave to make the transition then. If you wait until then, it will be even harder to
transition. 

"So," we asked, "what can we do to push the transition forward".

## Choose your words.

The words you use — on the internet or in real life — influence
the people's vision of the future. To the extent that self-fulfilling prophecies are agreed to be a real thing, visions of the future determine the future. For the future of a programming language, that live and die by the people who know how to speak it, self-fulfilling prophecies are the modus operandus.

So, we propose  `Legacy Python` vs `Python`. That is, what to this date we have been calling `Python 3`, that is just `Python`. What we've referred to as `Python 2`, we instead suggest calling `Legacy Python`.  If you fear being alone; IDEs and members of the TwitterSphere are already [joining](https://twitter.com/astrofrog/status/646976176657932288) [the](https://twitter.com/almarklein/status/645542438937980929)
movement.

Beyond that, we have a grammatical suggestion, to Legacy Python in the past tense, in the way that you would speak of a dead relative that you loved dearly. Do so, in the way that one refers to "Shōwa Tennō" rather than "Hirohito" to refer to the emporer of Japan who reigned from 1926–1989. It is a term of respect, but it acknowledges an era whose end has passed. It will remind people that Legacy Python, as valuable as it a mummy or a museum exhibit at best. 

Legacy Python, fo rall its worth, had many defects:

  - you were free to fail by accidentaly mixing Unicode and bytes,
  - integer division could easily become a logical trap  (5/4 > 1)
  - the printing function was locked away (because it was not a function)
  - range object was inefficient
  - re-raised exceptions were forbidden
  - asynchrony was challenging, `yield from` did not exist
  - `super()` calls required repeating the current class.
  - tabs and spaces coudl be mixed with abandon.
  - function annotations were not possible

Legacy Python was missing many other features that are part of Python.

Do not state what's better in Python 3; it was missing/broken in
`Legacy Python`.  Much like the missing matrix multiplication operator was the missing multiplication operator included in `Python 3.5`. `Legacy Python` prevented using efficient numeric libraries relying on the numerical operator.

## Don't respond to "and on Python 2"

I pose a pledge: 

* During talks I will dismiss question regarding
`legacy Python`, and will treat questions such questions much as I would if someone asked whether I support Windows Vista. 

> Next question please.  

The less you talk about `Legacy Python`,  the more you imply Legacy Python is not a thing anymore, the less `Legacy Python` continues to exist.

## Drop support for `Legacy Python` (at least on paper)

If you a library author, you have probably had to deal with users trying your
software on `Legacy Python`, and spend lot of time making your codebase
compatible with both `Python` and `Legacy Python`.  There are a few steps you can take to push users toward using `Python`.

If a user is not willing to update to `Python`, and decides to handicap themselves with `Legacy Python`, they can most likely pin your library to be the most recent version supporting `Legacy Python`. 

### Make your examples/documentation Python 3 only

Or at least do not make effort to have examples that work using Legacy Python.
Sprinkle with function annotation, and `async`/`await` keyword can help with
communicating your example are Python 3 only.

You can even avoid mention of Legacy Python in your documentation and assume
your users are using Python 3, this will make writing documentation much easier,
and increase the chances to get examples right.

### Ask user to reproduce but on up-to-date Python version.

Have you ever had a bug report where you ask users to upgrade your libraries
dependencies ? Do the same with Python. If a user make a bug report that discusses `Python 2.7`, ask them if they can reproduce with an "up-to date version of `Python`". Even if the bug is on your side, this will have positive effects. If they really cannot upgrade they will know and will say so to you, at which point you can begin the fix. If they do upgrade and can reproduce the bug, then you'll have at least converted one user from Legacy Python (and in the meantime you might have given yourself more time to correct the bug).


### Defer `Legacy Python` support to companies like Continuum

This is already what [Nick Coghlan
recommands](http://www.curiousefficiency.org/posts/2015/04/stop-supporting-python26.html)
for `Python 2.6`, and that's what you can do for `Legacy Python` fixes. If you
have a sufficient number of user which are asking for `Legacy Python` support, accept the bug report, but as an open source maintainer do not prioritize work on it. Companies like Continuum or Enthought can work on it, and users can "buy" `Legacy Python` support for your libraries. In exchange of which the Companies could spend some of their developer time fixing `Legacy Python` bugs for your code-base.

After a quick discussion with Peter Wang, this may be possible. But for now, it is merely a hypothetical suggestion, details need to be worked out.


## Make `Python` (formerly, `Python 3`) even *more* attractive

### Create new features

Plan new features to be `Python` exclusive. Even features would be
simple to make compatible with `Legacy Python`, disable it on old platforms, or issue a warning indicating that the feature is not available on instlalations of `Legacy Python`. This will mean you are nolonger hamstrung by the requirements of `Legacy Python` — Unicode characters and other `Python` features lacking on Legacy Python will finally be available to you.

### Create new Python packages

Make new packages `Python` only. I.e., make them such that they don't need need to support `Legacy Python`. Instead, make all the design decision you didn't do on your previous package for the sake of maintaining compatibility with `Legacy Python`. `Python` libraries are much easier to create and
[build](http://flit.readthedocs.org/en/latest/)  once you are not held back by
`Legacy Python`.

## Helping Other project

Despite all the good will in the world, migration path from `Legacy Python` to `Python` is still hard. There are still a lot of things that will help current
and new projects push forward on adopting `Python`.

### Testing

All of your projects should have tests.

All of your projects should have continuous integration (e.g., [Travis CI](https://travis-ci.org/)).

Make sure that all the project you care about have continuous integration on
`Python` (include at least `3.3` and `3.4`). Build your documentation with `Python`(not `Legacy Python`). Defaults like this help ensure that Legacy Python dies and that `Python` is the default.

With continuous integration, check that your favorites projects are tested on
`Python Nightly`(the nightly build of `Python`). Most CI provider allow the tests to be ran on nightly, but let the project fail safely if those tests fail. See
[`allow_faillure`](http://docs.travis-ci.com/user/customizing-the-build/#Rows-that-are-Allowed-to-Fail) on Travis-CI for example.

### Porting `C`-extensions, move to `Cython`

The path to migrate `C`-extensions is not well documented. The preferred approach
is to use [CFFI](https://cffi.readthedocs.org/en/latest/), but there is still
a lack of well-written, centralised documentation on how to integrate with `Python` if a `C`-extension was originally built with `Legacy Python`. If you are knowledgeable in this domain, your help is welcome.


## The things we will (probably) not do.

### Friendly Haraunging

We will probbaly not make a twitter account that shame people for using `Legacy Python`. 

We might do a Parody account which says funny things, and push people toward using an up-to-date version of `Python`.

### Mild Lag Mischief

We probably won't slow code on purpose and obviously on Legacy Python:

```python
import sys
if sys.version_info[0] < 3:
    import time
    time.sleep(1)
```

Though it would be funny.

### Moderate Interface Clutter

We probably will not ask users that startup a new instance of an IDE or CLI whether they want to upgrade to Python3:

```bash
$ python2
Python 2.7.10 (default, Jul 13 2015, 12:05:58)
Type "help", "copyright", "credits" or "license" for more information.

Warning you are starting a Legacy Python interpreter. Aren't you sure you don't
want not to upgrade to a newer version ? [y]:_

```


### Severe Lag Mischief

We probably won't delay `Legacy Python` packages releases by a few weeks to incentivize migration. Though ensuring compatibility with `Legacy Python` when developing on a modern `Python` system slows down development time, and so it would be unsurprising if some delays did occur.


# Final words

If you have any ideas, send me a Pull Request — I'll be happy to discuss. 

As usual my English is far from perfect, so Pull Requests are welcomed on this blog post. Thanks to @michaelpacer did some rereading/rephrasing of
this and the first draft.



