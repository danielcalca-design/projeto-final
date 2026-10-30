from flask import flash
from sqlalchemy import select, func
from sqlalchemy.exc import SQLAlchemyError

from models import db_session, Equipamento

def select_todos_equipamentos():
    equipamentos_sql = select(Equipamento)
    equipamentos = db_session.execute(equipamentos_sql).scalars()
    return equipamentos
def select_total_equipamentos():
    equipamentos_sql = select(func.count(Equipamento.id_equipamento))
    quantidade_total = db_session.execute(equipamentos_sql).scalar
    return quantidade_total
print(select_total_equipamentos())
def salvar(nome,data_nsc,email,senha):
    try:
        funcionario_novo = Equipamento(nome,data_nsc,email,senha)
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
def select_um(id_equipamento):
    equipamentos_sql = select(Equipamento).where(Equipamento.id_equipamento == id_equipamento)
    equipamentos = db_session.execute(equipamentos_sql).scalar_one_or_none()
    return equipamentos