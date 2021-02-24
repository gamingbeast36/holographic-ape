from flask import Flask, render_template, url_for, request, make_response
from functools import wraps, update_wrapper
from datetime import datetime



app = Flask(__name__)

def nocache(view):
    @wraps(view)
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers['Last-Modified'] = datetime.now()
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response
        
    return update_wrapper(no_cache, view)


@app.route("/")
def index():
    return render_template("index.html") 


@app.route("/articles/")
def articles():
    return render_template("articles.html") 


if __name__ == "__main__":
    app.run(debug=True)

