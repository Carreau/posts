<!-- 
.. title: The difficulty with Python Packaging
.. slug: the-difficulty-with-python-packaging
.. date: 2015-12-07 22:14:28 UTC
.. tags: python, packaging, thoughts
.. category: 
.. link: 
.. description: 
.. type: text
-->

Python Packaging is a hairy subject, [many]() [places]() on [the]()
[internet]() describe how to package python modules and the various choices
that you have at your disposition. 

Though, having too many choices, and having to spend time evaluating each of
these, as well as the cognitive cost to maintain all these possibilities, is
high. And also as the Zen of Python from Tim Peters says, "There should be
one-- and preferably only one --obvious way to do it". So why is not this
mantra applicable to Python packaging ?


# Steps to create a package.

I'm going here for all the steps necessary to Open Source a package. If you
where meeting for a single day, with someone from another community, interested
in how Python does it. What do you need to do ? So let's try to enumerate what
is needed:

### Step 1: Find a name.

Not too generic the name, and not taken on PyPI, because you likely want to
publish your package later. You likely want the name to be recognizable enough.
Not too close to other package name: user will be confused by `panda` vs
`panda`, or `pigments` vs `pygments`. Not too long, easy to type, and likely
with dash, or underscore for the import to match the package name. Also a valid
Python identifier, and not conflicting with standard library.

Ouch, that was tough. Tougher than I expected, though I know naming is hard. 

### Step 2: Layout your project files

Base of course on the name of your package. You want your dunder-init-dot-py
(`__init__.py`) with a DocString that explain what your package does, a
dunder-version attribute (`__version__`), likely a dunder-main-dot-py
(`__main__.py`) to invoke your package with `python -m <module>`. Figure out
how to write your `setup.py` with the right options, and the right metadata
like `requires-python` that nobody uses.

Tools like [Cookie-Cutter] can help, but you need to know the template you like, 
install it locally, clone your template, and pass the template to Cookie-Cutter.

You already need to be a seasoned Python programmer to do that correctly from
memory.

### Step 3: Vcs

Even for 1 time script, you VCS. You can choose Git, Mercurial, Darcs, or whatever.
Edit your configuration for ignore file, init, first commit, add the rights files. 

This was easy. 

### Step 4: Hosting

Make it Open-Source now, or it will never be. You likely want to host your code
online. Likely Bitbucket, GitHub, GitLab or equivalent. You need to log-in
figure out how to create a repository, set up the remote for your local copy.
And push it. Can you give me from the top of your head how to add a git/hg remote ?
(Bonus if it's over ssh so you can have your credential to push)

> git remote add github ssh://github.com/<Username>/<repo>.git

By the way you forgot your LICENSE file at step 2. If you don't put one it's
not open source. Also did you set up the corresponding ["Trove
Classifier"](https://pypi.python.org/pypi?%3Aaction=list_classifiers) ?

### Step 4: Tests

It isn't working if it doesn't have test ! So [py.test]() , [nose 1 or 2](),
unittest ? in `/test`, `/tests/` or `/<package>/test(s)/` ? Custom script to
run test ? `python -m package test` ?

I guess you start to see a pattern: No Right or Wrong answer, everyone has a
habit, and it's either too complex to decide for a beginner, or too hard even
for old bearded programmer to know by heart.

### Step 5: CI

Because I am lazy, and I don't want to run the test locally every time, I need
to set up continuous integration. Preferably hooked into the hosting platform.
You can choose among Travis-CI, Circle-CI, AppVeyor, often many of the. Each
of them with various integration procedure. Many of them need a file in your
repo, with a specific format and option depending on the language.

I'm still baffled that I have to do that at east partially manually each time. 

### Step 6: Documentation

Set-up Sphinx, its plugin, its conf.py, set-up hooks to trigger docs build, and
host on pythonhosted.org, readthedocs and GitHub-pages depending on your preference.

### Step 7 and after.

You still need to learn how to register a package on PyPI, upload it, build the
wheels deals with bug report and so on and so forth. It is too complicated. It
literally takes years to master all these tools. Initiatives like [Software
Carpentry](http://software-carpentry.org/) cannot even teach a third of this
during their bootcamp. With all the required knowledge how can you expect scientist, 
that already have a lot on their plate to also spend time open sourcing their projects ?


# A Rusty Detour. 

A few weeks ago I follow an introduction to [Rust], in particular I followed
[the rust book], that walk you through creating a rust Crate, with a binary,
create and run tests. I enjoyed it. It was easy, simple obvious, and more especially
there is one and only one obvious way to do it: Cargo.

Create a new Package? Easy :

```bash
$ Cargo new --bin hello_world
```

Test and run the package ?

```
$ Cargo test
$ cargo run
```

Oh, My, Gosh, if the package has dependencies and need to be recompiled it
install dependencies, build, link install and run test for me ! And it display
output in colors ! With useful error messages !

I learned in two days more about how to package in rust than in Python in a year !

(I would call that battery included, but that's Python Trademark)

# Easier is not always better

Let's take another ecosystem that has evolved a lot recently and which does a
great job at creating and distributing Packaging. That's one of the language I
love to Hate. Javascript has already around 4 times more packages on npm than
PyPI. In the other hand, for every task you can choose among at least 4
packages that do the same things in a slightly different manner. Also the depth
of the dependency tree seem to be often so deep that it's hard to have all
versions up to date, without any usage of deprecated features. So perhaps the
package creation in Javascript is too good to have developers actually
collaborating. Though this does not prevent to have a nice tool to create
packages. The unix philosophy has always been: "do one thing, do it well", but
has it gone too far in the python world, where we have too many tools ? Could we have one tool
that deals with packaging once and for all ?



# An opinionated library

I'm not against users having choices, but having a choice does not mean that a
tool cannot have good defaults. And good default now, might not be the same in
a few years. Though changing defaults is a [complex
subject](http://matplotlib.org/style_changes.html), default can be changed and are not fixed in stone. 

I wan an Opinionated library and command line tools that does all all that for
me, I give it a name, it check for existence on PyPI, and use Levenstein
distance to tell me whether my name is recognisable enough, and cannot be
mistaken. It create the repository on github, clone it locally, and make an
editable install I just have to tinker with.

If I ask this tool to add tests, I want it to setup Travis-CI, and hook it with
GitHub, and fill in the python-version my library support automatically. 

If I ask to set-up documentation, I want the sphinx developer-dependency to be added, 
and readthedocs integration to be setup-up. I would like an experience like that :

```bash
$ create xkcd_random_number
[Info]: "xkcd_random_number" does not exist on PyPI, and looks like a great name
[Info]: GitHub repository "Carreau/xkcd_random_number" created and set up as remote of local clone.
[Info]: Setting up package layout, author name and email, homepage...
[Info]: ... done
[Info]: Please Choose a liscence:
1: MIT
2: BSD
3: GPL
4: APACHE
5: Other
your choice : 1

$ cd xkcd_random_number
$ create --test 
[Info] adding py.test as test dependencies
[Info] creating `tests/test_xkcd_random_number.py` file
[Info] Creating `.travis.yml` file
[Info] Hooking up Travis-CI with GitHub
[Info] Done
```

Same for docs and many other things, like parsing the AST, to find out
dependencies, and warn me if I have potentially missing, or extra dependencies,
extracting version number from commit if I use a VCS. My experience, and the
experience of the package manager/creator of python packages should improve
while I'm updating my system. I should not have to configure and copy-past
fifty lines of python code `setup.py` script to get new features.




Programing is incidental (Chris Granger: https://www.youtube.com/watch?v=VZQoAKJPbh8)
