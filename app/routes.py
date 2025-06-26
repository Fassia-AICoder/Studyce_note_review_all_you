from flask import Blueprint,render_template


plan = Blueprint("blue",__name__)

@plan.route('/')
def home():
    return render_template('base.html')