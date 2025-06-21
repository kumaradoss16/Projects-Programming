import os
import secrets
from PIL import Image
from flask import Blueprint, render_template, url_for, flash, redirect, request, abort
from flaskblog import db, bcrypt, mail
from flaskblog.forms import (RegistrationForm, LoginForm, UpdateAccountForm, PostForm, ResetPasswordForm,
                             RequestResetForm)
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message

main_routes = Blueprint('main_routes', __name__)


# @app.routes("/")
# @app.routes("login", methods=['GET', 'POST'])
@main_routes.route("/")
@main_routes.route("/home")
def home():
    # (8) Create, Update and Delete Posts
    # posts = Post.query.all()
    # (9) Pagination
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    # (9) Pagination
    return render_template('home.html', posts=posts)


@main_routes.route("/about")
def about():
    return render_template('about.html', title='About')


@main_routes.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main_routes.home"))
    form = RegistrationForm()
    # db.create_all()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created! You are now able to log in", 'success')
        return redirect(url_for('main_routes.login'))
    return render_template('register.html', title='Register', form=form)


@main_routes.route("/login", methods=['GET', 'POST'])
# @app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main_routes.home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("main_routes.home"))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@main_routes.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main_routes.home"))


# (7) User Account and User Picture
def save_picture(form_picture):
    # Generate a random hex string (16 characters) using the secrets module
    random_hex = secrets.token_hex(8)
    # Split the filename and extension of the uploaded picture
    _, f_ext = os.path.splitext(form_picture.filename)
    # Concatenate the random hex string and the file extension to create a unique filename
    picture_fn = random_hex + f_ext
    # Define the path where the picture will be saved
    # os.path.join() joins paths with the appropriate separator for the operating system
    picture_path = os.path.join(main_routes.root_path, 'static/profile_pics', picture_fn)
    # Define the desired output size for the image
    output_size = (125, 125)
    # Open the uploaded image using the Image module from the Python Imaging Library (PIL)
    i = Image.open(form_picture)
    # Resize the image to fit within the specified output size while preserving aspect ratio
    i.thumbnail(output_size)
    # Save the resized image to the specified picture path
    i.save(picture_path)
    # Return the filename of the saved picture
    return picture_fn


# (7) User Account and User Picture
@main_routes.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    # Create an instance of the UpdateAccountForm
    form = UpdateAccountForm()
    # Check if the form has been submitted and is valid
    if form.validate_on_submit():
        # Check if a new profile picture has been uploaded
        if form.picture.data:
            # Save the uploaded picture and get the filename
            picture_file = save_picture(form.picture.data)
            # Update the current user's image file with the new filename
            current_user.image_file = picture_file
        # Update the current user's username and email with the form data
        current_user.username = form.username.data
        current_user.email = form.email.data
        # Commit changes to the database
        db.session.commit()
        # Flash a success message to the user
        flash("Your account has been updated!", "success")
        # Redirect the user to the account page to prevent form resubmission on refresh
        return redirect(url_for("main_routes.account"))
    # If the request method is GET (initial page load or validation failure)
    elif request.method == "GET":
        # Populate the form fields with the current user's data
        form.username.data = current_user.username
        form.email.data = current_user.email
    # Generate the URL for the current user's profile picture
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    # Render the account.html template with the form and image_file variables
    return render_template('account.html', title='Account', image_file=image_file, form=form)


# (8) Create, Update and Delete Posts
@main_routes.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        posts = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(posts)
        db.session.commit()
        flash("Your post has been created!", "success")
        return redirect(url_for("main_routes.home"))
    return render_template('create_post.html', title='New Post', form=form, legend='New Post')


@main_routes.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("post.html", title=post.title, post=post)


@main_routes.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash("Your post has been Updated!", "success")
        return redirect(url_for("main_routes.post", post_id=post.id))
    elif request.method == "GET":
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')


@main_routes.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash("Your post has been Deleted!", "success")
    return redirect(url_for('main_routes.home'))


# (9) Pagination
@main_routes.route("/user/<string:username>")
def user_post(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return render_template('user_post.html', posts=posts, user=user)


# (10) Email and Password Reset
def send_reset_email(user):
    token = user.get_reset_token()
    print(token)
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('main_routes.reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)


@main_routes.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main_routes.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('main_routes.login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


@main_routes.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main_routes.home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('main_routes.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('main_routes.login'))
    return render_template('reset_token.html', title='Reset Password', form=form)




