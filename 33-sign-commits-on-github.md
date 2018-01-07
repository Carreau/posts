<!-- 
.. title: Sign commits on GitHub
.. slug: 33-sign-commits-on-github.md
.. date: 2018-01-07 13:30 UTC
.. tags: git, github, pgp
.. category: 
.. link: 
.. description: 
.. type: text
-->

# Signing Commit on Tags on GitHub

I've recently set-up [keybase](https://keybase.io/) and integrated my public key
with git to be able to sign commits.

I decided to not automatically sign, as auto-signing would allow any attacker
that takes control of my machine to create signed commit. The git [Merkle
tree](https://en.wikipedia.org/wiki/Merkle_tree) of git still insure repos are
not tampered with, as long as you issue `$ git fsck --full` on a repo or `$ git
config --global transfer.fsckobjects true` once and forget it.

Using `$ git log --show-signatur` you can now check that commits (and tags) are
correctly signed. Be careful though, correct signature does not mean trusted,
and if you have a PGP key set; GitHub will helpfully signed the commit you make
on their platform with **their key**. 

    * commit 5ced6c6936563fea7ba7efccecbc4248d84cfabb (tag: 5.2.1, origin/5.2.x, 5.2.x)
    | gpg: Signature made Tue Jan  2 19:51:17 2018 CET
    | gpg:                using RSA key 99B17F64FD5C94692E9EF8064968B2CC0208DCC8
    | gpg: Good signature from "Matthias Bussonnier <bussonniermatthias@gmail.com>" [ultimate]
    | Author: Matthias Bussonnier <bussonniermatthias@gmail.com>
    | Date:   Tue Jan 2 19:49:34 2018 +0100
    |
    |     Bump version number to 5.2.1 for release
    |
    *   commit 5a28fb0a121c286e35db309fe11b53693969b2d6
    |\  gpg: Signature made Tue Jan  2 13:58:08 2018 CET
    | | gpg:                using RSA key 4AEE18F83AFDEB23
    | | gpg: Good signature from "GitHub (web-flow commit signing) <noreply@github.com>" [unknown]
    | | gpg: WARNING: This key is not certified with a trusted signature!
    | | gpg:          There is no indication that the signature belongs to the owner.
    | | Primary key fingerprint: 5DE3 E050 9C47 EA3C F04A  42D3 4AEE 18F8 3AFD EB23
    | | Merge: 3fd21bc 065a16a
    | | Author: Min RK <benjaminrk@gmail.com>
    | | Date:   Tue Jan 2 13:58:08 2018 +0100
    | |
    | |     Merge pull request #326 from jupyter/auto-backport-of-pr-325
    | |
    | |     Backport PR #325 on branch 5.2.x
    | |
    | * commit 065a16aad2e84d506b36bb2c874a7c287c53c61f (origin/pr/326)
    |/  Author: Min RK <benjaminrk@gmail.com>
    |   Date:   Tue Jan 2 10:57:13 2018 +0100
    |
    |       Backport PR #325: Parenthesize conditional requirement in setup.py

So in the previous block, you can see that `5ced6c6...` have been done **and
signed** by me, while `5a28fb0...` has be allegedly done by Min, _but_ signed by
GitHub.

By default you do not have GitHub Signature locally, so the GitHub Signed
commits can appear as unverified. 

To do so fetch the GitHub Key:


```
$ gpg --keyserver hkp://keys.gnupg.net --recv-keys 4AEE18F83AFDEB23
```

Where `4AEE18F83AFDEB23` is the key you do not have locally. 
And remember Valid Signature, does not mean trusted.

## verifying Tags

Tags can be signed, and need to be checked __independently of commits__ :

    $ git tag --verify 5.2.1
    object 5ced6c6936563fea7ba7efccecbc4248d84cfabb
    type commit
    tag 5.2.1
    tagger Matthias Bussonnier <bussonniermatthias@gmail.com> 1514919438 +0100

    release version 5.2.1
    gpg: Signature made Tue Jan  2 19:57:18 2018 CET
    gpg:                using RSA key 99B17F64FD5C94692E9EF8064968B2CC0208DCC8
    gpg: Good signature from "Matthias Bussonnier <bussonniermatthias@gmail.com>" [ultimate]

So you can check that _I_ tagged this commit.

## learn more

As usual the [git documentation](https://git-scm.com/book/id/v2/Git-Tools-Signing-Your-Work)
has more to say about this. And signing is not really useful without checking
the integrity of Git history, so please set `$ git config --global transfer.fsckobjects true` as well !

