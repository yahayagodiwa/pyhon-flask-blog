from flask import Flask, render_template, request
import requests
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

posts = requests.get("https://api.npoint.io/3dc7299f222a3678ec7c").json()


app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)

@app.route('/post/<int:index>')
def single_post(index):
    target_post = next((post for post in posts if post['id'] == index), None)   
    if target_post == None:
        return "Not found" 
    return render_template('post.html', post=target_post)

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        data = request.form
        message = "Successfully sent message"
        return render_template('contact.html', message=message)
    else:
        return render_template('contact.html', )

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True, port=5001)
