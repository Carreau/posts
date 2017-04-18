<!-- 
.. title: Migration to Python 3 only
.. slug: 28-migration-to-python-3-only.md
.. date: 2017-04-18 10:00:00 UTC
.. type: text
-->

This is a personal experience of having migrated IPython from being single
source Py2-Py3 to Python 3 only.

# The migration plan

The migration of IPython to be Python 3 only, started about a year ago. For the
last couple of years, the IPython code base was "single source", meaning that yo
could run it on Python 2 and Python 3 without a single change to the source
code. 

We could have made the transition to a Python 3 only code base with the use of a
transpiler (like 2to3, but 3to2), though there does not seem to be any commonly
used tools. This would also have required taking care of functionality backport,
which can be a pain, and things like async-io are quasi impossible to backport
cleanly to Python 2

So we just dropped Python 2 support


# The levels of Non-support

While it is easy to use the term "non-supported" there are different level of
non-support.

 - Do not release for Python 2, but ou can "compile" or clone/install yourself.
 - Officially saying "this software is not meant to run on Python 2", but it
   still does and is released.
 - CI Tests are run on Python 2 but "allow failure"
    - likely to break, but you accept PRs to fix things 
 - CI Tests are not run on Python 2, PR fixing things are accepted
 - PR to fix things on Python 2 are not accepted 
 - You are actively adding Python 3 only code
 - You are actively removing Python 2 code
 - You are actively keeping Python 2 compatibility, but make the software delete
   user home directory.

We settle somewhere in between adding python 3 only feature, and removing Python
2 code. 

Making a codebase Python 3 only is "easy" in the sens that adding a single `yield
from` is enough to make your code not valid Python 2, and no `__future__`
statement can fix that.


# Removing code

One of the things you will probably see in the background of this section is
that static languages would be of great help for this task. I would tend to say
"thank you captain obvious", but there is some truth. Though Python is not a
static language and we are trying to see how we can write Python in a better way
to ease the transition.

## the obvious

There are obvious functions that are present only for Python 2. In general
present in `if Py2` blocks. These can simply be deleted, and hopefully now your
linter will complain about a ton of unused variable and import you can remove. 

This is not always the case with function definition as most linter assume
function are exported. You can help with coverage, but then you have to make
sure your function is not tested separately on Python 3. 

One of the indirect effect in many places was the reduced indentation.
Especially at module level this lead to much greater readability as module-level
function are easily confused for object methods when indented in an `if py2:`


## EAFP vs LBYL

It is common in Python to use try/except in place of if/else condition. 
The well-known `hasattr` works by catching an exception, and if/else is subject
to race conditions. So it's not uncommon to hear that "Easier to Ask Forgiveness
than Permission" is preferred to  "Look Before you Leap". That might be a good
move in a codebase with requirement that will never change, though in the
context of code removal it is an hassle. Indeed when encountering a try/except
which is **likely** meant to handle a change of behavior between versions of
Python is hard to know for which version(s) of Python this was written – some
changes are between minor versions ; in which order is the try/except written
(Python 2 in the try, or in the except clause), and especially it is quasi
impossible to **find** these location. 

In the other hand explicit if statement (`if sys.version_info < (3,)`) are easy
to find – remember you only need to compare the first item of the tuple – and
easy to reduce to the only needed branch. It's also way easier to apply (and
find) these for minor versions.

The zen of Python had it right: Explicit is better than implicit. 

For me at least, `try/except ImportError, AttributeError` is a pattern I'll
avoid in favor of explicit if/else.


## byte/str/string/unicode

There is a couple location where you might have to deal with
bytes/unicode/str/string – oh boy, these names are not well chosen. In
particular in area where you are casting thing that are bytes to unicode and
vice-versa. And I can never remember when I read `cast_bytes_py2` if it's doing
nothing on Python 2, or nothing on Python 3. Though once you got the hang of it
the code is soooo much shorter and simpler and clearer in your head. 

Remember `bytes<->unicode` at boundary and keep things Unicode everywhere in
your programs if you want to avoid headache. Good Python Code is boring Python
code.

# Python 2-ism 

Dealing with removing Python 2 code made me realise that there is still a lot of
Python-2-ism in most of the Python 3 code I write.

## inheriting classes

Writing classes that do not need to inherit from `object` feels weird, and I
definitively don't have the habit (yet) of not doing it. Having the ability to
use a bare `super()` is great as I fevered remembered the order of parameter. 

## Pathlib

IPython uses a lot of path manipulation, so we keep using `os.path.join` in many
paces, or even just use the `with open(...)` context manager. If you can afford
it and target only recent python version `pathlib` and Path object are great
alternative that we tend to forget exist. 

## decode

Most of decode/encode operation do the right things, there is almost no need to
precise the encoding anywhere. This make handling `bytes-> str` conversion even
easier.


# Python 3 ism

This are the feature of Python 3 which do not have equivalent in Python 2 and
would make great addition in many code base. I tend to forget they exist and do
not design code around them enough.

# async/await

I'm just scratching the surface of async/await, and I definitively see great
opportunities here. You need to design code to work in an async-fashion, but it
should be _relatively_ straightforward to use async code from synchronous one. I
should learn more about sans-io (google is your friend) to make code reusable. 

# type anotations

Type annotation are an incredible feature that even just as visual annotation
replace numpydoc. I have a small grudge against the pep8 that describe the
position of space, but even without mypy the ability to annotate type is a huge
boon for documentation. Now docstring can focus on why/how of functions.

# kwarg only

Keyword arguments only is a great feature of Python 3, often under-appreciated
the `*`-syntax is IMHO a bit clunky – but I don't have a better option. It give
you a great flexibility in api without sacrifying backward compatibility. 
I wish I had position only as well. 




  
