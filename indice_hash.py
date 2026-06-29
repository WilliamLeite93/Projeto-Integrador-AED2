TAMANHO_TABELA = 10
tabela_hash = [None] * TAMANHO_TABELA


class NoHash:
    def __init__(self, chave, ocorrencia):
        self.chave = chave
        self.ocorrencia = ocorrencia
        self.proximo = None


def funcao_hash(chave):
    chave = str(chave).lower().strip()
    valor = 0

    for caractere in chave:
        valor += ord(caractere)

    return valor % len(tabela_hash)


def inserir_indice(chave, ocorrencia):
    chave = str(chave).lower().strip()
    indice = funcao_hash(chave)

    novo_no = NoHash(chave, ocorrencia)

    if tabela_hash[indice] is None:
        tabela_hash[indice] = novo_no
    else:
        atual = tabela_hash[indice]

        while atual.proximo is not None:
            atual = atual.proximo

        atual.proximo = novo_no


def indexar_ocorrencia(ocorrencia):
    inserir_indice(ocorrencia["nome"], ocorrencia)
    inserir_indice(ocorrencia["tipo"], ocorrencia)


def buscar_no_indice(chave):
    chave_busca = str(chave).lower().strip()
    indice = funcao_hash(chave_busca)

    resultados = []
    atual = tabela_hash[indice]

    while atual is not None:
        chave_atual = str(atual.chave).lower().strip()

        if chave_atual == chave_busca:
            resultados.append(atual.ocorrencia)

        atual = atual.proximo

    return resultados


def inserir_hash(ocorrencia):
    indexar_ocorrencia(ocorrencia)


def buscar_hash(chave):
    return buscar_no_indice(chave)

"""
Onde foi usada a HashTable?
A Hashtable foi utilizada na funcionalidade de busca rápida de ocorrências por nome do solicitante ou tipo de ocorrência.
No cadastro da ocorrência, ela é inserida na tabela hash duas vezes, uma utilizando o nome como chave e a segunda como tipo.
Caso dê coalisão, ela é tratada por encadeamento, utilizando lista ligada de nós naquela posição. Na busca, o sistema calcula
novamente o índice da chave pesquisa e percorre apenas a lista daquele índice.
""" 