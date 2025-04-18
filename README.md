# Sistema de Cadastro de Usuários (Console)

Este é um projeto simples feito em **Python**, onde desenvolvi um sistema de cadastro de usuários no terminal. O objetivo foi praticar lógica de programação, uso de listas, dicionários e funções.

## O que o programa faz

O programa permite cadastrar, listar e buscar usuários usando um menu no console. Tudo acontece em memória (os dados não são salvos em arquivos).

### 1. Cadastro de Usuário

Quando o usuário escolhe essa opção, o programa:

- Pede o nome, e-mail e idade
- Cria um dicionário com essas informações
- Adiciona esse dicionário em uma lista chamada `usuarios`

Exemplo de dado salvo:
```python
{"nome": "Maria", "email": "maria@email.com", "idade": "22"}
