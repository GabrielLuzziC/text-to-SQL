# Autor: Gabriel Luzzi Correa   RA: 2516918
# Projeto: Text to SQL

# --- Descrição ---
# Para as traduções de linguagem natural para SQL, foi usado o modelo Gemma3:4b, 
# que é um modelo de linguagem treinado pela Google, e está disponível no Ollama.

# Para interface com o banco de dados, foi utilizado o SQLAlchemy,
# que é uma biblioteca Python para interagir com bancos de dados SQL.

# Para a interface gráfica, foi utilizado o Streamlit,
# que é uma biblioteca Python para criar aplicativos web interativos de forma rápida e fácil.
# -----------------

import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from langchain_community.utilities import SQLDatabase
from langchain_ollama import ChatOllama
from langchain.chains import create_sql_query_chain

#conexão com o banco de dados
def get_db_connection(db_type, user, password, host, port, database):
    try:
        if db_type.lower() == 'mysql':
            conn_string = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}" # gera a string de conexão 
        elif db_type.lower() == 'postgresql':
            conn_string = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
        else:
            return None
        engine = create_engine(conn_string) # faz a ponte com o banco de dados
        engine.connect()
        return engine
    except Exception as e:
        st.error(f"Erro ao conectar ao banco de dados: {e}")
        return None
    
# geração da query SQL e conexão com o modelo de linguagem
def get_sql_query(engine, natural_query):
    try:
        db = SQLDatabase(engine) # pega as tabelas e campos do banco de dados
        llm = ChatOllama(model="gemma3:4b", temperature=0) #inicializa o chat
        chain = create_sql_query_chain(llm, db) #cria a cadeia de consulta SQL

        #prompt para gerar a consulta SQL
        prompt = f"""Você é um assistente de IA especialista em converter perguntas em linguagem natural para consultas SQL 
        para um banco de dados. Dada a pergunta, gere uma consulta em SQL.
        Pergunta: {natural_query}
        Instrução adicional: A menos que o usuário peça explicitamente um número de resultados (ex: 'top 5' ou 'limite 5'), 
        a consulta SQL gerada NÃO DEVE incluir uma cláusula LIMIT. Retorne todos os resultados.
        """
        sql_query = chain.invoke({"question": prompt}) 
        sql_query = sql_query.replace("```sql", "").replace("```", "").strip()  # limpa a formatação
        return sql_query
    except Exception as e:
        st.error(f"Erro ao gerar a query SQL: {e}")
        st.info("Dica: Verifique se o Ollama está rodando.")
        return None

# execução da query SQL e retorno dos resultados
def execute_sql_and_get_results(engine, query):
    if not query:
        return None
    try:
        with engine.connect() as connection:
            result_df = pd.read_sql_query(query, connection) # executa a consulta SQL e retorna os resultados em um DataFrame
        return result_df
    except Exception as e:
        st.error(f"Erro ao executar a query: {e}")
        return None
    
# --- Interface Gráfica com Streamlit ---
st.set_page_config(page_title='Assistente de Banco de Dados', layout='wide')
st.title('🤖 Assistente de Banco de Dados com IA')
st.caption('Faça uma pergunta em linguagem natural sobre seus dados e obtenha a resposta.')

# Usamos o st.session_state para "lembrar" da conexão com o banco
if 'engine' not in st.session_state:
    st.session_state.engine = None

# Campo de entrada para a pergunta do usuário
with st.sidebar:
    st.header('Configuração do Banco de Dados')
    db_type = st.selectbox('Tipo de Banco de Dados', ['MySQL', 'PostgreSQL'])
    host = st.text_input('Host', 'localhost')
    port = st.text_input('Porta', '3306' if db_type == 'MySQL' else '5432')
    user = st.text_input('Usuário' , 'root' if db_type == 'MySQL' else 'postgres')
    password = st.text_input('Senha', type='password')
    database = st.text_input('Nome do Banco de Dados')

    if st.button("Conectar ao Banco"):
        st.session_state.engine = get_db_connection(db_type, user, password, host, port, database) # conecta ao banco de dados
        if st.session_state.engine:
            st.success("Conexão estabelecida com sucesso!")
    
# Campo de entrada para a pergunta do usuário
if st.session_state.engine is None:
    st.info("Por favor, configure e conecte-se a um banco de dados para começar.")
else:
    st.success("Conectado! Pronto para receber suas perguntas.")

    natural_query = st.text_input("Sua pergunta", placeholder="Ex: Quais os professores com maior salário por departamento?")

    if st.button("Gerar Consulta SQL"):
        if natural_query:
            with st.spinner("Pensando e consultando os dados..."):
                # Gera a consulta SQL a partir da pergunta em linguagem natural
                st.subheader("1. Query SQL Gerada")
                sql_query = get_sql_query(st.session_state.engine, natural_query)

                if sql_query:
                    st.code(sql_query, language="sql")

                    # Executa a consulta SQL e obtém os resultados
                    st.subheader("2. Resultados da Consulta")
                    result_df = execute_sql_and_get_results(st.session_state.engine, sql_query)

                    if result_df is not None:
                        if result_df.empty:
                            st.warning("A consulta foi executada, mas não retornou resultados.")
                        else:
                            st.dataframe(result_df)
                else:
                    st.error("Não foi possível gerar a consulta SQL. Verifique a pergunta e tente novamente.")
        else:
            st.warning("Por favor, insira uma pergunta antes de gerar a consulta SQL.")
