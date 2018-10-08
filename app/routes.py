# coding=utf-8
from flask import redirect, render_template, url_for
from flask_bootstrap import Bootstrap
from app import app
from app.classes import LoginForm, StartForm
from app.main import main


app.config['SECRET_KEY'] = 'gshn'
Bootstrap(app)
loginned = False



@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    global loginned
    form = LoginForm()
    if form.validate_on_submit():
        if form.password.data == '201239955' and form.username.data == 'gshn':
            loginned = True
            return redirect(url_for('adjoy_1c_master'))
        else:
            return '<h1>Invalid username or password</h1>'
    return render_template('login.html', form=form)


@app.route('/adjoy_1c_master', methods=['GET', 'POST'])
def adjoy_1c_master():
    global loginned
    if loginned:
        form = StartForm()
        if form.validate_on_submit():
            response = []
            try:
                if eval(form.days_to_parse.data) < 151:
                    pass
                else:
                    return '<h1>Введите количество дней от 0 до 150</h1>'
            except:
                return '<h1>Скорее всего что то введено неверно</h1>'
            response.append(eval(form.days_to_parse.data))
            response.append([form.parsing_buh.data, form.parsing.data, form.buh.data])
            if response[1].count(True) > 1:
                return '<h1>Пожалуйста выберете только один режим</h1>'
            mode = [i for i, x in enumerate(response[1]) if x][0]

            main(response[0], mode)
            return '<h1>Работа окончена</h1>'
        return render_template('adjoy_1c_master.html', form=form)
    else:
        return '<h1>Страница доступна только после успешной авторизации</h1>'
