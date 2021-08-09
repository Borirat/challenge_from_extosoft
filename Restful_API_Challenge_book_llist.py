##8. Restful API Challenge
##  Write a Restful API program to Gets a list of books from an external book publisher’s web
##services and returns the list sorted alphabetically with the recommended books always
##appears first. The should be no duplicated books in the list.

##set FLASK_APP=Name
##flask run

from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/book_list')
def book_list():
    book_list = []
    recommend = requests.get("http://35.186.153.190:1323/books/recommend")
    recommend_json = recommend.json()

    num_book_recommend = len(recommend_json)
    
    for book in recommend_json:
        if(len(book_list)==0):
            book_list.append(book)
        else:
            
            for num_book in range(len(book_list)):
                if(book in book_list):
                    break
                else:
                    if(book['book_name'][0].lower()<book_list[num_book]['book_name'][0].lower()):
                        book_list.insert(num_book,book)
                        break
                    elif(book['book_name'][0].lower()==book_list[num_book]['book_name'][0].lower()):
                        book_list.insert(num_book+1,book)
                        break
                    if(num_book==len(book_list)-1):
                        book_list.append(book)
    from_web = requests.get("http://35.186.153.190:1323/books")
    from_web_json = from_web.json()
    
    for book in from_web_json:
        if(len(book_list)==num_book_recommend):
            book_list.append(book)
        else:
            
            for num_book in range(num_book_recommend,len(book_list)):
                if(book in book_list):
                    break
                else:
                    if(book['book_name'][0].lower()<book_list[num_book]['book_name'][0].lower()):
                        book_list.insert(num_book,book)
                        break
                    elif(book['book_name'][0].lower()==book_list[num_book]['book_name'][0].lower()):
                        book_list.insert(num_book+1,book)
                        break
                    if(num_book==len(book_list)-1):
                        book_list.append(book)
                    
    return "<p>"+json.dumps(book_list)+"</p>"
