---
layout: post
title: Tryhackme Room - Takeover
---

Room: [Takeover](https://tryhackme.com/room/takeover)

# Initial Recon Methodology

- Run `FFuf`

```bash
gobuster vhost -u futurevera.thm -w /usr/share/wordlists/seclists/Discovery/DNS/bitquark-subdomains-top100000.txt --append-domain

```
