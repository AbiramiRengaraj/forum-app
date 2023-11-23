# downloaded the flask with the help of pip install flask and then imported flask for the building the forum application

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# testing purpose
posts = [
    {"id": 1, "title": "First Post", "content": "This is the content of the first post.", "comments": []},
    {"id": 2, "title": "Second Post", "content": "This is the content of the second post.", "comments": []},
]

#directed to the url (index.html)
@app.route('/')
def index():
    return render_template('index.html', posts=posts)

#display the content of the post 
@app.route('/post/<int:post_id>')
def post(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
#postid not found means it shows 404 error
    if post:
        return render_template('post.html', post=post)
    return "Post not found", 404

#handles both the get and the post method
@app.route('/new_post', methods=['GET', 'POST'])
#newpost is defined
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_post = {"id": len(posts) + 1, "title": title, "content": content, "comments": []}
        posts.append(new_post)
        return redirect(url_for('index'))
    return render_template('new_post.html')


#update the comments with respect to the postid 
@app.route('/new_comment/<int:post_id>', methods=['POST'])
def new_comment(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    if post:
        comment_text = request.form['comment']
        post['comments'].append(comment_text)
        return redirect(url_for('post', post_id=post_id))
    return "Post not found", 404

#default port=5000(if we need to run in a specific port means #app.run(port=8080))
if __name__ == '__main__':
    app.run
