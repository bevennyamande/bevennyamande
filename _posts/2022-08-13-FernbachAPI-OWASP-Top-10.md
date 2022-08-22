---
layout: post
title: OSWAP Top Ten on FernbachAPI Lab
author: Beven Nyamande 
---

# Directory bruteforcing with Ffuf

```bash

status                  [Status: 200, Size: 91, Words: 15, Lines: 5]
console                 [Status: 200, Size: 1909, Words: 405, Lines: 52]
```
- Let me find some more endpoints using seclists `api wordlist`

```bash

/api/v1/user            [Status: 401, Size: 37, Words: 6, Lines: 4]

```

- seems we have found an `api endpoint`. I will throw in another wordlist
- visiting the endpoint `http://127.0.0.1:5000/api/v1/user` i see i need to provide a token
- what aabout `v2` just thing let me check it - well not found, let me continue 