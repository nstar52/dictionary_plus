from app import app, db
from flask import jsonify, request
import time
from app.models import Word

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

@app.route("/", methods=['GET'])
def home():
    print(f"The secret key is {app.config['SECRET_KEY']}")
    return "Hello World! I am using Flask."


@app.route("/api/add", methods=['GET', 'POST'])
def add_a_word():
    name = request.args.get('name')
    translation = request.args.get('summary')
    w = Word(name=name, meaning=translation)
    db.session.add(w)
    db.session.commit()
    return {'time': time.time()}


@app.route("/api/remove", methods=['GET', 'POST'])
def remove_a_word():
    name = request.args.get('name')
    a_word = Word.query.filter_by(name=name).first_or_404()
    db.session.delete(a_word)
    db.session.commit()
    return {'time': time.time()}

# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    response = jsonify(books)
    # response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    # x = "some data you want to return"
    # return x, 200, {'Content-Type': 'text/css; charset=utf-8'}