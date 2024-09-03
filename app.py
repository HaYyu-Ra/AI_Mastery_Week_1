from flask import Flask, render_template
import streamlit as st

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    exec(open('main.py').read())
    return "Streamlit dashboard running..."

if __name__ == '__main__':
    app.run(debug=True)
