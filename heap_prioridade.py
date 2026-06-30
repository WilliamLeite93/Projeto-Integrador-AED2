def obter_valor(ocorrencia, campo):
    if isinstance(ocorrencia, dict):
        return ocorrencia.get(campo)
    return getattr(ocorrencia, campo, None)

class HeapPrioridade:
    def __init__(self):
        self.dados = []

    def esta_vazia(self):
        return len(self.dados) == 0
    
    def tem_maior_prioridade(self, ocorrencia_a, ocorrencia_b):
        prioridade_a = int(obter_valor(ocorrencia_a, "prioridade"))
        prioridade_b = int(obter_valor(ocorrencia_b, "prioridade"))

        if prioridade_a > prioridade_b:
            return True
        
        if prioridade_a < prioridade_b:
            return False
        
        ordem_a = int(obter_valor(ocorrencia_a, "ordem_chegada"))
        ordem_b = int(obter_valor(ocorrencia_b, "ordem_chegada"))

        return ordem_a < ordem_b
    
    def inserir(self, ocorrencia):
        self.dados.append(ocorrencia)
        self.subir(len(self.dados) - 1)

    def remover_maior_prioridade(self):
        if self.esta_vazia():
            return None
        
        ocorrencia_prioritaria = self.dados[0]
        ultima_ocorrencia = self.dados.pop()
        
        if not self.esta_vazia():
            self.dados[0] = ultima_ocorrencia
            self.descer(0)

        return ocorrencia_prioritaria
    
    def subir(self, indice):
        while indice > 0:
            indice_pai = (indice - 1) // 2

            if self.tem_maior_prioridade(self.dados[indice], self.dados[indice_pai]):
                self.dados[indice], self.dados[indice_pai] = (
                    self.dados[indice_pai],
                    self.dados[indice]
                )
                indice = indice_pai
            else:
                break

    def descer(self, indice):
        tamanho = len(self.dados)

        while True:
            indice_esquerda = 2 * indice + 1
            indice_direita = 2 * indice + 2
            indice_maior = indice

            if(
                indice_esquerda < tamanho
                and self.tem_maior_prioridade(
                    self.dados[indice_esquerda],
                    self.dados[indice_maior]
                )
            ):
                indice_maior = indice_esquerda

            if(
                indice_direita < tamanho
                and self.tem_maior_prioridade(
                    self.dados[indice_direita],
                    self.dados[indice_maior]
                )
            ):
                indice_maior = indice_direita
            
            if indice_maior != indice:
                self.dados[indice], self.dados[indice_maior] = (
                    self.dados[indice_maior],
                    self.dados[indice]
                )
                indice = indice_maior
            else:
                break

'''
# A heap é usada como fila de prioridade
# Ela atende primeiro a ocorrência com maior prioridade.
# Segye a prioridade de 5 a 1. Em caso de empate ,a ordem de chegada pode ser como desempate.
'''