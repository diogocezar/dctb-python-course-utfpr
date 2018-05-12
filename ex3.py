nome_completo = "Diogo Cezar Teixeira Batista"
print(nome_completo)
print("A quarta e a ultima letra: {} - {}".format(nome_completo[3], nome_completo[-1]))
print("As três primeiras letras: {}".format(nome_completo[0:3]))
print("Uma lista com nome e sobrenome separados (a partir da string): ", nome_completo.split(" "))
print("Contar a quantidade de letras (sem contar o “espaço”)", len(nome_completo.replace(" ", "")))
print("As duas ultimas letras. (DESAFIO)", nome_completo[-2:])