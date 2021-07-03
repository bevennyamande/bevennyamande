---
layout: post
title: Setting Flask App to run on Apache2 
---

# Installing the required libraries

```bash

apt install libapache2-mod-wsgi-py3
a2enmod wsgi

# change directory to the folder hosting the application

cd /var/www
vim /etc/apache2/sites-available/THE_FLASK_APP.conf


```
<VirtualHost *:80>
         ServerName x.x.x.x
         # DocumentRoot /var/www/mysite

         # ServerAdmin admin@mywebsite.com
         WSGIScriptAlias / /var/www/mysite/mysite.wsgi
         WSGIDaemonProcess mysite user=www-data group=www-data threads=6 display-name=%{GROUP} processes=5
         WSGIScriptReloading On
         WSGIProcessGroup mysite
         WSGIApplicationGroup %{GLOBAL}
         ErrorLog ${APACHE_LOG_DIR}/error-mysite.log
         LogLevel debug
         CustomLog ${APACHE_LOG_DIR}/access-mysite.log combined
         Timeout 600

         <Directory /var/www/mysite/mysite/>
         <IfVersion >= 2.4>
             Require all granted
         </IfVersion>
         <IfVersion < 2.4>
             Order allow,deny
             Allow from all
         </IfVersion>
         </Directory>

 </VirtualHost>

```bash
a2ensite mysite
chown -R www-data: /var/www/mysite/staticfiles
```
