from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/BestSteelerplayers')
def bestpit():
    return render_template('steelers.html')

@app.route('/BestPackerplayers')
def bestgb():
    return render_template('packers.html')

@app.route('/BestBrownplayers')
def bestcle():
    return render_template('browns.html')

@app.route('/BestSeahawkplayers')
def bestsea():
    return render_template('seahawks.html')

@app.route('/BestChiefplayers')
def bestkc():
    return render_template('chiefs.html')



