#!/usr/bin/python2.7
from flask import Flask,render_template


app = Flask(__name__)
print __name__
@app.route('/')
def index():
	return render_template('index.html')


@app.route('/user/<user_name>')
def hello(user_name=None):
    return render_template('index.html',user_name=user_name)


@app.route('/post/<int:post_id>')
def post(post_id):
    return "Hello %d" % post_id

if __name__=='__main__':
	app.debug = True
	app.run(host='0.0.0.0')