from flask import request


def get_post_data_from_the_form():
    """
    Retrieves the post details from a HTML form.
    :return: Author, title and content of the post as tuple.
    """
    user_name = request.form.get('user_name')
    post_title = request.form.get('post_title')
    post_content = request.form.get('post_content')

    return user_name, post_title, post_content


def find_post(blog_posts, post_id):
    """
    Finds the post in the storage.
    :param blog_posts: JSON formatted data from the storage.
    :param post_id: ID of the blog post.
    :return: Index of the post in the list of blog_posts.
    """
    for index, post in enumerate(blog_posts):
        if post['id'] == post_id:
            return index

    return f"Warning: post with id {post_id} doesn't exist in the storage.", 404
