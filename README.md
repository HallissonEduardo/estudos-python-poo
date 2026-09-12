# 🐍 Estudos em Python - Programação Orientada a Objetos (POO)

![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

Repositório dedicado aos meus exercícios práticos e anotações de estudo sobre **Programação Orientada a Objetos (POO)** utilizando a linguagem Python.

## 🎯 Objetivo dos Estudos
O foco destes exercícios é consolidar os pilares fundamentais da POO na prática, evoluindo desde a criação simples de objetos até arquiteturas mais complexas como o padrão MVC (Model-View-Controller).

## 📂 Estrutura dos Exercícios
O repositório contém 16 exercícios progressivos. Abaixo está o índice detalhado de cada um:

- **Modelagem Básica e Herança** - Criação de uma classe `Veiculo` (com métodos de ligar, acelerar e frear) e uma classe filha `Moto` que herda seus atributos.
- **Lógica de Negócios** - Simulação de uma Conta Bancária com métodos de saque, depósito e validação de saldo.
- **Herança Simples** - Sistema corporativo com a classe `Funcionario` e a classe filha `Gerente`.
- **Polimorfismo e Type Hinting** - Uso do módulo `typing (Generic, TypeVar)` para calcular áreas de Formas Geométricas (Retângulo e Círculo).
- **Composição** - Criação de uma estante de livros, onde a classe `Biblioteca` armazena objetos da classe `Livro`.
- **Variáveis de Classe** - Criação de um contador global compartilhado entre todas as instâncias da classe `Funcionario`.
- **Encapsulamento e Properties** - Uso dos decoradores `@property` e `.setter` para validar a alteração de temperatura em um Termostato.
- **Métodos Mágicos (Dunder Methods)** - Implementação dos métodos `__str__` e `__len__` em um Carrinho de Compras.
- **Classes Abstratas (ABC)** - Uso da biblioteca `abc` para forçar a implementação do método `emitir_som()` nas classes filhas `Cachorro` e `Gato`.
- **Interação de Objetos** - Sistema de Batalha RPG, onde a classe `Personagem` interage recebendo instâncias da classe `Arma`.
- **Tratamento de Dados e `match-case`** - Validação de dias da semana utilizando getters, setters e estrutura de controle (match-case).
- **Fixação de Classes Abstratas** - Obrigação de implementação de métodos em uma classe `Controle` de Ar-condicionado.
- **Métodos de Classe (`@classmethod`)** - Criação de fábricas (factories) instanciando um objeto `Data` a partir de uma string formatada ("DD-MM-YYYY").
- **Métodos Estáticos (`@staticmethod`)** - Implementação de lógicas utilitárias (validador de e-mail) sem depender do `self` ou `cls`.
- **Herança Múltipla** - Criação de um `SuperHeroi` que herda simultaneamente as habilidades das classes `Nadador` e `Voador`.
- **Design Pattern MVC** - Construção de um Gerenciador de Tarefas completo e estruturado separando dados (Model), interface (View) e lógica (Controller).

## 🛠️ Tecnologias e Conceitos Aplicados
- Python 3.x
- PEP 8 
- Type Hinting 
- Padrão de Arquitetura MVC
- Tratamento de Exceções 