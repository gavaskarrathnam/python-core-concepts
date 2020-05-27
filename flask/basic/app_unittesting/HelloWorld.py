from flask import Flask, jsonify, request
#
app = Flask(__name__)

books = [{'name':'Python'}, {'name': 'Flask'}, {'name': 'docker'}, {'name':'Kubernetes'}, {'name':'redis'}]

@app.route('/') #decorator
def index(): #view function under the decorator
    return '<h1>Hello Flask World...Its working...</h1>'

@app.route('/book', methods=['GET'])
def getAllBooks():
    return jsonify({'books':books})

@app.route('/book/<string:name>', methods=['GET'])
def getBook(name):
    book = [book for book in books if book['name'].upper() == name.upper()]
    return jsonify({'book': book[0]})

@app.route('/book', methods=['POST'])
def addBook():
    book = {'name':request.json['name']}
    books.append(book)
    return jsonify({'books':books})

@app.route('/book/<string:name>', methods=['PUT'])
def updateBook(name):
    book = [book for book in books if book['name'] == name]
    book[0]['name'] = request.json['name']
    return jsonify({'book':book[0]})

@app.route('/book/<string:name>', methods=['DELETE'])
def deleteBook(name):
    book = [book for book in books if book['name'] == name]

    books.remove(book[0])
    return jsonify({'books':books})

# Below line meaning, i am going to call/run directly - means >python HelloWorld.py
if __name__ == '__main__':
    app.run(debug=True)