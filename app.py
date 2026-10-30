from flask import Flask, render_template, url_for, redirect, request, flash

from banco import tabela_equipamentos, tabela_recursos
from banco import tabela_clientes, tabela_ordens

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cadastro_clientes', methods=['GET', 'POST'])
def cadastro_clientes():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        data_nsc = request.form.get("data_nasc") or None
        email = request.form.get("email", "").strip()
        senha = request.form.get("senha") or None
        if not nome:
            flash("Preencha o nome do funcionario", "Error")
            return redirect(url_for("cadastro_clientes"))
        if not data_nsc:
            flash("Preencha a data de nascimento do funcionario", "Error")
            return redirect(url_for("cadastro_clientes"))
        if not email:
            flash("Preencha o email do  funcionario", "Error")
            return redirect(url_for("cadastro_clientes"))
        if not senha:
            flash("Preencha a senha  funcionario", "Error")
            return redirect(url_for("cadastro_clientes"))

        tabela_clientes.salvar(nome,data_nsc,email,senha)
    clientes = tabela_clientes.select_todos_clientes()
    return render_template('cadastro_clientes.html', clientes=clientes)