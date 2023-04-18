# Define grupos
groups = {
'BEL01  ASAP : 301': range(30100, 30150),
'BEL02  ASAP : 301': range(30150, 30200),
'BEL03  HIZS : 302': range(30200, 30300),
'BEL04  ASAP : 303': range(30300, 30400),
'BEL05  ASAP : 304': range(30400, 30446),
'BEL06  ASAP : 304': range(30446, 30500),
'BEL07  ASAP : 305': range(30500, 30600),
'BEL08 BARREIRO 1  HIZS : 306': range(30600, 30646),
'BEL09 BARREIRO 2  HIZS : 306': range(30646, 30700),
'BEL10  ASAP : 307': range(30700, 30800),
'BEL11  ASAP : 308': range(30800, 30846),
'BEL12  ASAP : 308': range(30846, 30900),
'BEL13  ASAP : 309': range(30900, 31000),
'BEL14  ASAP : 310': range(31000, 31100),
'BEL15  ASAP : 311': range(31100, 31150),
'BEL16  ASAP : 311': range(31150, 31200),
'BEL17  ASAP : 312': range(31200, 31300),
'BEL18  ASAP : 313': range(31300, 31400),
'BEL19  ASAP : 314': range(31400, 31500),
'BEL20  ASAP : 315': range(31500, 31600),
'BEL21  ASAP : 316': range(31600, 31700),
'BEL22  ASAP : 317': range(31700, 31800),
'BEL23  ASAP : 318': range(31800, 31900),
'BEL24  ASAP : 319': range(31900, 32000),
'CON31  CENTRO 1 HIZS : 320': range(32000, 32018),
'CON31  CENTRO 2 HIZS : 320': range(32018, 32044),
'CON31  NOVA CONT HIZS : 320': range(32044, 32070),
'CON31  PETROLANDIA HIZS : 320': range(32070, 32100),
'CON32  HIZS : 321': range(32100, 32200),
'CON33  HIZS : 322': range(32200, 32300),
'CON34  HIZS : 323': range(32300, 32400),
'IB/SA PARTE DE CIMA HIZS : 324': range(32400, 32413),
'IB/SA PARTE DE BAIXO HIZS : 324': range(32413, 32450),
'IB/SA SARZEDO E MARIO CAMPOS HIZS : 324': range(32450, 32480),
'BETI1  HIZS : 325': range(32500, 32600),
'BETI1 CENTRO  1 HIZS : 326': range(32600, 32611),
'BETI1 CENTRO  2 HIZS : 326': range(32612, 32626),
'BETI1 ALTEROSA  HIZS : 326': range(32670, 32675),
'BETI1 CAPELINHA  HIZS : 326': range(32675, 32679),
'BETI1 PETROVALE 1  HIZS : 326': range(32668, 32670),
'BETI1 PETROVALE 2  HIZS : 326': range(32688, 32690),
'BETI1 PTB 1  HIZS : 326': range(32657, 32668),
'BETI1 PTB 2  HIZS : 326': range(32679, 32688),
'BETI1 INDEFINIDO 1  HIZS : 326': range(32626, 32635),
'BETI1 INDEFINIDO 2  HIZS : 326': range(32636, 32639),
'BETI1 INDEFINIDO 3  HIZS : 326': range(32643, 32657),
'BETI1 327  HIZS : 327': range(32700, 32800),
'ESM02  HIZS : 328': range(32800, 32860),
'MJI3  1  HIZS : 329': range(32635, 32636),
'MJI3  2  HIZS : 329': range(32639, 32643),
'MJI3  3  HIZS : 329': range(32900, 33000),
# Adicione mais grupos aqui, se necessário
}

counters = {}
for group_name in groups.keys():
    counters[group_name] = 0

while True:
    # Solicita a entrada do usuário
    num = str(input("Digite o CEP (ou 'exit' p/ sair): "))
    num = num.replace("-", "")

    # Verifica se o usuário quer sair
    if num.lower().strip() == "exit":
        break

    # Verifica se a entrada é válida
    if not num.isnumeric() or len(num) < 5:
        print("Valor inválido! Digite um CEP com 5 dígitos.")
        continue

    # Converte a entrada em um número inteiro de 5 dígitos
    num = int(num[:5])

    # Verifica a qual grupo o número pertence
    group_found = False
    for group_name, group_range in groups.items():
        if num in group_range:
            print(f"\n{num} pertence ao grupo {group_name}\n")
            counters[group_name] += 1
            group_found = True

    # Se a entrada não pertencer a nenhum grupo, imprime mensagem de erro
    if not group_found:
        print(f"Erro: {num} não pertence a nenhum grupo de rotas")

    # Imprime as contagens dos grupos (somente se o contador for maior que zero)
    print("Contagem dos grupos:")
    for group_name, count in counters.items():
        if count > 0:
            print(f"{group_name}: {count}")