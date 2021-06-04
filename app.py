# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request, redirect
from flask_pymongo import PyMongo


# -- Initialization section --
app = Flask(__name__)

'''events = [
        {"event":"First Day of Classes", "date":"2019-08-21"},
        {"event":"Winter Break", "date":"2019-12-20"},
        {"event":"Finals Begin", "date":"2019-12-01"}
    ]'''

# name of database
app.config['MONGO_DBNAME'] = 'test'

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin:PWSDOZ2WNv14dYUY@cluster0.irm1j.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

mongo = PyMongo(app)

# -- Routes section --
# INDEX

@app.route('/')
@app.route('/index')

def index():
    collection = mongo.db.events
    events = collection.find({}).sort('date', 1)
    return render_template('index.html', events = events)


# CONNECT TO DB, ADD DATA

@app.route('/add')

def add():
    user = mongo.db.users
    user.insert({'name':'Elaine'})
    return 'Added User!'

@app.route('/events/new', methods=['GET', 'POST'])

def new_event():
    if request.method == "GET":
        return render_template('new_event.html')
    else:
        event_name = request.form['event_name']
        event_date = request.form['event_date']
        user_name = request.form['user_name']

        events = mongo.db.events
        events.insert({'event': event_name, 'date': event_date, 'user': user_name})
        return redirect('/')

@app.route('/events')

def events():
    collection = mongo.db.events
    events = collection.find({})

    return render_template('events.html', events = events)