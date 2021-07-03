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
		ServerName mywebsite.com
		ServerAdmin admin@mywebsite.com
		WSGIScriptAlias / /var/www/FlaskApp/flaskapp.wsgi
		<Directory /var/www/FlaskApp/FlaskApp/>
			Order allow,deny
			Allow from all
		</Directory>
		Alias /static /var/www/FlaskApp/FlaskApp/static
		<Directory /var/www/FlaskApp/FlaskApp/static/>
			Order allow,deny
			Allow from all
		</Directory>
		ErrorLog ${APACHE_LOG_DIR}/error.log
		LogLevel warn
		CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

```bash
a2ensite bountyapp

```
