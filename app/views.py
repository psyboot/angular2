from app import app
from flask import render_template, flash, redirect
from .forms import LoginForm, TestMongoForm
from .viborka import CheckViborka
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from config import MONGO_DB_IP,MONGO_DB_PORT


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Nick'}
    posts = [  # Выдуманные посты
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title="Home", user=user, posts=posts)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requested for OpenId: " + form.userlogin.data + 
            " remember_me: " + str(form.remember_me.data))
        return redirect('/index')
    flash(str(form.remember_me.data))
    return render_template('login.html', title='Sighn in', form=form)

@app.route('/vib')
def viborka():
    check = CheckViborka()
    check.check()
    #for key in check.gorod.keys():
    #    out.append(str(check.gorod[key]))
    return render_template('viborka.html', title='Расчет выборки', data=check.data)
    #return str(check.gorod.keys())+str(check.gorod.values())

@app.route('/polls')
def pollslist():
    mongocl = MongoClient(MONGO_DB_IP,MONGO_DB_PORT)
    db = mongocl.vibsettdb
    polls_list = []
    for pl in db.viborki.find():
        polls_list.append(pl["opros"])
    return "<br>".join(polls_list)
    

@app.route('/vibsett', methods=['POST','GET'])
def vibsett():
    form = TestMongoForm()
    mongocl = MongoClient(MONGO_DB_IP,MONGO_DB_PORT)
    db = mongocl.vibsettdb
    if form.validate_on_submit():
        print ("Validate!")
        viborka = {
            "opros": form.opros_id.data, 
            "gorod": {
                "m18":form.gorodm18.data,
                "m30":form.gorodm30.data,
                "m59":form.gorodm59.data,
                "m60":form.gorodm60.data,
                "w18":form.gorodw18.data,
                "w30":form.gorodw30.data,
                "w59":form.gorodw59.data,
                "w60":form.gorodw60.data,
            },
            "rayon": {
                "m18":form.rayonm18.data,
                "m30":form.rayonm30.data,
                "m59":form.rayonm59.data,
                "m60":form.rayonm60.data,
                "w18":form.rayonw18.data,
                "w30":form.rayonw30.data,
                "w59":form.rayonw59.data,
                "w60":form.rayonw60.data,
            },
            "selo": {
                "m18":form.selom18.data,
                "m30":form.selom30.data,
                "m59":form.selom59.data,
                "m60":form.selom60.data,
                "w18":form.selow18.data,
                "w30":form.selow30.data,
                "w59":form.selow59.data,
                "w60":form.selow60.data,
            },
            "code_gorod": form.code_gorod.data,
            "code_rayon": form.code_rayon.data,
            "code_selo": form.code_selo.data,
            "code_woman": form.code_woman.data,
            "code_man": form.code_man.data,
            "code_18": form.code_18.data,
            "code_30": form.code_30.data,
            "code_59": form.code_59.data,
            "code_60": form.code_60.data
        }

        try:
            if db.viborki.find_one({"opros": form.opros_id.data}):
                print(db.viborki.find({"opros": form.opros_id.data}))
                db.viborki.update({"opros": form.opros_id.data},{"$set":viborka})                
                flashmsg = "Опрос " + form.opros_id.data + " существует. Данные обновлены."
            else:
                db.viborki.insert(viborka)
                flashmsg = "Данные по опросу" + form.opros_id.data + " введены."
        except  ConnectionFailure as e:
            flashmsg = "Error " + str(e)
        flash(flashmsg)
        return redirect('/index')
    form_errors = {
        "opros_id": "",
        "gorodm18" : "",
        "gorodm30" : "",
        "gorodm59" : "",
        "gorodm60" : "",
        "gorodw18" : "",
        "gorodw30" : "",
        "gorodw59" : "",
        "gorodw60" : "",
        "rayonm18" : "",
        "rayonm30" : "",
        "rayonm59" : "",
        "rayonm60" : "",
        "rayonw18" : "",
        "rayonw30" : "",
        "rayonw59" : "",
        "rayonw60" : "",
        "selom18" : "",
        "selom30" : "",
        "selom59" : "",
        "selom60" : "",
        "selow18" : "",
        "selow30" : "",
        "selow59" : "",
        "selow60" : "",
        "code_gorod" : "",
        "code_rayon" : "",
        "code_selo" : "",
        "code_man" : "",
        "code_woman" : "",
        "code_18" : "",
        "code_30" : "",
        "code_59" : "",
        "code_60" : "",
    }
    for f in form.errors:
        form_errors[f] = form.errors[f]    
    return render_template('viborka_settings.html', title='Выборка', form=form,form_errors=form_errors)
