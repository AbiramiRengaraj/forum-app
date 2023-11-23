# downloaded the flask with the help of pip install flask and then imported flask for building the forum forum_application

from flask import Flask, render_template, request, redirect, url_for

forum_app = Flask(__name__)

# testing purpose
posts = [
    {"id": 1, "title": "Post", "content": "content of the post", "comments": []},
    
]

# directed to the url (index.html)
@forum_app.route('/')
def index():
    return render_template('index.html', posts=posts)

# display the content of the post 
@forum_app.route('/post/<int:post_id>')
def post(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    # postid not found means it shows 404 error
    if post:
        return render_template('post.html', post=post)
    return "Post not found", 404

# handles both the get and the post method
@forum_app.route('/new_post', methods=['GET', 'POST'])
# newpost is defined
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_post = {"id": len(posts) + 1, "title": title, "content": content, "comments": []}
        posts.append(new_post)
        return redirect(url_for('index'))
    return render_template('new_post.html')


# update the comments with respect to the postid 
@forum_app.route('/new_comment/<int:post_id>', methods=['POST'])
def new_comment(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    if post:
        comment_text = request.form['comment']
        post['comments'].append(comment_text)
        return redirect(url_for('post', post_id=post_id))
    return "Post not found", 404










# default port=5000(if we need to run in a specific port means #forum_app.run(port=8080))
if __name__ == '__main__':
    forum_app.run(debug=True)

