#Aluno:Marcel Gustavo de Barros Araujo
#Curso:Engenharia da Computação
A=1
s=2

cont=0
while (s>1):
  A=A/2
  s=1+A
  cont=cont+1

print(f"Precisão da máquina: {2*A}")
print(f"Número de iterações: {cont}")

#Explicação:
# '''
# A repetição só termina quando o valor de s se torna igual a 1, ou seja, quando o valor de A é tão pequeno que, ao adicioná-lo a 1,
# o resultado ainda é interpretado como 1 pela máquina. Isso acontece porque A se aproxima do menor valor positivo que o sistema consegue distinguir de 1,
# chamado de épsilon da máquina (ε).
# No caso dos números do tipo float (32 bits), são usados 24 bits para a mantissa, o que garante aproximadamente 7 dígitos decimais de precisão.
# Já o tipo double (64 bits) usa 53 bits na mantissa, permitindo cerca de 15 dígitos decimais, o que significa que ele consegue representar números bem menores
# com mais exatidão.
# Por isso, o double é considerado mais preciso do que o float – ele pode lidar com valores muito menores antes de alcançar o limite do epsilon,
# embora consuma o dobro da memória.
# O resultado (2*A) representa o menor número que, somado a 1,
# resulta em um valor maior que 1 no sistema de ponto flutuante.
# Isso define a precisão numérica da máquina.

# O contador mostra quantas divisões binárias foram necessárias
# para atingir esse limite.
# '''
