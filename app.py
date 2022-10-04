from dbhelpers import conn_exe_close
from flask import Flask
import json

app = Flask(__name__)

@app.get('/api/books')
def books_author_title():
    result = conn_exe_close('call books_author_title()',[])
    result_json = json.dumps(result,default=str)
    return result_json

@app.get('/api/books_authored')
def count_books_author():
    result = conn_exe_close('call count_books_author()',[])
    result_json = json.dumps(result,default=str)
    return result_json


@app.get('/api/best_selling_book')
def most_sold_book():
    result = conn_exe_close('call most_sold_book()',[])
    result_json = json.dumps(result,default=str)
    return result_json


@app.get('/api/best_selling_author')
def order_authors_sale():
    result = conn_exe_close('call order_authors_sale()',[])
    result_json = json.dumps(result,default=str)
    return result_json


app.run(debug=True)