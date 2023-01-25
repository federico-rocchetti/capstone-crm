from project import app, db, connect_to_db
from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_user, login_required, logout_user
from project.models import User, Contact, Note
from project.forms import LoginForm, RegistrationForm, AddContact

@app.route('/')
def home():
    return render_template('/home.html')

@app.route("/login", methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash("Logged in Succesfully.")

            next = request.args.get("next")

            if next == None or not next[0]=="/":
                next = url_for('dashboard')
            
            return redirect(next)

    return render_template('login.html', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Registered Successfully.")
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out successfully")
    return redirect(url_for('home'))

@app.route('/dashboard')
@login_required
def dashboard():

    contacts = Contact.query.all()

    return render_template('/dashboard.html', contacts=contacts)

@app.route('/add_contact', methods=['GET', 'POST'])
@login_required
def add_contact():

    form = AddContact()
    if form.validate_on_submit():
        contact = Contact(user_id=form.user_id.data, name=form.name.data, contact_type=form.contact_type.data, email=form.email.data,
                        mobile_phone=form.mobile_phone.data, work_phone=form.work_phone.data, address=form.address.data,
                        company=form.company.data)
        db.session.add(contact)
        db.session.commit()
        flash("Contact Added.")
        return redirect(url_for('add_contact'))
    return render_template('/add_contact.html', form=form)

@app.route('/contact/<contact_id>')
@login_required
def contact(contact_id):
    contact = Contact.query.get(contact_id)
    return render_template('contact.html', contact=contact)

if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True)