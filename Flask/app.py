from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index( ):
    return "안녕하세요"

@app.route('/chicken')
def html( ):
    return render_template('chicken.html')

# chicken.html을 띄워주세요