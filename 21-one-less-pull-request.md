<!-- 
.. title: One less Pull Request
.. slug: 21-one-less-pull-request.md
.. date: 2016-09-26 20:00:00 UTC
.. tags: python, open-source
.. category: 
.. link: 
.. description: 
.. type: text
-->

This time of the year again, it's soon going to be the period where many
websites and organisation will push you to make contribution to Open-Source,
for example via [hacktoberfest](https://hacktoberfest.digitalocean.com/) I got
a nice T-shirt last year, and [24pullrequests](http://24pullrequests.com/) seem
to get tractions as well each years. Theses are really nice incentive that push
users of open-source to start contributing and already seasons developers to
try touch new project. 

Here is a request I got for you whether you participate or not to these events:
Please close a Pull Request. 

# Less is More

While I really appreciate having new contributions, there is a point were too
many opened pull-requests can – I think – be harmful. I'm going to expose the
various case, why I think these are harmful and what can be done.

Here are two specific examples : the [Sympy
Project](https://github.com/sympy/sympy) (as [Aaron feel
targeted](https://twitter.com/asmeurer/status/780512119024410625)), the authors
are absolutely extraordinary and reactive. The current count of opened PR is
378. [Matplotlib](https://github.com/matplotlib/matplotlib) is also apparently
at [207](https://twitter.com/tacaswell/status/780508160490692609). You can see
in the discussion linked here that maintainers feel differently about high
number of PRs.


## I open to many pull requests

I currently have 12 opened pull requests, see how many [you
have](https://github.com/pulls). This mean that I (at least) have to follow-up
with around 12 projects every days. This is an extremely hight cognitive cost
of switching. I try to not keep a PR older than 6 month. If it's older then
it's most likely not going to be merged or taken care of by the maintainers.
Every time I get to this screen I at least spend 30 sec wondering what to do
about old PRs.

My advice is to stay focus: If you are not going to work on a Pull Request, let
the maintainers know about this fact: close it. It can still be reopened. You
might want to leave a message explaining why you are not working on it, and
that you would be happy (or not), for someone else to take over.

I'm now back to 8. It fits on one screen, I can be more focused.

Also if you are a maintainer and know a pull-request will likely not get
merged, I would prefer you don't give me false hope, and close it. Explain why.
Even if it's just that's you are busy on something else and would appreciate if
this was resubmitted later. I'm more likely to get over it and try a few other
time than if my first contribution got no responses.

## I receive too many pull-requests

I strongly encourage you to try
[minrk.github.io/all-my-pulls](https://minrk.github.io/all-my-pulls/) it allows
you to view all the pull-requests you have the ability to merge. And filter by
repositories you do not wish to see. After filtering, I have 61 pull requests
in 19 repos. It is too much to stay focused as well.

Many of these pull-requests have stalled, and I would gladly appreciate for the
authors to close them if they have no intention on working on things. To be
honest many of the oldest pull-requests have entered this "Awkward state" of
wanting to close it but not actually doing so because it can be rough for the
author to see his work dismiss. 

As a maintainer I should do a better job as saying when a Pull request have
stalled and is just polluting the PR list. Close it with a nice explanation.
It's always possible to reopen if needed. GitHub allows canned responses, I use
it as a template to list the policy of PR closing. I've found that [having a
clear
policy](http://jupyter.readthedocs.io/en/latest/development_guide/closing_prs.html)
often make decision easier. And sometime closing even allow work to be
resubmitted, to appear on the top of the pile, and start anew.

There is also the possibility of taking over the author work and finishing up
in a separate PR, or push directly on authors forks if he is allowing it. I
personally rarely do that, as I feel like it is a slippery slope for the
maintainer to do everything.

I find myself much more efficient when there is only 5 to 6 opened
pull-requests. I can keep track of each of them, judge whether or not the work
will conflict and give proper care to each of these. I fail to do so when there
are many pages. 

## I don't contribute to repository that have too many PRs.

When I come across a repository with more than 20-ish pull-requests, I tend to
think that the authors are not responding so why bother to contribute. I know
that often these are only *impressions* and I can get over it because _I have
the chance_ to often know the maintainers. This feeling is though hard to get
over on repositories I'm new to.

With a high number of opened PRs, I tend to also be discouraged at searching
whether someone is fixing the bug I saw, or implementing the feature I wish.
Moreover the higher the number of opened PRs the more chance there is for the
maintainers to review my PR in a long time, and the higher chance there will be
that I will need to [rebase](https://git-scm.com/docs/git-rebase) my work,
which regardless of whether you are a git master [or
not](https://xkcd.com/1597/) can be painful process to go through (and to ask
someone to go through).

I'm pretty certain I'm not the only one to be discouraged from seeing a large
number of open non active Pull requests. I've
[asked](https://twitter.com/Mbussonn/status/780474037977751552) on twitter and
it looks like roughly every other respondent are discouraged to contribute if
too many PR are opened.

# What do you think ?

The above paragraphs are my though on too many opened pull-requests ? How are
you feeling about that ? As you might have read in the twitter conversation
linked to above, different people have different opinions.

If you want to comment, please open an [issue on
GitHub](https://github.com/Carreau/posts/issues), and if you have the courage
to help improve my English feel free to send me a PR (sic) to make this more
readable.


# Close a PR !

Thanks you for reading up until here ! If you want to restore part of the
sanity of some maintainers, or want to appeal a bit more to some users, please
go close a PRs ! Or help finish a Pr that have stalled ! I can't give you a
free T-shirt like for HactoberFest but feel free to tweet with hashtag
`#IClosedAPR` !


