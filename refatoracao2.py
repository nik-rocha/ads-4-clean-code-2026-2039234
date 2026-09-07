from dataclasses import dataclass, field
from enum import Enum
import random

# Refatoração 1

# @dataclass
# class Usuario:
#     nome: str
#     email: str
#     senha: str
#     cargo: str
    
# minimo_senha = 8

# class Cargo(Enum):
#     ADMINISTRADOR = "Administrador"
#     PADRRAO = "Padrão"

# def validar_senha(senha: str) -> bool:
#     return len(senha) >= minimo_senha

# def validar_adm(usuario: Usuario) -> None:
#     return usuario.cargo == Cargo.ADMINISTRADOR.value

# def conceder_permissao_adm(usuario: Usuario) -> None:
#     print(f"Permissão de administrador concedida ao usuário {usuario.nome}.")
    
# def exibir_boas_vindas(usuario: Usuario) -> None:
#     print(f"\nUsuário {usuario.nome} cadastrado com sucesso! Seja bem-vindo.")

# def cadastrar_usuario(usuario: Usuario, enviar_boas_vindas: bool = True) -> bool:
#     if not validar_senha(usuario.senha):
#         print("Senha inválida. Tente novamente.")
#         return False
        
#     if validar_adm(usuario):
#         conceder_permissao_adm(usuario)
        
#     if enviar_boas_vindas:
#         exibir_boas_vindas(usuario)
        
#     return True

# user1 = Usuario("Marcos", "marcos@gmail.com", "12345678", "Administrador")
# cadastrar_usuario(user1)    

# ---------------------------------------------------------------------------------------------

# Trade-offs:
# * Separar cada função do cadastro em outra função traz maior legibilidade e simplicidade de ajustes ao código, o mesmo vale para os valores.
# * Especificar exatamente o que entra e sai em cada função facilita o entendimento do código.
# * Colocar os cargos em um Enum garante maior segurança ao usuário e facilita a escrita.

# ---------------------------------------------------------------------------------------------

# Refatoração 2

# @dataclass
# class Produto:
#     nome: str
#     cod_registro: int
#     qtd_estoque: int = 0
    
# limite_log = 20000
    
# def salvar_estoque(produto: Produto) -> None:
#     print(f"A adição do produto {produto.nome} - {produto.cod_registro} foi salvo no regristo do estoque.")

# def geral_log_produto(produto: Produto) -> None:
#     numero_log = random.randint(1, limite_log)
#     print(f"A adição do produto {produto.nome} - {produto.cod_registro} teve seu log gerado no sistema: Nº {numero_log}")
#     return numero_log
    
# def notificar_produto(produto: Produto) -> None:
#     print(f"A adição do produto {produto.nome} - {produto.cod_registro} foi notificada aos funcionários do sistema.")

# def atualizar_estoque_quantidade(produto: Produto, quantidade_a_adicionar: int) -> int:
#     produto.qtd_estoque += quantidade_a_adicionar    
#     return produto.qtd_estoque

# teclado = Produto("Teclado Redragon", 223122)
# atualizar_estoque_quantidade(teclado, 2)
# salvar_estoque(teclado)
# geral_log_produto(teclado)
# notificar_produto(teclado)
# print(f"Quantidade atual: {teclado.qtd_estoque}")

# ---------------------------------------------------------------------------------------------

# A testabilidade é melhorada com a separação de cada função da atualização, ao invés de fazer tudo ao atualizar o estoque. O que pode ser feito após torna-se opcional.

# ---------------------------------------------------------------------------------------------

#Refatoração 3

@dataclass
class Item:
    nome: str
    cod_registro: int
    preco: float
    
@dataclass
class Cliente:
    nome: str
    forma_pagamento: str
    cpf: str
    lista_compras: list = field(default_factory=list)
    valor_pago: float = 0
    
fator_desconto = 0.9

def aplicar_desconto(cliente: Cliente) -> None:
    cliente.valor_pago = cliente.valor_pago * fator_desconto
    return print(f"Valor com promoção aplicada: {cliente.valor_pago}")

def salvar_venda(cliente: Cliente) -> None:
    print("Venda salva com os seguintes produtos:\n")
    for item in cliente.lista_compras:
        print(item.nome)

def emitir_nota(cliente: Cliente) -> None:
    print("Gerando nota fiscal da venda:\n")
    for item in cliente.lista_compras:
        print(f"{item.nome}: R${item.preco}")
        
def enviar_email(cliente: Cliente) -> None:
    print("Email enviado:\nOlá! A seguinte venda foi relizada contendo os seguintes produtos:\n")
    for item in cliente.lista_compras:
        print(f"{item.nome}: R${item.preco}")

def finalizar_venda(itens: list, cliente: Cliente) -> float:
    preco_total = 0

    for item in itens:
        preco_total += item.preco
        cliente.lista_compras.append(item)
        
    cliente.valor_pago += preco_total
    return preco_total

jose = Cliente("José", "Débito", "222.222.222-22")
mouse = Item("Mouse Redragon", 23149, 250.50)
teclado = Item("teclado Coursair", 3223, 540.55)
fone = Item("Fone Coursair", 2433, 680.00)
carrinho = [mouse, teclado, fone]

finalizar_venda(carrinho, jose)
aplicar_desconto(jose)
salvar_venda(jose)
emitir_nota(jose)
enviar_email(jose)
print(f"\nCompra de {jose.nome} finalizada\nValor pago: {jose.valor_pago}")

# ---------------------------------------------------------------------------------------------

# Decidi separar as funções para a melhor legibilidade e usabilidade, além de adicionar ações ao próprio cliente como forma de armazenas melhor o valor total.