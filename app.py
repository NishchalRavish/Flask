from flask import Flask,render_template

app = Flask(__name__)

# Basic Route
@app.route('/')
def index():
    return render_template('basic.html')

#Dynamic Routes
@app.route('/puppy/<name>')
def puppy(name):
    return "<h1> This is a page for {}</h1>".format(name[100])

if __name__=="__main__":
    app.run(debug=True)