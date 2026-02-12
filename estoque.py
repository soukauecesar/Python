estoque_minimo = {
    'alimentos': 50,
    'bebidas': 75,
    'limpeza': 30
}

produto = input('Produto: ').strip()
categoria = input('Categoria (alimentos, bebidas ou limpeza): ').strip().lower()
qtde_input = input('Quantidade em estoque: ').strip()

if produto and categoria and qtde_input:
    try:
        qtde = int(qtde_input)

        if categoria in estoque_minimo:
            if qtde < estoque_minimo[categoria]:
                print(f'Solicitar {produto} à equipe de compras, temos apenas {qtde} unidades em estoque')
            else:
                print('Estoque dentro do nível mínimo.')
        else:
            print('Categoria inválida.')
    except ValueError:
        print('A quantidade deve ser um número inteiro.')
else:
    print('Preencha todas as informações corretamente.')