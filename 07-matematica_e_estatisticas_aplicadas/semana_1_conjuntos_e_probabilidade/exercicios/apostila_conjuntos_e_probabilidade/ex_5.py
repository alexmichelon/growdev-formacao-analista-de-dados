'''
5)(FASP) Em uma escola são lidos dois jornais, A e B. Exatamente 70% dos
alunos lêem o jornal A e 60% dos alunos o jornal B. Sabendo-se que todo
aluno é leitor de pelo menos um dos jornais, o percentual de alunos que
leem os dois ambos os jornais é:
a) 130%
b) 10%
c) 20%
d) 30%
'''

total_alunos = 1
alunos_jornal_A = 0.7
alunos_jornal_B = 0.6

alunos_nao_A = total_alunos - alunos_jornal_A
alunos_nao_B = total_alunos - alunos_jornal_B
alunos_jornal_A_e_B = total_alunos - alunos_nao_A - alunos_nao_B
print(f'O percentual de alunos que lêem os dois jornais A e B é de {(alunos_jornal_A_e_B * 100):.2f}%.')