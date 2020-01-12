from flask import Flask, render_template
app = Flask(__name__)

#mock posts in blog
posts = [
    {
        'author' : 'Kareem Abdelsalam',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'January 10, 2020'
    },
    {
        'author' : 'Kareem Ahmed',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'January 12, 2020'
    },
]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ =='__main__':
    app.run(debug=True)
