from geekio import app

@app.route('/')
def index():
    return 'Hello Geek!'
