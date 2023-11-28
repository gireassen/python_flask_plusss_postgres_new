import html
from flask import Flask, render_template, request #модуль(flask),класс(Flask)
from format_str_lst import format_string_to_list
from working_main import connect, single_insert, make_param_dic

app = Flask(__name__, template_folder='templates') #создание экземпляра объекта Flask и присваивание его переменной app
            #__name__ опредееляеется интерпритатором пайтон и, когда используется где-то в прогрм. коде, устанавливается равным имени текущего активного модуля

@app.route('/') #декоратор route из Flask доступен через app, созданную выше. деек-ор связваеет веб путь '/' с ф. main.
def main() -> str:
    return "Main file"

@app.route('/query_result', methods = ['POST'])
def do_query() -> 'html':
    text = request.form.get("query")
    print("TEXT FROM do_query:",text)
    query = format_string_to_list(text)
    print(query)
    database = request.form["database"]
    user = request.form["user"]
    password = request.form["password"]
    host = request.form["host"]
    port = request.form["port"]
    connection_parametters = make_param_dic(database, user, password, host, port)
    conn = connect(connection_parametters)
    for q in query:
        single_insert(conn, q)
    print("query_to_do from main.py",query)
    return render_template('results.html', 
                            query = query,
                            the_results = single_insert(conn, q))

@app.route('/entry')
def vars_page() -> 'html':
    return render_template('entry.html',
                           the_title = "PostgreSQL query.") #Указали имя шаблона, и пеередали значение аргументу the_title
if __name__ == '__main__':
    app.run(debug= False)