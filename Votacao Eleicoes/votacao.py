candidato = []
vencedor = []
with open('dados_eleicao.txt', 'r') as dados:
  for votos in dados.readlines()[1:]:
    voto = votos.split(',')
    candidato.append(voto[2].replace('\n',''))


khan = candidato.count('Khan')
correy = candidato.count('Correy')
li = candidato.count('Li')
tooley = candidato.count("O'Tooley")

if khan > correy and khan > li and khan > tooley:
  vencedor = 'Khan'
elif correy > khan and correy > li and correy > tooley:
  vencedor = 'Correy'
elif li > khan and li > correy and li > tooley:
  vencedor = 'Li'
elif tooley > khan and tooley > correy and tooley > li:
  vencedor = "O'Tooley"

with open('resultado.txt', 'w') as relatorio:
  relatorio.write('Resultados Eleitorais\n')
  relatorio.write(('-'*25) + '\n')
  relatorio.writelines(f'Total de votos: {len(candidato)}\n')
  relatorio.write(('-'*25) + '\n')
  relatorio.writelines(f'Khan: {(khan/len(candidato) * 100):.2f}% ({khan}) \n')
  relatorio.writelines(f'Correy: {(correy/len(candidato) * 100):.2f}% ({correy})\n')
  relatorio.writelines(f'Li: {(li/len(candidato) * 100):.2f}% ({li}) \n')
  relatorio.writelines(f"O'Tooley: {(tooley/len(candidato) * 100):.2f}% ({tooley})\n")
  relatorio.write(('-'*25) + '\n')
  relatorio.writelines(f'Vencedor: {vencedor}\n')
  relatorio.write(('-'*25) + '\n')