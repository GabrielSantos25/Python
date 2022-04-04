func1 = [] # Pedro
func2 = [] # Maria
func3 = [] # Carlos
func4 = [] # Gabriel
func5 = [] # Ana
dados = [] # soma de todos
top3 = [] # Lista que apresenta os 3 melhores funcionarios

# For c (Coleta de informações / Avaliação do cliente.)
for c in range(5):
    nome = str(input("Escolha o Funcionario [Pedro, Maria, Carlos, Gabriel, Ana]: ")).title()
    nota = int(input('Informe a nota [1 a 5]: '))
   
    #Condições criadas para cada funcionario da loja. 
    if nome == 'Pedro':
        func1.append(nota)
    
    if nome == 'Maria':
        func2.append(nota)
    
    if nome == 'Carlos':
        func3.append(nota)
        
    if nome == 'Gabriel':
        func4.append(nota)
        
    if nome == 'Ana':
        func5.append(nota)
        
# Expressão criada para receber a soma das notas de cada funcionario junto com o nome.
dados.append(str(sum(func1)) + ' - Pedro')
dados.append(str(sum(func2)) + ' - Maria')
dados.append(str(sum(func3))+ ' - Carlos')
dados.append(str(sum(func4))+ ' - Gabriel')
dados.append(str(sum(func5))+ ' - Ana')

# Função sort organiza a lista em ordem crescente por padrão e Reverse é o metodo que inverte os elementos da lista.
dados.sort(reverse=True)

# Com os dados organizados do maior para menor, eu criei outra lista chamada top3 e adicionei os 3 primeiros indice nela que apresenta os 3 melhores colocados. 
for r in range(3):
    top3.append(dados[r])

print(top3)
