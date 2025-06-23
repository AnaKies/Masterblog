import uuid

from flask import Flask, render_template, request, redirect, url_for

import helpers.helper as helper
import json_manager.json_handler as json_handler

app = Flask(__name__)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """
    Asks the user to enter details for a new blog post.
    """
    try:
        if request.method == 'POST':
            user_name, post_title, post_content = helper.get_post_data_from_the_form()
            user_id = str(uuid.uuid4())

            new_post = {'id': user_id,
                        'author': user_name,
                        'title': post_title,
                        'content': post_content,
                        'likes': 0}

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
            return 'Nothing to delete', 404

        post_index = helper.find_post(blog_posts, post_id)
        blog_posts.pop(post_index)
        json_handler.write_json(blog_posts)

        #return render_template('index.html', posts=blog_posts)
        return redirect(url_for('index'))

    except Exception as error:
        print(f"Error deleting blog post data: {error}")
        return []


@app.route('/update/<string:post_id>', methods=['GET', 'POST'])
def update(post_id):
    """
    Updates a blog post by UUID.
    """
    try:
        blog_posts = json_handler.read_json()

        if not blog_posts:
            return 'Nothing to update', 404

        post_index = helper.find_post(blog_posts, post_id)
        post_to_update = blog_posts[post_index]

        if request.method == 'POST':
            (user_name,
             post_title,
             post_content) = helper.get_post_data_from_the_form()

            blog_posts[post_index]['author'] = user_name
            blog_posts[post_index]['title'] = post_title
            blog_posts[post_index]['content'] = post_content

            json_handler.write_json(blog_posts)

            return redirect(url_for('index'))
        return render_template('update.html', post=post_to_update)

    except Exception as error:
        print(f"Error updating blog post data: {error}")
        return []


@app.route('/like/<string:post_id>')
def like(post_id):
    """
    Likes a blog post by UUID.
    """
    try:
        blog_posts = json_handler.read_json()

        if not blog_posts:
            return 'Nothing to update', 404

        post_index = helper.find_post(blog_posts, post_id)
        blog_posts[post_index]['likes'] += 1
        json_handler.write_json(blog_posts)

        return redirect(url_for('index'))

    except Exception as error:
        print(f"Error updating blog post data: {error}")
        return []


@app.route('/')
def index():
    """
    Main page, that shows all the blog posts.
    """
    blog_posts = json_handler.read_json()

    if not blog_posts:
        blog_posts = []

    return render_template('index.html', posts=blog_posts)


@app.errorhandler(404)
def page_not_found(error):
    """
    Displays a 404 error page with an explanation of the error.
    """
    return render_template('404.html', error_message=str(error)), 404


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
