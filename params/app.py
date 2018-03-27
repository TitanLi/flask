from flask import Flask
app = Flask(__name__)

# string    accepts any text without a slash (the default)
# int       accepts integers
# float     like int but for floating point values
# path      like the default but also accepts slashes
# any       matches one of the items provided
# uuid      accepts UUID strings

@app.route("/user/<username>")
def index(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
