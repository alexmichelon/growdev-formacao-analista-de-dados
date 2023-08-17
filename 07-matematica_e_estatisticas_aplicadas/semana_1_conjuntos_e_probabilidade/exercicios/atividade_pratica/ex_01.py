print('Atividade Prática 01 - \nEm uma cerimônia de colação de grau de certa universidade, 30 mulheres e '
    '20 homens receberam seus diplomas de concluintes em curso de nível '
    'superior. Entre as mulheres, formaram-se 10 arquitetas, 14 médicas e 6 '
    'engenheiras. Entre os homens, formaram-se 2 arquitetos, 10 médicos e 8 '
    'engenheiros. Durante essa cerimônia, um dos formandos foi escolhido ao '
    'acaso para fazer o juramento em nome de todos. Sabendo que o formando '
    'sorteado foi uma mulher, qual é a probabilidade de que ela seja uma médica '
    'formada?\n\n')

mulheres  = 30
homens  = 20
mulheres_arquitetas = 10
mulheres_medicas = 14
mulheres_engenheiras = 6
homens_arquitetos = 2
homens_medicos = 10
homens_engenheiros = 8

formado_juramento = 0

print(f'A probabilidade de uma mulher formada em medicina ser escolhida para '
      f'fazer o juramento em nome de todos é de: {mulheres_medicas}/{mulheres}, '
      f'{((mulheres_medicas/mulheres) * 100):.2f}%.')