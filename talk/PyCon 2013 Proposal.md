Crypto 101
==========

Cryptography (and information security in general) is a tricky subject.

There's an infinitude of ways to get it wrong, but there's only a few ways to get it right. Failures are usually silent, and only evident once it's too late.

This talk will touch on basic cryptographic primitives and tools: just enough to know what they do, when and why you'd want it, and just enough to satisfy basic curiosity.

I will also touch on common attack vectors, some of which expose issues they may have never even considered (e.g. timing attacks), or to provide them with a baseline for understanding security news (such as break-in post-mortems). Although technically those things are information security, of which cryptography is only one component, I think they'd fit well in this talk.

(I'm amenable to ideas about changing the talk title because of this, but I feel people coming for infosec might be disappointed by how much crypto they'd get...)

Goals
-----

At the end of this talk, attendees should know how to use the available cryptographic tools to build larger systems that involve cryptography. They should also have some basic understanding of how some common systems compare, and also a sense for detecting and exposing snake oil. Finally, they should have some idea of common ways the security of their programs can become compromised.

People won't leave the room as newly minted cryptographers, but I hope they'll leave a lot less likely to shoot themselves in the foot.

I feel that this talk probably would benefit from a fairly lengthy time allotted for questions.

Target audience
---------------

This talk is aimed at programmers of any skill level that lack crypto chops.

Subjects
--------

- Primitives
    - Encryption
    - Authentication
    - One way functions
- Common attack types
    - Replays
    - Man-in-the-middle
    - Timing attacks
    - Password storage
