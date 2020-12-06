<h1 align="center"> 
   API Imobiliaria :house:
</h1>

## :white_check_mark: Status do Projeto
- Status: em desenvolvimento :construction:

 ### :link: Tecnologias

![Python](https://img.shields.io/badge/Python-v3.9.0-blue) 
![Django](https://img.shields.io/badge/Django-v3.1.2-blue) 
![Django Rest Framework](https://img.shields.io/badge/DjangoRestFramework-v3.12.1-blue)



### URL's


|    Endpoint     |                    URL                          |  
|-----------------|-------------------------------------------------|
|  Register       |  `http://localhost:8000/api/v1/register/`       |   
|  Login          |  `http://localhost:8000/api/v1/login/`          |   
|  Logout         |  `http://localhost:8000/api/v1/logout/`         |   
|  Logoutall      |  `http://localhost:8000/api/v1/logoutall/`      |   
|  Profile        |  `http://localhost:8000/api/v1/profile/`        |  
|  Address        |  `http://localhost:8000/api/v1/address/`        |   
|  Immobile type  |  `http://localhost:8000/api/v1/immobiletype/`   |
|  Immobile       |  `http://localhost:8000/api/v1/immobile/`       | 
|  Sale buy       |  `http://localhost:8000/api/v1/saleBuy/`        |
|  Lease          |  `http://localhost:8000/api/v1/lease/`          |
|                 |                                                 |



### Features

:white_check_mark: OK <br>
:heavy_exclamation_mark: Em análise <br>

:white_check_mark: Register / Login  <br>
:white_check_mark: Profile user  <br>
:white_check_mark: Property registration for sale  <br>
:white_check_mark: Rental property registration  <br>
:white_check_mark: Add permissions  <br>
:white_check_mark: Deploy Heroku  <br>
:heavy_exclamation_mark: Review script  <br>



## Link deploy [deploy-heroku](https://apimobiliaria.herokuapp.com/)



## Arquitetura final do projeto

Este projeto tem como finalizade expor uma API de uma imobiliaria, onde um usuário pode criar um perfil,
logar no sistema e adicionar um ou mais imoveis. Para locação, venda ou comprar um imóvel.

Foi desenvolvido um **Front end** para consumir os dados desta API, o repositório pode ser acessado neste link. [Front end](https://github.com/fabriciocovalesci/Imobiliaria-frontend-Svelte).

O checkout da transação na compra do imovel ou aluguel, é gravado em num blockchain de desenvolvimento, para emular este blockchain local, foi utilizado o [Ganache](https://www.trufflesuite.com/ganache). Foi desenvolvido um *smart contract* na **linguagem Solidity**, com toda lógica da regra do negócio.


## Como rodar este projeto

|           Descrição                  |                          COMANDOS                                      |  
|--------------------------------------|------------------------------------------------------------------------|
|  Clonar o repositório                |  `git clone git@github.com:fabriciocovalesci/API_Imobiliaria.git`      |   
|  Acessar a pasta API_Imobiliaria     |  `cd API_Imobiliaria`                                                  |   
|  Criar um virtualenv python          |  `python -m venv virtualenv`                                           |   
|  Ativar o virtualenv                 |  `source virtualenv/bin/activate`                                      |   
|  Instalar as dependências do projeto |  `pip install -r requirements.txt`                                     |  
|  Instalar as dependências do projeto |  `pip install -r requirements.txt`                                     |
|  Rodar as migrações do BD            |  `python manage.py migrate`                                            |   
|  Subir o servidor python             |  `python manage.py runserver`                                          |
|                                      |                                                                        | 

