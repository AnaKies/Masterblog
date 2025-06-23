from flask import Flask, render_template, request, redirect, url_for
import json_manager.json_handler as json_handler
import random


app = Flask(__name__)

@app.route('/add', methods=['GET', 'POST'])
def add():
    """
    Asks the user to enter details for a new blog post.
    """
    try:
        if request.method == 'POST':
            user_name = request.form['user_name']
            post_title = request.form['post_title']
            post_content = request.form['post_content']
            user_id = random.randint(100000, 999999)
            new_post = {'id': user_id, 'author': user_name, 'title': post_title, 'content': post_content}
            data = json_handler.read_json()
            if not data:
                data = []
            data.append(new_post)
            json_handler.write_json(data)

            return redirect(url_for('index'))
        # case for GET request
        return render_template('add.html')
    except Exception as error:
        print(f"Error adding blog post data: {error}")
        return []



@app.route('/')
def index():
    blog_posts = json_handler.read_json()
    if not blog_posts:
        blog_posts = []
    return render_template('index.html', posts=blog_posts)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)