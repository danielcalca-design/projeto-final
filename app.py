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


@app.route('/cadastro_equipamentos', methods=['GET', 'POST'])
def cadastro_equipamentos():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        data_equipamento = request.form.get("data_equipamento", "") or None
        descricao = request.form.get("descricao", "").strip()
        fabricante = request.form.get("fabricante") or None
        horario = request.form.get("horario") or None
        if not nome:
            flash("Preencha o nome do funcionario", "Error")
            return redirect(url_for("cadastro_equipamentos"))
        if not data_equipamento:
            flash("Preencha a data de nascimento do funcionario", "Error")
            return redirect(url_for("cadastro_equipamentos"))
        if not descricao:
            flash("Preencha o email do  funcionario", "Error")
            return redirect(url_for("cadastro_equipamentos"))
        if not fabricante:
            flash("Preencha a senha  funcionario", "Error")
            return redirect(url_for("cadastro_equipamentos"))
        if not horario:
            flash("Preencha a senha  funcionario", "Error")
            return redirect(url_for("cadastro_equipamentos"))

        tabela_equipamentos.salvar(nome, data_equipamento, descricao, fabricante, horario)
    clientes = tabela_equipamentos.select_todos_clientes()
    return render_template('cadastro_equipamentos.html', clientes=clientes)


def cadastro_ordem_servico():
    if request.method == "POST":
        id_os = request.form.get("nome", "").strip()
        id_equipamento = request.form.get("data_equipamento", "") or None
        descricao = request.form.get("descricao", "").strip()
        id_cliente = request.form.get("fabricante") or None
        data_hora = request.form.get("horario") or None
        if not id_os:
            flash("Preencha o nome do funcionario", "Error")
            return redirect(url_for("cadastro_ordens"))
        if not id_equipamento:
            flash("Preencha a data de nascimento do funcionario", "Error")
            return redirect(url_for("cadastro_ordens"))
        if not descricao:
            flash("Preencha o email do  funcionario", "Error")
            return redirect(url_for("cadastro_ordens"))
        if not id_cliente:
            flash("Preencha a senha  funcionario", "Error")
            return redirect(url_for("cadastro_ordens"))
        if not data_hora:
            flash("Preencha a senha  funcionario", "Error")
            return redirect(url_for("cadastro_ordens"))

        tabela_ordens.salvar(id_os, id_equipamento, descricao, data_hora)
    clientes = tabela_ordens.select_todos_clientes()
    return render_template('cadastro_equipamentos.html', clientes=clientes)