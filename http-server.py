from flask import Flask, redirect

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return redirect('https://hsts.local/', code=301)

if __name__ == '__main__':
	app.run(port=80)