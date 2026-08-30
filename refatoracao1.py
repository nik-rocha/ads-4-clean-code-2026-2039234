# def calcular_pedido(lista_produtos):
#     valor_total = 0
#     limite_desconto = 1000
#     percentual_desconto = 0.1
#     desconto_pedido = 0

#     for produto in lista_produtos:
#         if produto["em_estoque"]:
#             valor_produto = produto["valor"] * produto["quantidade"]
#             valor_total += valor_produto
            
#     if valor_total > limite_desconto:
#         desconto_pedido = valor_total * percentual_desconto
#         valor_total -= desconto_pedido

#     return valor_total

# valor_final = calcular_pedido(lista_produtos)
# print("Valor final:", valor_final)

def calcular_relatorio(lista_funcionarios):
    contagem_funcionarios = 0
    salario_totalizado = 0
    limite_salario = 3000
    
    for funcionario in lista_funcionarios:
        salario = funcionario["salario"]
        
        if salario > limite_salario:
            contagem_funcionarios += 1
    
        salario_totalizado += salario
    
    
    return contagem_funcionarios, salario_totalizado

quantidade, total = calcular_relatorio(lista_funcionarios)

print("Quantidade:", quantidade)
print("Total:", total)