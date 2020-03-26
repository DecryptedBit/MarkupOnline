from flask import current_app, Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, logout_user, current_user, login_user
from sqlalchemy.exc import IntegrityError
from mark_one import db, login_manager
from mark_one.models import User
from mark_one.forms import LoginForm, RegistrationForm

# auth = Blueprint('auth', __name__, url_prefix='/auth')
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    """User login page."""
    if not current_user.is_authenticated:
        form = LoginForm()
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            user = db.session.query(User).filter_by(username=username.strip()).first()
            if user and user.check_password(password):
                user.authenticated = True
                db.session.commit()

                login_user(user)

                return redirect(url_for('editor.index'))
            else:
                flash('wrong / misspelled credentials', 'error')
        return render_template('auth/login.html', form=form)
    else:
        return redirect(url_for('editor.index'))

@auth.route('/logout')
@login_required
def logout():
	user = current_user
	user.authenticated = False
	db.session.commit()
	logout_user()
	return redirect(url_for('main.index'))

@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        try:
            user = User(
                username=reg_form.username.data,
                password=reg_form.password.data,
                email=reg_form.email.data
            )

            db.session.add(user)
            db.session.commit()
            
            return redirect(url_for('auth.login'))

        except IntegrityError:
            db.session.rollback()
            flash('ERROR - Email and/or username might already exist!', 'error')

    return render_template('auth/signup.html', form=reg_form)
