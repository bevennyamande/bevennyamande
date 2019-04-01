---
layout: post
title:  "Getting started with Flask!"
date:   2019-04-01 23:16:50 +0200
categories: jekyll update
---

## The development environment
* Flask
* Flask-SQLAlchemy for ORM and databases

Flask is a simple web framework to learn and get started bringing projects to life
Flask documentation can be found [here](http://flask.pocoo.org/). It has become one 
of my favourite framework to develop in

### Installing the libraries
* pipenv install flask
* pipenv install flask-sqlalchemy

### Hello, world

like its traditional to introduce people to learning languages
by printing 'Hello, world'. Let us make a web application and return the
value 'hello world'

{% highlight python %}
from flask import Flask

# instatiatiation
app = Flask(__name__)

app.config({
	'DEBUG': True
})


@app.route('/')
def index():
    return ' Hello World'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

{% endhighlight %}

we now have a python flask web application, yay !
Jump to your terminal and run the application
save the file as app.py

python3 app.py
