from flask import Flask, render_template, request, redirect, url_for
import json_manager.json_handler as json_handler
import uuid


app = Flask(__name__)

@app.route('/add', methods=['GET', 'POST'])
def add():
    """
    Asks the user to enter details for a new blog post.
    """
    try:
        if request.method == 'POST':
            user_name = request.form.get('user_name')
            post_title = request.form.get('post_title')
            post_content = request.form.get('post_content')
            user_id = str(uuid.uuid4())
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


@app.route('/delete/<string:post_id>')
def delete(post_id):
    """
    Deletes a blog post by UUID.
    """
    try:
        blog_posts = json_handler.read_json()

        if not blog_posts:
            raise Exception('Nothing to delete')

        post_found = False

        for i, post in enumerate(blog_posts):
            if post['id'] == post_id:
                blog_posts.pop(i)
                post_found = True
                break

        if not post_found:
            print(f"Warning: post with id {post_id} doesn't exist in the storage.")

        json_handler.write_json(blog_posts)

        return render_template('index.html', posts=blog_posts)
    except Exception as error:
        print(f"Error deleting blog post data: {error}")
        return []


@app.route('/update/<string:post_id>', methods=['GET', 'POST'])
def update(post_id):
    try:
        blog_posts = json_handler.read_json()

        if not blog_posts:
            raise Exception('Nothing to update')

        post_to_update = None
        for post in blog_posts:
            if post.get('id') == post_id:
                post_to_update = post
                break;

        if not post_to_update:
            print(f"Warning: post with id {post_id} doesn't exist in the storage.")

        if request.method == 'POST':
            pass
            return redirect(url_for('index'))
        return render_template('update.html', post=post_to_update)
    except Exception as error:
        print(f"Error updating blog post data: {error}")
        return []


@app.route('/')
def index():
    blog_posts = json_handler.read_json()
    if not blog_posts:
        blog_posts = []
    return render_template('index.html', posts=blog_posts)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)