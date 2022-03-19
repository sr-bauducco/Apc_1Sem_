# Conversão de Real para Dólar
cotacao =float(input())
lote = int(input())
vendido = int(input())
i=1
while i < vendido+1:
    print(f'Lote: {i} - Total da venda: R$ {(lote * cotacao) + (0.025 * lote* cotacao):.2f}')
    i = i+1
    
    
    
