from flask import flash
from sqlalchemy import select, func
from sqlalchemy.exc import SQLAlchemyError

from models import db_session, Cliente

def select_todos_clientes():
    clientes_sql = select(Cliente)
    clientes = db_session.execute(clientes_sql).scalars()
    return clientes
def select_total_clientes():
    clientes_sql = select(func.count(Cliente.id))
    quantidade_total = db_session.execute(clientes_sql).scalar
    return quantidade_total
print(select_total_clientes())
def salvar(nome,data_nsc,email,senha):
    try:
        funcionario_novo = Cliente(nome,data_nsc,email,senha)
        db_session.add(funcionario_novo)
        db_session.commit()
        flash('Funcionario cadastrado com sucesso', 'success')
    except SQLAlchemyError as e:
        db_session.rollback()
        flash('ocorreu um erro, tente novamente', 'error')
        print(f"Erro: {e}")
    except Exception as e:
        db_session.rollback()
        flash('ocorreu um erro, tente novamente', 'error')
        print(f"Erro: {e}")
def select_um(id_cliente):
    clientes_sql = select(Cliente).where(Cliente.id_cliente == id_cliente)
    clientes = db_session.execute(clientes_sql).scalar_one_or_none()
    return clientes