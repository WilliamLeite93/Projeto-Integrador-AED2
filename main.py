from indice_hash import inserir_hash, buscar_hash

MAX_HISTORICO = 100
historico_pilha = [None] * MAX_HISTORICO
topo = -1

ocorrencias = []

fila = []
fila_inicio = 0

HASH_TAM = 10
tabela_hash = [[] for _ in range(HASH_TAM)]
contador_colisoes = 0

proximo_ordem = 1

def adicionar_ao_historico(acao):
    global topo
    if topo >= MAX_HISTORICO - 1:
        print("Pilha de histórico cheia!")
        return
    topo += 1
    historico_pilha[topo] = acao

def exibir_historico():
    global topo
    print("\n HISTÓRICO DE AÇÕES")
    if topo == -1:
        print("Nenhuma ação registrada.")
        return
    for i in range(topo, -1, -1):
        print(f"{topo - i + 1}. {historico_pilha[i]}")

def desfazer_ultima_acao():
    global topo
    print("\n DESFAZER ÚLTIMA AÇÃO")
    if topo == -1:
        print("Não há ações para desfazer.")
        return
    ultima_acao = historico_pilha[topo]
    historico_pilha[topo] = None
    topo -= 1
    print(f"Ação desfeita -> [{ultima_acao}]")

def gerar_id(nome):
    soma = sum(ord(letra) for letra in nome)
    return nome[:3].upper() + "-" + str(soma % 10000)

def inserir_fila(ocorrencia):
    pass

def listar_todas():
    pass

def atender_fila():
    pass

def buscar_por_hash():
    pass

def ordenar_lista_manual():
    pass

def gerar_massa_testes():
    pass

def cadastrar_ocorrencia():
    print("\nCADASTRAR OCORRÊNCIA")
    nome = input("Nome do requisitante: ")
    tipo = input("Tipo da ocorrência: ")
    descricao = input("Descrição: ")
    while True:
        try:
            prioridade = int(input("Prioridade de 1 a 5: "))
            if 1 <= prioridade <= 5:
                break
            print("Prioridade inválida! Digite um valor entre 1 e 5.")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro entre 1 e 5.")
    id_ocorrencia = gerar_id(nome)
    ocorrencia = {
        "id": id_ocorrencia,
        "nome": nome,
        "tipo": tipo,
        "descricao": descricao,
        "prioridade": prioridade,
        "ordem_chegada": proximo_ordem,
        "status": "Aberto"
    }
    global proximo_ordem
    proximo_ordem += 1
    ocorrencias.append(ocorrencia)
    inserir_fila(ocorrencia)
    inserir_hash(ocorrencia)
    print("\nOcorrência cadastrada com sucesso!")
    print(f"ID gerado: {id_ocorrencia}")
    adicionar_ao_historico(f"Cadastro da ocorrência ID {id_ocorrencia}")

def iniciar_sistema():
    print("Inicializando Sistema de Gerenciamento de Ocorrências Acadêmicas\n")
    while True:
        print("="*40)
        print("   SISTEMA DE OCORRÊNCIAS ACADÊMICAS")
        print("="*40)
        print("1 - Cadastrar ocorrência")
        print("2 - Listar ocorrências")
        print("3 - Atender próxima (Fila FIFO)")
        print("4 - Buscar por Nome/Tipo (Hash Table)")
        print("5 - Ordenar ocorrências")
        print("6 - Gerar massa de testes")
        print("7 - Ver histórico de ações")
        print("8 - Desfazer última ação")
        print("0 - Sair")
        print("="*40)
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar_ocorrencia()
        elif opcao == "2":
            listar_todas()
        elif opcao == "3":
            atender_fila()
            adicionar_ao_historico("Atendimento via fila realizado")
        elif opcao == "4":
            buscar_por_hash()
        elif opcao == "5":
            ordenar_lista_manual()
        elif opcao == "6":
            gerar_massa_testes()
        elif opcao == "7":
            exibir_historico()
        elif opcao == "8":
            desfazer_ultima_acao()
        elif opcao == "0":
            print("\nEncerrando o sistema. Até logo!")
            break
        else:
            print("\nOpção inválida!")

if __name__ == "__main__":
    iniciar_sistema()
