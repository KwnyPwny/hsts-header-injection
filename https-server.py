from flask import Flask, request, Response, make_response, render_template
import werkzeug, random

def _validate_value(self, value):
	pass

werkzeug.datastructures.Headers._validate_value = _validate_value

app = Flask(__name__)

@app.route('/')
def index():
	resp = make_response(render_template('index.html', cb=random.randrange(2**32)))
	resp.headers['Strict-Transport-Security'] = 'max-age=31536000'
	resp.set_cookie('secret','this-is-a-secret', httponly=True)
	return resp

@app.route('/vuln')
def vuln():
	param = request.args.get('param')
	resp = Response('<html><head><title>Title</title></head><body>Just some HTML</body></html>')
	resp.headers['X-Vulnerable-Header'] = 'param={}'.format(param)
	resp.headers['Strict-Transport-Security'] = 'max-age=31536000'
	return resp

if __name__ == '__main__':
	app.run(port=443, ssl_context=('certs/hsts.local.crt', 'certs/hsts.local.key'))
