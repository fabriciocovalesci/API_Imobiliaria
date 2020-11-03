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
:heavy_exclamation_mark: Review script  <br>



## Arquitetura final do projeto

Este projeto tem como finalizade expor uma API de uma imobiliaria, onde um usuario pode criar um perfil,
logar no sistema e adicionar um ou mais imoveis. Para locação, venda ou comprar um imóvel.

Na segunda parte do projeto será desenvolvido um *smart contract* na **linguagem Solidity**, utilizaremos a **rede Ethereum** como **Blockchain**, esta API, irá fornecer os dados. 

Será utilizado um *oráculo* da **ChainLink**, para fazer a comunicação entre a API e o smart contract.


![Arquitetura-versao](https://user-images.githubusercontent.com/40548641/97950272-1ecc0b80-1d75-11eb-9f9b-22df00c50ab1.jpg)

