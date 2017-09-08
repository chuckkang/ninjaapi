from flask import Flask, render_template, request, redirect, session
from flask import jsonify

app = Flask(__name__)
app.secret_key = "thisisasecret"

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/ninja/')
def tmnt():
  return render_template("tmnt.html", color='home')

@app.route('/ninja/<color>')
def tmnt_color(color):
      return render_template("tmnt.html", username)

@app.route('/get_current_user/<color>', methods=['GET'])
def get_current_user(color):
    if (color=='red'):
        name='raphael'
    elif (color=='blue'):
        name='donatello'
    elif (color=='orange'):
        name='leonardo'
    elif (color=='purple'):
        name='michelangelo'
    else: 
        name='notapril'

    return jsonify(color=color, name=name)
      
      
app.run(debug=True) # run our server