from flask import *

import datetime, time
import subprocess

from config import *
from db import Database
import hello
import echo
import joke



app = Flask(__name__)

app.secret_key = "Rr9Svc89n8Wv4xn9ocnPQ261oLts0MZj"
app.permanent_session_lifetime = datetime.timedelta(days=999)


db = Database("db.db")



# Домашняя страница
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")



# Страница для создания нового бота
@app.route("/program_your_bot/", methods=["GET"])
def program_your_bot():
    return render_template("programm_your_bot.html")



# Все боты
@app.route("/bots/", methods=["GET"])
def bots():
    bots = db.get_all_bots()
    return render_template("bots.html", len_bots=len(bots), bots=bots, delete_bot_url=f"http://{HOST}:{PORT}/delete_bot/", restore_bot_url=f"http://{HOST}:{PORT}/restore_bot/")



# Удаление бота
@app.route("/delete_bot/", methods=["GET"])
def delete_bot():
    token = request.args.get("token", "")

    if token != "":
        data = db.delete_bot_from_bots(token)
        return "\n".join(map(str, data))

    return redirect("/")



# Востановление бота
@app.route("/restore_bot/", methods=["GET"])
def restore_bot():
    token = request.args.get("token", "")
    name = request.args.get("name", "")
    program_type = request.args.get("program_type", "")

    if token != "":
        db.add_bot_to_bots(token, name, program_type)
        subprocess.Popen(f'python {program_type}.py {token}')  # Запуск бота

        return "Ok!"

    return redirect("/")



# Добавление новой задачи (бота) в бд и её запуск
@app.route("/new_program/", methods=["GET"])
def new_program():
    token = request.args.get("token", "")
    name = request.args.get("name", "")
    program_type = request.args.get("program_type")

    bot = db.get_bot_data(token)
    if bot != None:
        session["error"] = ["A bot with this token already exists", bot[1]]
        return redirect("/error/")

    if token != "":
        db.add_bot_to_bots(token, name, program_type)
        subprocess.Popen(f'python {program_type}.py {token}')  # Запуск бота

        return redirect("/load")

    return redirect("/")



# Страница загрузки
@app.route("/load/", methods=["GET"])
def load():
    return render_template("load.html", redirect_to=f"http://{HOST}:{PORT}/bots")



# Страница ошибки
@app.route('/error/', methods=["GET"])
def error_function():
    try:
        error_list = session["error"]
        session["error"] = list()
    except KeyError:
        return redirect("/")

    if error_list == list():
        return redirect("/")

    if len(error_list) == 1:
        error_list.append("")

    return render_template("error.html", delay=4, error=error_list[0], bot_name=error_list[1], redirect_to=f"http://{HOST}:{PORT}/program_your_bot")



if __name__ == "__main__":
    bots = db.get_all_bots()

    db.delete_all_bots()

    time.sleep(2)

    # Запуск ботов
    for i in bots:
        db.add_bot_to_bots(i[0], i[1], i[2])
        subprocess.Popen(f'python {i[2]}.py {i[0]}')


    app.debug = False
    app.run(host=HOST, port=PORT, threaded=True)