<!-- 
.. title: Open in Binder Browser Extension
.. slug: 31-open-in-binder-browser-extension
.. date: 2017-11-22 17:25:31 UTC
.. tags: firefox, binder
.. category: 
.. link: 
.. description: 
.. type: text
-->

Today I am please to announce the release of a first project I've been working
on for a bout a week: A Firefox extension to open the GitHub repository you are
visiting using MyBinder.org. 

If you are in a hurry, just head there to [Install version 0.1.0 for
Firefox](https://addons.mozilla.org/en-US/firefox/addon/open-with-binder/).
If you like to know more read on. 

![Binder Logo](img/binder_logo_128x128.png)


## Back to Firefox.

I've been using Chrome for a couple of years now, but heard a lot of good stuff
about [Rust](https://www.rust-lang.org/en-US/) and all the good stuff it has
done or [Firefox](https://blog.mozilla.org/blog/2017/11/14/introducing-firefox-quantum/). 
Ok that's a bit of marketing but it got me to retry Firefox (Nightly please),
and except for my password manager which took some week to update to the new
Firefox API, I rapidly barely used Chrome. 

![Firefox Nightly Logo](img/Firefox_Nightly_Logo_2017.png)

## MyBinder.org

I'm also spending more and more time working with the JupyterHub team on
[Binder](https://MyBinder.org), and see more and more developer adding binder
badges to their repository. Mid of last week I though:

> You know what's not optimal? It's painful to browse repositories that don't
> have the binder badge on MyBinder.org, also sometime you have to _find_ the
> badge which is at the bottom of the readme.

You know what would be great to fix that ? A button in the toolbar doing the
work for me.

## Writing the extension

As I know Mozilla (which has a not so great [new
design](https://blog.mozilla.org/opendesign/mdns-new-design-beta/) BTW, but
personal opinion) cares about making standard and things simple for their users,
I though I would have a look at the new
[WebExtension](https://developer.mozilla.org/en-US/Add-ons/WebExtensions).

And 7 days later, after a couple of 30 minutes break, I present to you a
staggering 27 lines (including 7 line business logic) extension that does that:


    (function() {
      function handleClick(){
        browser.tabs.query({active: true, currentWindow: true})
        .then((tabs) => {return tabs[0]})
        .then((tab) => {
          let url = new URL(tab.url);
          if (url.hostname != 'github.com'){
          console.warn('Open in binder only works on GitHub repositories for now.');
          return;
          };
          let parts = url.pathname.split('/');
          if (parts.length < 3){
            console.warn('While you are on GitHub, You do not appear to be in a github repository. Aborting.');
            return;
          }
          let my_binder_url = 'https://mybinder.org/v2/gh/'+parts[1] +'/'+parts[2] +'/master';
          console.info('Opening ' + url + 'using mybinder.org... enjoy !')
          browser.tabs.create({'url':my_binder_url});
        })

      }
      console.info('(Re) loading open-in-binder extension.');
      browser.browserAction.onClicked.addListener(handleClick);

      console.info('❤️ If you are reading this then you know about binder and javascript. ❤️');
      console.info('❤️ So you\'re skilled enough to contribute ! We\'re waiting for you on https://github.com/jupyterhub/ ❤️');
    })()
  
You can find the [original source here](https://github.com/Carreau/open-with-binder-firefox-extension/blob/a46c59199e6e5883ab4985064f6bddba5c6827d2/content_scripts/binderify.js)

![Firefox Dev Logo](img/firefox-dev-logo.png)

The hardest part was finding the API and learning how to package and set the
icons correctly. There are still [plenty of missing
features](https://github.com/Carreau/open-with-binder-firefox-extension/issues)
and [really low hanging
fruits](https://github.com/Carreau/open-with-binder-firefox-extension/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22),
even if you have never written an extension before (hey it's my first and I
averaged 1-useful line/day writing it...).

## General Feeling

Remember that I'm new to that and started a week ago.

The Mozilla docs are good but highly varying in quality, it feels (and is) a
wiki. More opinionated tutorials might have been less confusing. A lot of
statements are correct but not quite, and leaving the choice too users is just
confusing. For example : you can use SVG or PNG icons, which I did, but then
some area don't like SVG (addons.mozilla.org), and the WebExtensions should work
on Chrome, but Chrome requires PNG. Telling me that I could use SVG was not
useful.

The review of addons is blazingly fast (7min from first submissions to Human
approved). Apple could learn from that if what I've heard here and there is
correct..

The submission process has way to many manual steps, I'm ok for first
submission, but updates, really ? I want to be able to fill-in all the
information ahead of time (or generate them) and then have a cli to submit
things. I hate filling forms online.

The first submission even if marked Beta will not be considered beta. So
basically I published a 0.1.0beta1, then 0.1.0beta2 which did not trigger
automatic update because the beta1 was not considered beta. Super confusing. I
could "force" to see the beta3 page but with a warning that beta3 was an older
version than beta1 ? What ? 

There is still this feeling that this last 1% of polishing the process has not
been done (That's usually where Apple is know to shine). For example your store
icon will be resized to 64x64 (px) and display in a 64x64 (px) square but I have
a retina screen ! So even if I submitted a 128x128 now my icon looks blurry !
WTF !

## You can contribute

As I said earlier there is a lot of low hanging fruits ! I went through the
process of figuring things out, so that you can contribute easily:

 - detect if not on /master/ and craft corresponding binder URL
 - Switch Icons to PNGs
 - test/package for Chrome
 - Add options for other binders than MyBinder.org
 - Add Screenshots and descriptions to the Addon Store.

So see you
[there](https://github.com/Carreau/open-with-binder-firefox-extension) !







