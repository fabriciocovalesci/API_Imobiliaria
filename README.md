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

:white_check_mark: OK
:heavy_exclamation_mark: Em análise

:white_check_mark: Register / Login
:white_check_mark: Profile user
:white_check_mark: Property registration for sale
:white_check_mark: Rental property registration
:white_check_mark: Add permissions
:heavy_exclamation_mark: Review script



## Arquitetura final do projeto

Este projeto tem como finalizade expor uma API de uma imobiliaria, onde um usuario pode criar um perfil,
logar no sistema e adicionar um ou mais imoveis. Para locação, venda ou comprar um imóvel.

Na segunda parte do projeto será desenvolvido um *smart contract* na *linguagem Solidity*, utilizaremos a *rede Ethereum* como *Blockchain*, esta API, irá fornecer os dados. 

Será utilizado um *oráculo* da *ChainLink*, para fazer a comunicação entre a API e o smart contract.


![alt text](/home/fabricio/Documentos/APNPs/Projeto_Integrador/API_Imobiliaria/API_Imobiliaria/ImgReadme/Arquitetura-versao.jpg)

