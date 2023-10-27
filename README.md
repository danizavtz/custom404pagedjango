# custom404pagedjango

### Instruções para executar

1. Clonar o projeto
2. Iniciar um virtualenv com python3, com o comando:

    virtualenv venv -p $(which python3)

3. Carregar o ambiente virtual, com o comando:

    source venv/bin/activate

4. instalar as dependências, com o comando:

    pip install -r requirements.txt

5. executar o servidor de desenvolvimento, com o comando:

    python manage runserver

6. Depois basta acessar qualquer rota que não esteja declarada no `urls.py`.

No meu caso eu acessei a rota `http://localhost:8000/a`.
