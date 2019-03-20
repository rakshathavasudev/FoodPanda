import flask

from flask import Flask, render_template, request
app=flask.Flask(__name__)

@app.route('/foodpanda')
def foodpanda():
	return render_template('one.html')


@app.route('/2nd.html')
def about():
	return render_template('2nd.html')

@app.route('/3rd.html')
def menu():
	return render_template('3rd.html')


@app.route('/one.html')
def back():
	return render_template('one.html')

if __name__=='__main__':
    app.jinja_env.globals.update(chr=chr)
    app.run(host="0.0.0.0",port=8000,debug=True,threaded=True)

