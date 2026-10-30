from flask import flash
from sqlalchemy import select, func
from sqlalchemy.exc import SQLAlchemyError

from models import db_session, Ordem_servico

def select_todos_equipamentos():
    ordens_servicos_sql = select(Ordem_servico)
    ordens_servicos = db_session.execute(ordens_servicos_sql).scalars()
    return ordens_servicos
def select_total_equipamentos():
    ordens_servicos_sql = select(func.count(Ordem_servico.id_ordem))
    quantidade_total = db_session.execute(ordens_servicos_sql).scalar
    return quantidade_total
print(select_total_equipamentos())
def salvar(nome,data_nsc,email,senha):
    try:
        ordem_novo = Ordem_servico(nome,data_nsc,email,senha)
        db_session.add(ordem_novo)
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
    ordens_servicos_sql = select(Ordem_servico).where(Ordem_servico.id_ordem == id_equipamento)
    ordens = db_session.execute(ordens_servicos_sql).scalar_one_or_none()
    return ordens