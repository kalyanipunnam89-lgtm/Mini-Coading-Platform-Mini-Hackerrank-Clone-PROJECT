from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/question')
def question():
    return render_template('question.html')

app.run(debug=True)