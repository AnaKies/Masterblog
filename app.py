from flask import Flask, render_template, request
import json


app = Flask(__name__)


def read_json():
    """
    Retrieves the blog posts data from the JSON storage.
    """
    try:
        with open('storage/posts.json') as json_file:
            json_data = json.load(json_file)
        return json_data
    except Exception as error:
        print(f"Error getting JSON data: {error}")
        return {}


@app.route('/add', methods=['GET', 'POST'])
def add():
    """
    Asks the user to enter details for a new blog post.
    """
    if request.method == 'POST':
        user_name = request.form['user_name']
        post_title = request.form['post_title']
        post_content = request.form['post_content']
        return render_template('add.html', data_submited=True,
                               user_name=user_name,
                               post_title=post_title,
                               post_content=post_content)
    # case for GET request
    return render_template('add.html', data_submited=False)



@app.route('/')
def index():
    blog_posts = read_json()
    return render_template('index.html', posts=blog_posts)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)