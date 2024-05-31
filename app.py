from flask import Flask

app = Flask(__name__)

# Basic Route
@app.route('/')
def index():
    return "<h1> Hello there</h1>"

#Dynamic Routes
@app.route('/puppy/<name>')
def puppy(name):
    return "<h1> This is a page for {}</h1>".format(name[100])

if __name__=="__main__":
    app.run(debug=True)