from project import app, db, connect_to_db
from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_user, login_required, logout_user, current_user
from project.models import User, Contact, Note
from project.forms import LoginForm, RegistrationForm, AddContact, AddNote, get_note_form

@app.route('/')
def home():
    return render_template('/home.html')

@app.route("/login", methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is not None and user.check_password(form.password.data) :
            login_user(user)
            flash("Logged in Succesfully.")

            next = request.args.get("next")

            if next == None or not next[0]=="/":
                next = url_for('dashboard')
            
            return redirect(next)
        else:
            flash('Invalid username or password.')
    return render_template('login.html', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            user = User(username=form.username.data, password=form.password.data)
            db.session.add(user)
            db.session.commit()
            flash("Registered Successfully.")
            return redirect(url_for('login'))
        else:
            flash("Username already in use.")
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

    contacts = Contact.query.filter_by(user_id=current_user.id)

    return render_template('/dashboard.html', contacts=contacts)

@app.route('/add_contact', methods=['GET', 'POST'])
@login_required
def add_contact():

    form = AddContact()
    if form.validate_on_submit():
        contact = Contact(user_id=current_user.id, 
                            name=form.name.data, 
                            contact_type=form.contact_type.data, 
                            email=form.email.data,
                            mobile_phone=form.mobile_phone.data, 
                            work_phone=form.work_phone.data, 
                            address=form.address.data,
                            company=form.company.data) 
        db.session.add(contact)
        db.session.commit()
        flash("Contact Added.")
        return redirect(url_for('add_contact'))
    return render_template('/add_contact.html', form=form)

@app.route('/contact/<contact_id>', methods=['GET', 'POST'])
@login_required
def contact(contact_id):
    contact = Contact.query.get(contact_id)
    notes = Note.query.filter_by(contact_id=contact_id)

    form = AddNote()
    if form.validate_on_submit():
        note = Note(contact_id=contact_id,
                        note=form.note.data)
        db.session.add(note)
        db.session.commit()
        flash('Note added to contact.')
        return redirect(url_for('contact', contact_id=contact_id, form=form, contact=contact, notes=notes))
    return render_template('contact.html', contact=contact, form=form, notes=notes)

@app.route('/update_contact/<contact_id>', methods=['GET', 'POST'])
@login_required
def update_contact(contact_id):
    form = AddContact()
    contact_to_update = Contact.query.get(contact_id)
    if form.validate_on_submit():
        contact_to_update.name = form.name.data
        contact_to_update.contact_type = form.contact_type.data
        contact_to_update.email = form.email.data
        contact_to_update.mobile_phone = form.mobile_phone.data
        contact_to_update.work_phone = form.work_phone.data
        contact_to_update.address = form.address.data
        contact_to_update.company = form.company.data

        db.session.commit()
        flash('Contact updated.')
        return redirect(url_for('contact', contact_id=contact_id))
    return render_template("update_contact.html", contact_to_update=contact_to_update, form=form)

@app.route('/delete_contact/<contact_id>')
@login_required
def delete_contact(contact_id):
    contact_to_delete = Contact.query.get(contact_id)
    db.session.delete(contact_to_delete)
    db.session.commit()
    flash('Contact Deleted')
    return redirect(url_for('dashboard'))

@app.route('/delete_note/<contact_id>/<note_id>')
@login_required
def delete_note(contact_id, note_id):
    note_to_delete = Note.query.get(note_id)
    db.session.delete(note_to_delete)
    db.session.commit()
    flash('Note deleted.')
    return redirect(url_for('contact', contact_id=contact_id))

@app.route('/edit_note/<contact_id>/<note_id>', methods=['GET', 'POST'])
@login_required
def edit_note(contact_id, note_id):

    note_to_update = Note.query.filter_by(id=note_id).first()
    form = get_note_form(note_to_update.note)
    if form.validate_on_submit():
        note_to_update.note = form.note.data

        db.session.commit()

        flash("Note edited.")
        return redirect(url_for('contact', contact_id=contact_id))
    return render_template("edit_note.html", contact_id=contact_id, 
                            note_to_update=note_to_update, form=form)

if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True)