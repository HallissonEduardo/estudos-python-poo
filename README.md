# 🐍 Estudos em Python - Programação Orientada a Objetos (POO)

![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

Repositório dedicado aos meus exercícios práticos e anotações de estudo sobre **Programação Orientada a Objetos (POO)** utilizando a linguagem Python.

## 🎯 Objetivo dos Estudos
O foco destes exercícios é consolidar os pilares fundamentais da POO na prática, evoluindo desde a criação simples de objetos até arquiteturas mais complexas como o padrão MVC (Model-View-Controller).

## 📂 Estrutura dos Exercícios
O repositório contém 16 exercícios progressivos. Abaixo está o índice detalhado de cada um:

- `POO_exercicio01.py`: **Modelagem Básica e Herança** - Criação de uma classe `Veiculo` (com métodos de ligar, acelerar e frear) e uma classe filha `Moto` que herda seus atributos.
- `POO_exercicio02.py`: **Lógica de Negócios** - Simulação de uma Conta Bancária com métodos de saque, depósito e validação de saldo.
- `POO_exercicio03.py`: **Herança Simples** - Sistema corporativo com a classe `Funcionario` e a classe filha `Gerente`.
- `POO_exercicio04.py`: **Polimorfismo e Type Hinting** - Uso do módulo `typing (Generic, TypeVar)` para calcular áreas de Formas Geométricas (Retângulo e Círculo).
- `POO_exercicio05.py`: **Composição** - Criação de uma estante de livros, onde a classe `Biblioteca` armazena objetos da classe `Livro`.
- `POO_exercicio06.py`: **Variáveis de Classe** - Criação de um contador global compartilhado entre todas as instâncias da classe `Funcionario`.
- `POO_exercicio07.py`: **Encapsulamento e Properties** - Uso dos decoradores `@property` e `.setter` para validar a alteração de temperatura em um Termostato.
- `POO_exercicio08.py`: **Métodos Mágicos (Dunder Methods)** - Implementação dos métodos `__str__` e `__len__` em um Carrinho de Compras.
- `POO_exercicio09.py`: **Classes Abstratas (ABC)** - Uso da biblioteca `abc` para forçar a implementação do método `emitir_som()` nas classes filhas `Cachorro` e `Gato`.
- `POO_exercicio10.py`: **Interação de Objetos** - Sistema de Batalha RPG, onde a classe `Personagem` interage recebendo instâncias da classe `Arma`.
- `POO_exercicio11.py`: **Tratamento de Dados e `match-case`** - Validação de dias da semana utilizando getters, setters e estrutura de controle (match-case).
- `POO_exercicio12.py`: **Fixação de Classes Abstratas** - Obrigação de implementação de métodos em uma classe `Controle` de Ar-condicionado.
- `POO_exercicio13.py`: **Métodos de Classe (`@classmethod`)** - Criação de fábricas (factories) instanciando um objeto `Data` a partir de uma string formatada ("DD-MM-YYYY").
- `POO_exercicio14.py`: **Métodos Estáticos (`@staticmethod`)** - Implementação de lógicas utilitárias (validador de e-mail) sem depender do `self` ou `cls`.
- `POO_exercicio15.py`: **Herança Múltipla** - Criação de um `SuperHeroi` que herda simultaneamente as habilidades das classes `Nadador` e `Voador`.
- `POO_exercicio16.py`: **Design Pattern MVC** - Construção de um Gerenciador de Tarefas completo e estruturado separando dados (Model), interface (View) e lógica (Controller).

## 🛠️ Tecnologias e Conceitos Aplicados
- Python 3.x
- PEP 8 
- Type Hinting 
- Padrão de Arquitetura MVC
- Tratamento de Exceções 