<!-- 
.. title: About security
.. slug: 19-about-security
.. date: 2015-09-24 21:33:24 UTC
.. tags: figshare, security, anger, privacy, swearwords
.. category: 
.. link: 
.. description: You are wrong about security.
.. type: text
-->

This is a bit of an anger post, I won't explicitly give name, but if you know
me you should be able to put the pieces together.

I'm angry for the reason that almost a year ago, I warn a known Londonian
startup, that they had a large security flaw in their software. They responded
that they were aware, and are working on a fix. Here we are almost a year
later, the fix is still not implemented, all their user password and credit
card number are potentially in the wild, and they are responding to me and
twitter that basically I don't understand security.

I have a tip for them. If people disagree whether a system is secure or not,
then the system is most likely not secure.


## Do you trust your postman ?

To be more accessible, I'll take the example of Alice and Bob communicating by
snail mail, instead of use the https/ssl encryption jargon.

Alice and Bob have never met, though they are communicating regularly by mail.
Bib is good in French, and Bob is helping her improve her French by improving
her translation. To thanks Bob Alice decide to send him a gift, for now in the
form of money.  As Alice does not trust the postman to not look into the mail
and steel cash, she decide to send a Paper Check. Though this does not prevent
the postman to steel the check, though if Bob account number is written on the
check, the postman will not be able to cash the check.

The solution implemented by above not mentioned company is the following:

Alice send a letter asking Bob for his account number.  Alice receive a
response with an account number.  Alice write a check fro this account and send
it to Bob's bank whose address was with the account number.

According to ANMC (Above Not Mentioned Company) this is secure as Alice does
send a check with Bob bank account number to Bob bank.

So let's see what the postman can do:

The Postman intercept Alice's letter to Bob, asking for his account number.  He
does not even bother sending the main to Bob, and respond to Alice with a
letter impersonating Bob, and having Postman's bank address and Postman's
account number.  Alice send a Paper check to the Postman's Bank without even
realising Bob's was not receiving mail.

So in the end ANMC, your implementation is wrong.  If you login page is on
http, and you tell me that the password is send over https, nothing prevent me
to Man in the middle your login form and have it submitted to a different
address.

## I'm not a clown

This is **basic** security when you care a bit on what you are doing, and
please be aware that people that will take the time to submit you such bug
report, are not clowns and actually take time to explain you these things.
Please respect them instead of raising some funds by venture capitals.

You get a statement on your website that you care about user privacy,
apparently you don't.

## Thanks

As usual, I'm not a good at writing English so I appreciate any Pull Request
that fix grammar, spelling and english expression.


