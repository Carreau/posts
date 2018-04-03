<!-- 
.. title: The Pleasure of deleting code
.. slug: 34-the-pleasure-of-deleting-code.md
.. date: 2018-04-03 13:30 UTC
.. tags: python, open-source, best-practices 
.. category: 
.. link: 
.. description: 
.. type: markdown
-->

# Good Code is Deleted Code

The only code without bugs is [no
code](https://github.com/kelseyhightower/nocode). And the less code you have,
the less mental load as well. This is why it is often a pleasure to delete a lot
of code. 

In IPython we recently bumped the version number to 7.0 and [dropped support for
Python 3.3](https://github.com/ipython/ipython/pull/10833). This was the
occasion to clean, and remove a lots of code that insure compatibility with
multiple minor Python version, and while it may seem easy it required a lot of
thinking ahead of time to make the process simple. 

## Finding what can (and should be deleted)

The hardest part is not deleting the code itself, but finding what can be
deleted. In many compiled languages, the compiler may help you, but with Python
it can be quite tougher, and some of Python usual practices make it harder.

Here are a few tips on how to prepare your code (when you write it) for
deletion. 

### EAFP vs LBYL

Python tend to be more on the Easier to ask Forgiveness than Permission, than
Look Before You Leap. It is thus common to see [code like](https://github.com/ipython/ipython/issues/11068):

    try: 
         from importlib import reload 
    except ImportError : 
         from imp import reload 

In this particular case though, why do we use the try/except ? Unless there is
a comment attached, it is hard guess that `from imp import reload` was
deprecated since python 3.4, the comment can easily get out of sync with the
actual code. 

A better way would be to explicitly check `sys.version_info`

    if sys.version_info < (3, 4):
         from imp import reload 
    else:
         from importlib import reload 

(Note, tuple from unequal length can be compared in python). 

It is now obvious which code should be removed and when. You can see that as
"Explicit is better than implicit" rule. 


## Deprecated code

Removing legacy deprecated code is also always a challenge, as you may be
worried of other library might be still relying deprecation. To help with that
let's see how we can improve typical deprecation, here is a typical deprecated
method from IPython::

    def unicode_std_stream(stream='stdout'):
        """DEPRECATED"""
        warn("IPython.utils.io.unicode_std_stream is deprecated", DeprecationWarning)
        ...

How much are you confident you can remove this ? A few question should pop into
your head:
  - Since when has this function been deprecated ? 

    def unicode_std_stream(stream='stdout'):
        """DEPRECATED"""
        warn("IPython.utils.io.unicode_std_stream is deprecated since IPython 4.0", DeprecationWarning)
        ...
    

With this new snippet I'm confident it's been 3 versions and I am more willing
to delete. This also helps downstream libraries to know whether they need
conditional code or now. I'm still unsure downstream maintainer have updated
their code. Let's add a stacklevel (to help them find where the deprecated
function is used, and add more informations about how they can replace code uses
this function:


    def unicode_std_stream(stream='stdout'):
        """DEPRECATED, moved to nbconvert.utils.io"""
        warn("IPython.utils.io.unicode_std_stream has moved to nbconvert.utils.io since IPython 4.0", DeprecationWarning, stacklevel=2)
        ...

Well with this information I'm even more confident downstream maintainer have
updated their code. They have an actionable item: replace one import for
another, and are more likely to do that, than dig for 1h in history to figure
out what to do. 


# TLDR

- Be explicit in your conditional import that depends on version of underlying
python or library. 

- take time to write good deprecation warning with : 
  - Stacklevel (=2 most of the time) 
  - Since When it was deprecated.
  - What should replace deprecated call for consumers. 

The time you put in these will greatly help your downstream consumers, and
benefit you later to simplify getting rid of lots of code easily.








