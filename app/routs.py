from flask import render_template, flash, redirect, url_for, request, abort
from flask_login import login_user, current_user, logout_user, login_required
from app import app, db
from app.models import User, Book, Movie, Series
from app.forms import LoginForm, MovieForm, SeriesForm, BookForm, RegistrationForm


@app.route('/', methods=['GET', 'POST'])
def Login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
    return render_template('login.html', form=form)


@app.route('/home')
@login_required
def home():
    movies = Movie.query.filter_by(user_id=current_user.id).all()
    series = Series.query.filter_by(user_id=current_user.id).all()
    books = Book.query.filter_by(user_id=current_user.id).all()

    return render_template('home.html', movies=movies, series=series, books=books)


@app.route('/movie_form', methods=['GET', 'POST'])
@login_required
def addMovie():
    form = MovieForm()
    if form.validate_on_submit():
        movie = Movie(title=form.title.data, link=form.link.data, watched=form.watched.data, anime=form.anime.data, dubbed=form.dubbed.data,
                      user_id=current_user.id)
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('movie_form.html', form=form)


@app.route('/series_form', methods=['GET', 'POST'])
@login_required
def addSeries():
    form = SeriesForm()
    if form.validate_on_submit():
        series = Series(title=form.title.data, link=form.link.data, watching=form.watching.data, anime=form.anime.data, dubbed=form.dubbed.data,
                        user_id=current_user.id)
        db.session.add(series)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('series_form.html', form=form)


@app.route('/book_form', methods=['GET', 'POST'])
@login_required
def addBook():
    form = BookForm()
    if form.validate_on_submit():
        book = Book(title=form.title.data, writer=form.writer.data, link=form.link.data, pages=form.pages.data, finished=form.finished.data,
                    user_id=current_user.id)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('book_form.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def Register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('Login'))
    return render_template('registration.html', form=form)


@app.route('/logout')
def Logout():
    logout_user()
    return redirect(url_for('Login'))


@app.route("/delete_series/<int:s_id>", methods=['POST'], endpoint='delSeries')
@login_required
def delSeries(s_id):
    series = Series.query.get_or_404(s_id)
    if series.author != current_user:
        abort(403)
    db.session.delete(series)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/delete_book/<int:b_id>", methods=['POST'], endpoint='delBook')
@login_required
def delBook(b_id):
    book = Book.query.get_or_404(b_id)
    if book.author != current_user:
        abort(403)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/delete_movie/<int:m_id>", methods=['POST'], endpoint='delMovie')
@login_required
def delMovie(m_id):
    movie = Movie.query.get_or_404(m_id)
    if movie.author != current_user:
        abort(403)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))
