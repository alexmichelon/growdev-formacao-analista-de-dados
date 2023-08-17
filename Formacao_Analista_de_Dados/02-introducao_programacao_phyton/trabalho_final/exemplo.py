def validate_integer_positive_whit_range_included(order, comparision_1, comparision_2):
    value = input(order)
    while (not value.isdigit()) or (int(value) < comparision_1) or (int(value) > comparision_2):
            value = input(f'\nEntrada Inválida!\n{order}\n')
    return int(value)

possibility_position_1 = 1
possibility_position_2 = 20

variavel = validate_integer_positive_whit_range_included('Informe um valor dentre 1 e 20: ', possibility_position_1, possibility_position_2)
print(f'Informou valor válido: {variavel}')