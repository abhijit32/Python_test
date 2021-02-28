from flask import Flask , render_template


app = Flask(__name__)

posts = {
    0: {'title':'Hello world', 'content': 'this is a test post'}
}

@app.route('/')
def home():
    return 'hello world'

@app.route('/post/<int:post_id>')
def post(post_id):
    post = posts[post_id]
    return render_template('test.html',post=post)
    


if __name__ == '__main__':
    app.run(debug=True)