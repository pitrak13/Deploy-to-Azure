from flask import Flask, request

app = Flask(__name__)

#@app.route('/')
#def hello():
#	return "Hello World!"

count = -1
@app.route("/")
def get_pongs():
    global count
    count+=1
    return f"<h1>pongs {count}</h1>"



if __name__ == '__main__':
	app.run(host='0.0.0.0', port=7999)
