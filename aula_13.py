# -*- coding: utf-8 -*-
"""Aula_13

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YPPC1XGS-dZxG_DQrMjDg2oXpep0tNTj
"""



"""VERIFICAÇÃO DE STRINGS COM PYTHON

A verificação de strings em Python pode ser feita de várias maneiras, dependendo do que você precisa verificar. Aqui estão algumas das operações mais comuns de verificação de strings em Python:

1. **Verificar se uma Substring está em uma String:**
    
    Use o operador `in` para verificar se uma substring está presente em uma string.
"""

texto = "Isso é uma string de exemplo"
if "exemplo" in texto:
    print("A substring 'exemplo' está na string.")

"""2. **Verificar o Comprimento de uma String:**
    
    Use a função `len()` para obter o comprimento de uma string.
"""

texto = "Isso é uma string de exemplo"
comprimento = len(texto)
print(f"O comprimento da string é {comprimento}.")

"""3. **Verificar se uma String Começa ou Termina com uma Substring:**
    
    Use os métodos `.startswith()` e `.endswith()` para verificar se uma string começa ou termina com uma determinada substring
"""

texto = "Isso é uma string de exemplo"
if texto.startswith("Isso"):
    print("A string começa com 'Isso'.")

if texto.endswith("exemplo"):
    print("A string termina com 'exemplo'.")

"""4. **Verificar se uma String é Numérica:**
    
    Use o método `.isnumeric()` para verificar se uma string é composta apenas por caracteres numéricos.
"""

numero = "12345"
if numero.isnumeric():
    print("A string contém apenas dígitos numéricos.")

"""5. **Verificar se uma String é Alfabética:**
    
    Use o método `.isalpha()` para verificar se uma string contém apenas letras do alfabeto.
"""

palavra = "Python"
if palavra.isalpha():
    print("A string contém apenas letras do alfabeto.")

"""6. **Verificar se uma String é Alfanumérica:**
    
    Use o método `.isalnum()` para verificar se uma string é composta apenas por caracteres alfanuméricos (letras e números).
"""



texto = "Python123"
if texto.isalnum():
    print("A string contém apenas caracteres alfanuméricos.")

"""Essas são algumas das operações comuns de verificação de strings em Python. Dependendo da sua necessidade específica, você pode escolher a operação apropriada para verificar ou manipular strings em seu código.

Os métodos `startswith()` e `endswith()` em Python são usados para verificar se uma string começa ou termina com um determinado prefixo ou sufixo, respectivamente. Ambos os métodos retornam um valor booleano (True ou False) indicando se a string atende aos critérios especificados.

Aqui está a sintaxe básica dos métodos `startswith()` e `endswith()`:
"""

string.startswith(prefixo)
string.endswith(sufixo)

"""onde:

- `string` é a string que você deseja verificar.
- `prefixo` é a substring que você deseja verificar se a string começa com ela.
- `sufixo` é a substring que você deseja verificar se a string termina com ela.

Aqui estão exemplos de uso desses métodos:

**Exemplo do método `startswith()`:**
"""

frase = "Olá, mundo!"
if frase.startswith("Olá"):
    print("A frase começa com 'Olá'.")
else:
    print("A frase não começa com 'Olá'.")

cidade = 'São Carlos'
endereço = 'Rua Candido Padim, 25 - Vila Prado'
completo = cidade + endereço
print(cidade.startswith('São'))
print(cidade.endswith('los'))
print('rua' in completo)
print('padim' in completo)

email = 'senai@gmail.com'
print('senai@gmail.com' in email)
if "senai@gmail.com" in email:
  print(email)

texto = 'Python é uma linguagem de programação. Python é simples. Python é organizado. Python é uma excelente linguagem.'
print(texto.count('é')) #conta quantas vezes o 'é' é usado no texto.
print(texto.find('python', 25, 50))
print(texto.rfind('lingua'))
print(texto.index('é'))
print(texto.rindex('é'))

"""**Exercícios**

1: Escreva um programa que verifique se a palavra "python"
está presente na string "Estou aprendendo Python".**texto em negrito**
"""

string = 'Estou aprendendo Python'
if 'Python' in string:
  print('A palavra Python está presente.')

"""2: Escreva um programa que peça ao usuário para digitar
seu nome e verifique se o nome começa com a letra "A" (maiúscula ou minúscula).
"""

nome = input("Escreva seu Nome: ")
if nome.startswith("A") or nome.startswith("a"):
    print("A string começa com a letra 'A'.")
else:
  print("A string não começa com a letra 'A'.")

"""3: Escreva um programa que peça ao usuário para digitar uma
senha e verifique se a senha contém pelo menos 8 caracteres.

"""

Acesso = input('Digite o Código: ')
carateres = len(Acesso)
print(f'O número de carateres é {carateres}.')

if carateres >= 8:
  print('Excelente, você digitou uma boa quantidade de carateres!')
else:
  print('Coloque mais carateres!')

"""4: Escreva um programa que peça ao usuário para digitar
um número e verifique se o número é uma representação numérica (não contém
letras ou símbolos).
"""

numeros = input('Digite um número: ')
if numeros.isnumeric():
  print('Não contém letras ou símbolos.')

"""5: Escreva um programa que peça ao usuário para digitar uma frase
e conte quantas vezes a letra "a" (maiúscula ou minúscula) aparece na frase.


"""

frase = input('Digite uma frase: ')
print(frase.count('a'))