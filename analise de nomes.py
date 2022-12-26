print("""\nOlá, seja bem vindo! Esse programa irá analisar um nome completo e mostrar as seguintes informações:
- O nome com todas as letras maiúsculas;
- O nome com todas as letras minúsculas;
- Vai dizer quantas letras tem no nome (ignorando os espaços);
- Vai dizer também quantas lentras tem o primeiro nome.
Sabendo disso, vamos ao trabalho!""")

nome = input("\nDigite um nome completo que deseja analisar: ")
nmais = nome.upper()
nminus = nome.lower()
nlet = nome.replace(" ", "")
nq1 = len(nlet)
nq02 = nome.split()
nq2 = len(nq02[0])
linha = "-"*40

from time import sleep

print(f"\nLetras maiúsculas: {nmais}.\n{linha}")
sleep(0.75)
print(f"Letras minúsculas: {nminus}.\n{linha}")
sleep(0.75)
print(f"Quantas letras tem no nome: {nq1}.\n{linha}")
sleep(0.75)
print(f"Quantas no primeiro nome: {nq2}.")
