---
layout: post
title: Bug Bounty Tips
---

Bug Bounty Tips

# Collect all js files and check if they resolve

```bash
echo "domain.com" | gau | grep '\.js$' | httpx -status-code -mc 200 -content-type | grep 'application/javascript'

```
