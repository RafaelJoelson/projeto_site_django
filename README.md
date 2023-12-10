# projeto_site_rafael

Este é meu primeiro projeto desenvolvido em python e django.
Também é o primeiro projeto que utilizei o github.
Meu site pessoal com o meu portifólio.

## Conteúdo

Explicação sobre os principais arquivos e diretórios no seu projeto.

- `app_website/`: Contém os arquivos da aplicação Django.
	- `templates/`: Contém os arquivos HTML das páginas.
		- about.html : Página que contém informações sobre características pessoais.
		- contact.html : Página de contato onde o usuário submete o formulário.
		- education.html : Página que contém informações sobre formação.
		- home.html : Página inicial.
		- portfolio.html : Página de portifólio para apresentar projetos.
		- success.html : Página resposta afirmativa do formulário.
	- `migrations/`: Contém as migrações dos dados do projeto.
		- 0001_initial.py : Migração inicial do banco de dados.
	- `admin.py`: Configurações para o Django Admin.
	- `apps.py`: Configurações da aplicação.
	- `decorators.py`: Contém decoradores personalizados utilizados para controlar o acesso a determinadas páginas no projeto.
	- `forms.py`: Formulários do Django para validação.
	- `models.py`: Modelos de dados para o banco de dados.
	- `tests.py`: Testes da aplicação.
	- `urls.py`: Configurações de URLs da aplicação.
	- `views.py`: Funções de visualização da aplicação.
- `static/`: Local para armazenar arquivos de mídia (vídeos, imagens, etc.).
	- `css/`: Armazena os estilos CSS do projeto.
	- `imgs/`: Armazena as imagens do projeto.
	- `videos/`: Armazena os videos do projeto.

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/RafaelJoelson/projeto_site_django.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd projeto_site_rafael
    ```

3. Crie e ative um ambiente virtual:

	```bash
    conda create --name pythonProject python=3.11
    conda activate pythonProject
    ```

4. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

5. Execute as migrações do banco de dados:

    ```bash
    python manage.py migrate
    ```

6. Crie um superusuário para acessar o Django Admin:

    ```bash
    python manage.py createsuperuser
    ```

7. Inicie o servidor de desenvolvimento:

    ```bash
    python manage.py runserver
    ```

8. Acesse o sistema em [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Acesso ao Django Admin

1. Acesse [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).
2. Faça login com as credenciais do superusuário.

## Créditos
	
	riajulislam:
	Ícones dos facebook, linkedin e instagram.
	Disponível em :https://www.flaticon.com/br/autores/riajulislam
	

## Autor

Rafael Joelson
