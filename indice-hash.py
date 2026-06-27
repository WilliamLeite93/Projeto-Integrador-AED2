TAMANHO_TABELA = 10
tabela_hash = [None] * TAMANHO_TABELA

class NoHash:
    def __init__(self, chave, ocorrencia):
        self.chave = chave
        self.ocorencia = ocorrencia
        self.proximo = None

def funcao_hash(chave):
    chave = chave.lower().strip()
    valor = 0

    for letra in chave:
        valor += ord(letra)

    return valor % len(tabela_hash)

def inserir(chave, ocorrencia):
    indice = funcao_hash(chave)

    novo_no = NoHash(chave, ocorrencia)
    
    if tabela_hash[indice] is None:
        tabela_hash[indice] = novo_no
    else:
        atual = tabela_hash[indice]

        while atual.proximo is not None:
            atual = atual.proximo
        
        atual.proximo = novo_no

def buscar_hash(chave):
    pass

def buscar_por_tipo(tipo):
    pass