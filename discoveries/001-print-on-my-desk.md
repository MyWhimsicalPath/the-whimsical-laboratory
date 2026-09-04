# Field Note 001 — Print on My Desk

**Found:** 4 September 2026  
**Source:** [eliorpom-cmd/print-on-my-desk](https://github.com/eliorpom-cmd/print-on-my-desk)

## What it is

A web page connected to a physical thermal printer. Someone writes a message, the message is checked and queued, the owner approves it, and it prints on paper in their room.

Its basic path is:

**web page → Cloudflare Worker and database → moderation and approval → physical printer**

## What caught my attention

The project turns an ordinary digital message into a physical event. It is personal, deliberately small-scale, and designed around one object in one room rather than becoming a large platform.

The repository is also written so a non-technical person can set it up with help from a coding assistant. Its documentation treats moderation, rate limits, physical limits, failure, and safety as part of the experience—not as afterthoughts.

## What it connects to

### Desk E-Ink Message Display

My e-ink concept has a closely related structure:

**public form → queue → private approval → internet-connected device → approved message displayed on e-ink**

The important difference is the final experience:

- Thermal printing produces a permanent paper object.
- E-ink produces a quiet, changeable display.
- The printer feels immediate and accumulative.
- The e-ink display feels slow, ambient, and temporary.

This repository may become a useful architectural reference without defining the identity of my project.

### The Owl Postal Empire

The same underlying system could eventually support fictional correspondence:

- a message enters a postal system;
- it waits for review or delivery;
- it travels with deliberate slowness;
- it arrives through a physical or ambient object.

The Owl Postal Empire could provide the world and emotional language; an e-ink device could become one artifact inside that world.

## Question to carry forward

How can one technical pathway—send, wait, approve, deliver—create very different emotional experiences depending on the physical output, pacing, interface, and fictional frame?

## Status

**Keep and revisit.** This is a strong reference for the future e-ink project, but not today's build.
