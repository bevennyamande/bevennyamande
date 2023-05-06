---
layout: post
title: Tryhackme Room - Olympus
---

Room: [Olympus](https://tryhackme.com/room/olympusroom)

# Initial Recon Methodology

```bash
gobuster vhost -u http://olympus.thm/ -w /usr/share/seclists/Discovery/DNS/bug-bounty-program-subdomains-trickest-inventory.txt -t 50 --append-domain

```

root@the-it-department
The old version of the website is still accessible on this domain
