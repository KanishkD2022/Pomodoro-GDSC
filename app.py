from os import name
from flask import Flask, render_template, request
import time

app = Flask(__name__)

@app.route('/')
def ht_ml_code():
  return render_template('index.html',)
if __name__=='__main__':
  app.run(host='0.0.0.0', debug=True)
  