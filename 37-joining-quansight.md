<!-- 
.. title: Joining QuanSight.
.. slug: 37-joining-quansight.md
.. date: 2020-04-29 11:59 UTC
.. tags: python, open-source, quansightt
.. category: 
.. link: 
.. description: 
.. type: markdown
-->

April 30th 2020 will be my Last Day at the University of California Merced, I
will be joining QuanSight and more particularly QuanSight Labs starting May
1st, and start hopefully to do more Python and Community work again. 

# A non typical background

While mostly being known for writing Python software my actual background is
actually as a (Bio)-Physicist. I've been (mostly) self-tough in everything
related to programming and Python related, which I mostly learned during my PhD
under the guidance of open-source mentors from the other end of the world when
I first stated to contribute to IPython in late 2011. 

Directly after my PhD I joined UC Berkeley as a Post Doc working full time on
Jupyter and IPython as part of the Berkeley Institute for Data Science. My
experience as an academic, programmer and open-source contributor and member of
the Scientific (Python) community gave me critically needed knowledge  about
which tools were needed to push Science Forward. 

After 2 years I had the opportunity to join University Of California Merced as
a Research Facilitator ; as most of my time I was anyway spending a large
amount of my time helping users of Python tools online and improving features
it was a good idea to officialism this role and engage in this new adventure.
Moreover it was helping with the famous 2 body problem.

# UC Merced 

The University of California Merced is the latest of the University of
California campus and is Situated in the Middle of the California Central
Valley. It is currently shy of having 10 000 students and is a quickly growing
campus which carry the mission of the University of California with a focus on
promoting and focusing on Diversity. 

As both a new and growing University, UC Merced come with a number of challenges
and opportunities.

The size of the campus (which close to doubled during my time here) means that
the person-to-person interaction are way easier and frequent than on larger
campus. The Research IT team is also embedded in the research buildings (I was
next doors to the Math, Physics and Chemistry department) Making it easy to get
to know Faculty, Staff and Students a like.

Many of the procedures, and process are still in motion at UC Merced leading to
usually way less overhead to getting things done, and also leaving the
opportunity to do tings the right way and still shape a lot of things. The
challenging counterpart being that with the growth, what is setup one day
likely need revisions every 6 month. 

With a brand new campus also come state of the art installations. I had the
chance to teach Software Carpentry on brand new media room which provided at
least one presenter screen for every 5 attendees allowing way more screen real
estate, and normal size fonts.

Speaking about real-estate, I also had the chance to help planning our 2000+
core cluster  move to a brand new data center room, with about 20 rack reserved
for current and future Research Usage. This room will also allows the available
storage available for Research to increase dramatically. One storage node on
its way to the new research facility (that we nicknamed the Borg Cube)
currently hold more storage capacity than the whole cluster had when I joined
UC Merced. We are on our way to have more than 1PB of effective storage on
site. 

On top of that we had now have brand new os on those storage nodes (CentOS 8),
with ZFS, snapshots, deduplication, RDMA etc, and we're thinking about growing
to a distributed filesystem (BeeGFS ?). And researchers have been quite
supportive of us pushing the cluster forward and understating when things might
failed. We of course have our HPC system running JupyterHub (with Dask) which
could use better Slurm integration and JupyterLab plugins :-). There are still
many things to be done (Unified user id on compute resource, and central Auth,
better monitoring, automation...etc), and in the current context, researchers
and students are looking even more for powerful infrastructure to run code, or
teach. I'm thus looking forward to see the Research IT team keep growing.


# The layers below

Even more now days with most researchers working from home on their computer,
and using cloud or on premise compute, one must not underestimate all the
work that goes on infrastructure.

During the last 18 month at UC Merced I went in practice way further down the
stack than I did before. I learned a lot on how to properly manage a system, the
trade-of of which file system to use how to configure them and what impact this
can have on overall performance, and how users can inadvertently create issues.

But at some point you hit the hardware limit, you don't want to go reboot
hundreds of machines by hand, so need proper out-of band control, and HPC tend
to consume a lot of power, so you need a proper redundant power distribution
and power load balancing. You may not think about it with your classical home
power outlet, but when you start to need to order devices that uses NEMA L5-30
and have to worry about balancing power across all the phases of your data
center there is no answer you can copy past from stack overflow.

I learn about many of those aspects during my time at UC Merced and still have
much more to learn. The team managing all of this is doing a fantastic job and
is critical to every software running on top. I'm looking forward to stay
involved but feel my skill are more on the development and higher level view of
things ; I also do miss a lot of the broader Scientific Python ecosystem,
nonetheless and despite trying my best to keep up and maintain IPython it is a
tough task when using those things less on a day-to-day basis.

# Joining QuanSight (Time to unwind the stack)

Starting May 1st (Friday) I'll be joining the fantastic team at QuanSight Labs,
to add my expertise to the growing team who works – among many other things –
on sustainability in open-source. QuanSight employs a number of open source
maintainers and experts, and if you need this expertise or guaranties about the
open-source projects you use, come [talk to us](https://www.quansight.com/),
and have a look at [QuanSight Training](https://www.quansight.com/training) and
[Residency programs](https://www.quansight.com/residency).

I have a much better understanding of how HPC works now, and I'll be unwinding
the stack relatively fast, back to application layer. Up until now I've been
keeping myself up-to-date with the regular [open-source directions podcast and
webinar](https://www.quansight.com/open-source-directions), and followed latest
project on [QuanSight Labs Blog](https://labs.quansight.org/).

I'm quite excited to join all the fantastic people there (Ralf Gommers, Carol
Willing, Anthony Scopatz, Melissa Mendonça, Aaron Meurer... and many other) and
spend more time back interacting with the Python community. Sustainability in
Open source, mentoring and taking proper care of the Community are things that
I deeply care about, and QuanSight values all of these as well.

I'm guessing you will also see me more around GitHub and on various mailing
list, I'm thus looking forward to your pull-requests and issues.
