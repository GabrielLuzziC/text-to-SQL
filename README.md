# 🤖 Assistente de Banco de Dados com IA

Um assistente inteligente que converte perguntas em português para consultas SQL e exibe os resultados, tudo através de uma interface web amigável construída com Streamlit.

> Projeto desenvolvido como parte de um trabalho acadêmico, demonstrando a integração de Modelos de Linguagem Locais (LLMs) com bancos de dados relacionais.

### Demo da Aplicação

*(Dica: Grave um GIF da sua aplicação funcionando (usando ferramentas como ScreenToGif ou GIPHY Capture) e substitua o link acima para mostrar o seu projeto em ação\!)*

-----

## 🎯 Sobre o Projeto

Muitas vezes, usuários que não são técnicos precisam extrair informações valiosas de bancos de dados, mas não sabem escrever consultas SQL. Este projeto resolve esse problema, atuando como um "tradutor" entre a linguagem humana e a linguagem de banco de dados.

O usuário simplesmente faz uma pergunta como "Quantos clientes temos em cada cidade?" e a aplicação, usando um modelo de linguagem rodando localmente via **Ollama**, gera e executa a consulta SQL correspondente, exibindo os resultados de forma clara e interativa.

-----

## ✨ Funcionalidades

  - [x] **Conexão Segura:** Conecta-se a bancos de dados **MySQL** e **PostgreSQL**.
  - [x] **Análise de Esquema Inteligente:** Carrega e interpreta a estrutura do banco (tabelas e colunas) para dar contexto à IA.
  - [x] **Interface Web Amigável:** Uma interface limpa e intuitiva construída com **Streamlit**, onde o usuário pode configurar a conexão e fazer suas perguntas.
  - [x] **Conversão Text-to-SQL:** Utiliza a biblioteca **LangChain** e um modelo **Ollama** local (como Gemma ou Llama3) para converter perguntas em português para código SQL.
  - [x] **Visualização de Resultados:** Apresenta tanto a query SQL gerada quanto os dados resultantes em uma tabela interativa.

-----

## 🛠️ Tecnologias Utilizadas

  - **Python 3.10+**
  - **Streamlit:** Para a criação da interface web.
  - **Ollama:** Para servir o modelo de linguagem localmente.
  - **LangChain:** Como orquestrador para a lógica de Text-to-SQL.
  - **SQLAlchemy:** Para a conexão e abstração do banco de dados.
  - **Pandas:** Para manipulação e exibição dos dados.

-----

## 🚀 Começando

Siga os passos abaixo para executar o projeto localmente.

### Pré-requisitos

1.  **Python:** Certifique-se de ter o Python 3.10 ou superior instalado.
2.  **Ollama:** É necessário ter o [Ollama](https://ollama.com/) instalado e rodando em segundo plano.
3.  **Modelo de Linguagem:** Você precisará de um modelo baixado. Este projeto foi testado com `gemma:7b`. Para baixá-lo, rode no seu terminal:
    ```bash
    ollama pull gemma:7b
    ```
4.  **Banco de Dados:** Tenha um servidor MySQL ou PostgreSQL ativo e acessível.

### Instalação

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/seu-usuario/nome-do-seu-repositorio.git
    cd nome-do-seu-repositorio
    ```

2.  **Crie e ative um ambiente virtual (Recomendado):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3.  **Instale as dependências Python:**
    Um arquivo `requirements.txt` é a melhor forma de gerenciar as dependências. Se você não tiver um, crie-o e adicione o seguinte conteúdo:

    ```txt
    # requirements.txt
    streamlit
    pandas
    sqlalchemy
    langchain-ollama
    langchain-community
    mysql-connector-python
    psycopg2-binary
    tabulate
    ```

    Agora, instale tudo com um único comando:

    ```bash
    pip install -r requirements.txt
    ```

-----

## Usage

1.  **Garanta que o Ollama esteja rodando** em segundo plano.
2.  No seu terminal, na pasta do projeto, execute o seguinte comando:
    ```bash
    streamlit run app.py
    ```
3.  Uma aba no seu navegador será aberta com a aplicação.
4.  Na barra lateral esquerda, insira as credenciais do seu banco de dados e clique em "Conectar ao Banco".
5.  Uma vez conectado, digite sua pergunta em português no campo principal e clique em "Gerar Resposta".

-----

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

-----

## Agradecimentos

  - À equipe do **Streamlit** por tornar a criação de UIs em Python tão simples.
  - À comunidade **LangChain** pelas ferramentas incríveis de orquestração de LLMs.
  - Ao projeto **Ollama** por democratizar o acesso a modelos de linguagem poderosos localmente.