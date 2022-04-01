func1 = [] #Pedro
func2 = [] #Maria
func3 = [] #Carlos
func4 = [] #Gabriel
func5 = [] #Ana
dados = [] # soma de todos
top3 = []
for c in range(5):
    nome = str(input("Nome do funcionario: ")).title()
    nota = int(input('Nota do funcionario (1 a 5): '))
    
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
        

dados.append(str(sum(func1)) + ' - Pedro')
dados.append(str(sum(func2)) + ' - Maria')
dados.append(str(sum(func3))+ ' - Carlos')
dados.append(str(sum(func4))+ ' - Gabriel')
dados.append(str(sum(func5))+ ' - Ana')
        
dados.sort(reverse=True)
top3.append(dados[0])
top3.append(dados[1])
top3.append(dados[2])
    
print(top3)
