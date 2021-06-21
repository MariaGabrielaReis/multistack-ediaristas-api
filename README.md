<h1  align="center">
  <img
    width="280px"
    src="https://github.com/MariaGabrielaReis/multistack-ediaristas/blob/main/public/img/logos/logo.svg"
  />
</h1>

<p align="center" >
  <a href="#projeto">Sobre a aplicação</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#tecs">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#rotas">Rotas</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#requisitos">Como rodar</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#licenca">Licença</a>
</p>

<span id="projeto">
  
### :bookmark_tabs: Sobre a aplicação
O evento "Multi-stack", realizado em junho de 2021, foi promovido pela Treina Web e incluiu a criação de uma aplicação chamada "E-Diaristas", 
que tinha o objetivo de ser uma ferramenta para busca de profissionais especializados em serviços domésticos, baseando a pesquisa no CEP do contratante 
e mostrando os profissionais que estivessem disponíveis para a região, contando também com avaliações dos clientes, formando uma reputação de até 5 estrelas 
para cada contratado. Esta é a API utilizada pela [aplicação web](https://github.com/MariaGabrielaReis/multistack-ediaristas-web) e 
[mobile](https://github.com/MariaGabrielaReis/multistack-ediaristas-mobile), responsável pelo retorno das diaristas cadastradas disponíveis na região.

  
<span id="tecs">
  
### 🛠️ Tecnologias

As seguintes tecnologias e ferramentas foram utilizadas neste projeto:

<p> 
  <a href="https://www.djangoproject.com/"><img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"/></a>
  <a href="https://www.jetbrains.com/pt-br/pycharm/"><img src="https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=gray&labelColor=green"/></a>
</p>
  
<span id="rotas">
  
### 🛤️ Rotas
-  GET: http://127.0.0.1:8000/api/city-housekeepers?cep= (retorna as diaristas disponíveis na região do CEP pesquisado)

<span id="requisitos">

### :gear: Como rodar

Para utilizar a API, é preciso abrir o projeto junto com o [Painel Administrativo](https://github.com/MariaGabrielaReis/multistack-ediaristas-painel-administrativo) no Pycharm, já que pelo Django é possível construir várias aplicações em um mesmo ambiente. Depois de baixar o [Python](https://www.python.org/downloads/) e organizar as pastas da maneira abaixo, rode `pip install -r requirements.txt`, `python manage.py makemigrations`, `python manage.py migrate` e `python manage.py runserver` respectivamente no terminal para iniciar a aplicação administrativa e a API. 
  
```bash
📂 E-diaristas
|- 📁 .idea
|- 📁 ediaristas
|--- 📁 api
|--- 📁 ediaristas_workshop
|--- 📁 painel_administrativo
|--- 📄 manage.py
|--- 📄 requirements.txt
```
  
<span id="licenca">

### :page_with_curl: Licença

Esse projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

[![image](https://img.shields.io/badge/✨%20Maria%20Gabriela%20Reis,%202021-LinkedIn-009973?style=flat-square)](https://www.linkedin.com/in/mariagabrielareis/)
