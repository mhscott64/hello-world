from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classifier-1')
def classifier_1():
    return render_template('classifier-1.html')


@app.route('/classifier-2')
def classifier_2():
    return render_template('classifier-2.html')

@app.route('/classifier-3')
def classifier_3():
    return render_template('classifier-3.html')    