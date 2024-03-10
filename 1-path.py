from pathlib import Path 

p1 = Path('dados', 'teste.txt')
print(p1)
print(type(p1)) # devolve o tipo de arquivo
print(p1.name)  # devolve o nome do arquivo
print(p1.stem)   # devolve o que esta antes do .
print(p1.suffix)  # devolve o que esta depois do .
print(p1.exists()) # checa se o arquivo existe, devolvendo true/false
if p1.exists():
    with open (p1, 'r', encoding='utf-8') as file:
        print(file.read())
        
p2 = Path('dados')
print(list(p2.iterdir())) # listar os arquivos