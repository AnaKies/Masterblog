# Blog

This is a lightweight web application built with Flask that allows users to manage blog posts. Users can create, view, update, delete, and like posts. The data is stored persistently in a local JSON file, simulating a simple database. Each post includes a unique ID (UUID), author name, title, content, and a like counter.

The frontend includes clean styling with a user-friendly layout. When updating a post, the existing data is pre-filled into the form fields for convenience. The app handles edge cases gracefully, such as empty storage or missing posts, and includes a custom 404 error page.

This project demonstrates full-stack CRUD operations using Python, Flask, HTML/CSS, and JSON for storage.

## Installation

To install this project, clone the repository from https://github.com/AnaKies/Masterblog.git
Install the dependencies in requirements.txt using `pip install -r requirements.txt`

## Usage

To use this project, run the following command - `python app.py`.
After launching, the console will display a local IP address (e.g., http://127.0.0.1:5001/). Open this address in your browser to access the web interface.

From there, you can perform standard operations:
- Create a new blog post 
- Read all existing posts 
- Update any post’s content 
- Delete posts 
- Like a post to increase its like counter

All data is stored in a local JSON file (posts.json) and updated in real-time as you interact with the app.

## Contributing

This is a personal educational project created for learning purposes.  
Contributions are not expected, but if you have suggestions or notice any issues, feel free to open an issue or submit a pull request.