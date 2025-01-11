# 🌹 Gilded Rose Refatorado - Python
Esta atividade consiste na refatoração do famoso kata Gilded Rose, aplicando boas práticas de programação e técnicas de design de software utilizando Python. 🚀

## 📋 Objetivo
- Refatorar o código original do Gilded Rose, que possuía alta complexidade e baixa legibilidade.
- Implementar boas práticas de clean code, como SRP (Single Responsibility Principle) e Open/Closed Principle (OCP).
- Facilitar a extensibilidade do sistema para a adição de novos tipos de itens.
- Garantir o funcionamento correto das regras de negócio por meio de testes automatizados.

## 📖 Sobre o Desafio
O desafio Gilded Rose Kata é um problema clássico que simula a manutenção de um sistema de inventário para uma loja fictícia. O objetivo principal é melhorar o código legado sem alterar o comportamento existente.

*Regras do Sistema:*
- A qualidade (quality) de um item nunca é negativa.
- A qualidade nunca é maior que 50 (exceto para itens "Sulfuras", que têm qualidade fixa de 80).
- A qualidade de itens normais diminui com o tempo.
- Itens especiais, como "Aged Brie" e "Backstage passes", têm comportamentos específicos:
  - Aged Brie aumenta em qualidade à medida que envelhece.
  - Backstage passes aumentam em qualidade à medida que o evento se aproxima, mas perdem todo o valor após o evento.
- Itens lendários, como "Sulfuras", não mudam de qualidade nem têm prazo de validade.

## 🎓 Aprendizados e Boas Práticas
- Aplicação de princípios SOLID.
- Uso de padrões de projeto para separar responsabilidades e melhorar a extensibilidade.
- Escrever testes automatizados para validar regras de negócio (TDD).
