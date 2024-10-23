from flask import Flask, request, render_template, redirect
from request_funcs import *
from condition_object import ConditionObject

app = Flask(__name__)


@app.route('/error')
def error_page():
    return render_template('error_page.html')


# Home page
@app.route('/', methods=['GET', 'POST'])
def start_page():
    # Тестируем на проблемы с API
    if not try_api():
        return redirect("/error")

    cond_obj_1 = ConditionObject()  # Создаем объекты где будет вся нужная нам информация о погоде
    cond_obj_2 = ConditionObject()

    if request.method == 'POST':

        cond_obj_1.add_data_from_post(1)  # Получаем данные из формы
        cond_obj_1.add_locationKey()  # Получаем ключ места
        cond_obj_1.add_condition_data()  # Получаем по ключу данные о погоде

        cond_obj_2.add_data_from_post(2)
        cond_obj_2.add_locationKey()
        cond_obj_2.add_condition_data()

    return render_template('start_page_3.html',
                           cond_obj_1=cond_obj_1,
                           cond_obj_2=cond_obj_2)


# Недоделанная карта мира, не хватило времени
@app.route('/world_map', methods=['GET', 'POST'])
def world_map():
    return render_template('world_map.html')


if __name__ == '__main__':
    app.run(debug=True)