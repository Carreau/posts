<!-- 
.. title: One less Pull Request Followup
.. slug: 22-one-less-pull-request-followup.md
.. date: 2016-09-27 20:00:00 UTC
.. type: text
-->


My earlier blog post could not have been more timely, here is what I received
this morning:

> Hacktoberfest is back! Ready to hack away?

> It’s that time of year again! [Hacktoberfest
> 2016](https://hacktoberfest.digitalocean.com/) is right around the corner and
> we’re back with new, featured projects and the chance to win the
> limited-edition Hacktoberfest T-shirt you all love. 

> Read the [blog
> post](https://www.digitalocean.com/company/blog/ready-set-hacktoberfest/) to
> see what’s changed this year and share on your favorite social media networks
> with #Hacktoberfest.


# Community Feedback. 

I quickly got some feedback in particular from [Aaron
Meurer](https://twitter.com/Mbussonn/status/780617317759672320). First there is
no comment box on this blog. I tried it's painful to maintain, need moderation
(...etc) so you can ping me on twitter, or [open a
GitHub](https://github.com/carreau/posts/issues/new). I think it's a high
enough filter, if you have something to say to what I write here, you (likely)
already have a GitHub account.

Also, I ran [a poll](https://twitter.com/Mbussonn/status/780474037977751552) on
twitter, with 41 responses, 51% (I assume 21 users) prefer few PRs. 49% (20
users) don't really count. So there is definitively a non-negligible population
that will still be ok to contribute. This also explains Aaron tweet:

> if the number of pull requests discouraged pull requests we wouldn't have so
> many pull requests

I would argue that if 50% of your users are not discouraged, you still
discourage the other half. Which might be fine according to your own metrics. 

## How to close ?

Aaron expressed his concern that closing a PR without a comment might send the
unintended message that:

  - The maintainer does not want your code (assuming the maintainer closes)
  - The Author does not want the project to get his code anymore (assuming the
    author closes)

It might not have been clear enough in earlier post but when closing please,
explain why you are closing, and what you expect. Here is one example of the
[IPython repository](https://github.com/ipython/ipython/pull/5373) where the
maintainers have close the PR:

> @takluyver and @ellisonbg have decided that we are going to close this PR and
> open an issue. We are still interested in this work going in, but the tests
> need to be written first. Feel free to re-open when the tests are ready.

If you are closing your own work, please make it clear whether:

 - You plan to work later on that
 - If what you did can be reuse by future developers.


## When not to close

Aaron pointed again that as a maintainer he prefers to keep PRs open. Now that
GitHub allows you to give maintainers ability to push on your branch, You can
give maintainers the ability to push on the PR. In case you disagree whether
the PR should be close or not, exchange with the maintainer. The commits of a
close PR can still be accessed and maybe a best course of action is for the
maintainer to for your branch and re-issue the PR. They will have more control
over it. Regardless discuss with the maintainer, convey your intent. 

## Look deeper into maintainers habits.

I purposely avoided the subject, but [Andreas
Mueller](https://twitter.com/amuellerml/status/780735097129558016) pointed out
that you can actually look at recently merged PRs, and commit history. Only if
all PR are old is Andreas discouraged. 

This is a valid strategy, but it requires time from the person that want to
submit the PR. And it's not always easy to do. I tend to go this extra step
when I really think the PR is worth it. 

# Things are subjective

Again, all these are personal thoughts and preferences. I prefer to have few
PR, like I would prefer to have zero-inbox. I would be curious to see analysis
of general _type_ of contribution vs number of opened PRs. Are novice users
less likely to contribute depending on the number of opened PRs? Are the
structures of networks across project different ?


Happy HacktoberFest.
