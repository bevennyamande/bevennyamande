---
layout: post
title: Setting Tor website 
---

# Setting the required file

```bash

vim  /etc/tor/torrc
HiddenServiceDir /var/lib/tor/hidden_service/                                                                                                                        
HiddenServicePort 80 127.0.0.1:80

service tor restart

cat /var/lib/tor/hidden_service/hostname




```
