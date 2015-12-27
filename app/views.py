from app import app
from .editsea import editSea
from flask import render_template, flash, redirect
from .forms import EditForm


@app.route('/')

@app.route('/edit', methods=['POST', 'GET'])
def edit():
    loadjson = editSea()
    loadjson.loadJson()
    form = EditForm()
    if form.validate_on_submit():
        flash("Login requested for OpenId: " + form.userlogin.data +
              " remember_me: " + str(form.remember_me.data))
        return redirect('/index')
    flash(str(form.remember_me.data))
    return render_template('edit.html', title='Sighn in', form=form)


