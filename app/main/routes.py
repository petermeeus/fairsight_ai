from flask import render_template, Blueprint
from flask_login import login_required

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html', title='Home')

@main.route('/about')
def about():
    return render_template('about.html', title='About')

@main.route('/team')
def team():
    return render_template('team.html', title='Team')

@main.route('/faq')
def faq():
    return render_template('faq.html', title='FAQ')

@main.route('/account')
@login_required
def account():
    return render_template('account_settings.html', title='Account Settings')

@main.route('/market')
def market():
    return render_template('market.html', title='Market & Feasibility')
