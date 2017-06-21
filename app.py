import tornado.ioloop
import tornado.web
import tornado.wsgi
import json

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Flask'


@app.route('/data')
def hello_world():
	data = [
		{ name:"edu", age:25 },
		{ name:"jobs", age: 56}
	]
    return json.dumps(data)
###########################################################


tr = tornado.wsgi.WSGIContainer(app)

application = tornado.web.Application([
	(r".*", FallbackHandler, dict(fallback=tr)),
])

wsgi_app  = tornado.wsgi.WSGIAdapter(application)