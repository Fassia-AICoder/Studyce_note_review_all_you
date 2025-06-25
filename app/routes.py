from flask import Blueprint


plan = Blueprint("blue",__name__)

@plan.route('/')
def home():
    return 'this is my first website'