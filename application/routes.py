from application import app, db, forms
from application.models import Users
from flask import Flask, render_template, request, redirect,url_for

@app.route('/')
def home():
    users=Users.query.all()
    return render_template('home.html', users=users)

@app.route('/add',methods=['GET', 'POST'])
def add():
    form=forms.AddUserForm()
    if request.method=='POST':
        first_name=form.first_name.data
        last_name=form.last_name.data
        email_address=form.email_address.data
        if len(first_name) == 0 or len(last_name) == 0 or len(email_address) == 0:
            error = "Please supply both first, last name and email"
        else:
            user_to_add=Users(first_name= form.first_name.data, last_name=form.last_name.data, email_address=form.email_address.data)
            db.session.add(user_to_add)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('adduserform.html',form=form)

@app.route('/update/<int:id>', methods=['GET','PUT'])
def update(id):
    error=""
    form=forms.UpdateUserForm()
    user_to_update=Users.query.filter_by(id=id).first()
    form.first_name.data=user_to_update.first_name
    form.last_name.data=user_to_update.last_name
    form.email_address.data=user_to_update.email_address
    if request.method=='PUT':
        first_name=form.first_name.data
        last_name=form.last_name.data
        email_address=form.email_address.data
        if len(first_name) == 0 or len(last_name) == 0 or len(email_address) == 0:
            error = "Please supply both first, last name and email"
            return redirect(url_for('update', id=id))
        else:
            user_to_update.first_name=first_name
            user_to_update.last_name=last_name
            user_to_update.email_address=email_address
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('updateuserform.html',form=form,message=error)


@app.route('/delete/<int:id>')
def delete(id):
    user_to_delete=Users.query.filter_by(id=id).first()
    db.session.delete(user_to_delete)
    db.session.commit()
    return redirect(url_for('home'), message="User has been deleted.")