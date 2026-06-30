class Ocorrencia:
    """Classe que define a estrutura de dados de uma Ocorrência."""
    def __init__(self, id_ocorrencia, nome_solicitante, tipo, descricao, prioridade, ordem_chegada):
        self.id = int(id_ocorrencia)
        self.nome = str(nome_solicitante)
        self.tipo = str(tipo)
        self.descricao = str(descricao)
        self.prioridade = int(prioridade)
        self.ordem_chegada = int(ordem_chegada)
        self.status = "Aberto"

    def exibir(self):
        print(f"ID: {self.id} | Solicitante: {self.nome} | Tipo: {self.tipo} | "
              f"Prioridade: {self.prioridade} | Ordem: {self.ordem_chegada} | Status: {self.status}")
        print(f"Descrição: {self.descricao}")
        print("-" * 50)


class NodeFila:
    """Nó para a estrutura de Fila Encadeada (Mecanismo Interno)."""
    def __init__(self, ocorrencia):
        self.ocorrencia = ocorrencia
        self.proximo = None


class FilaAtendimento:
    """Implementação manual de uma Fila FIFO (First-In, First-Out)."""
    def __init__(self):
        self.inicio = None
        self.fim = None

    def enqueue(self, ocorrencia):
        """Insere uma ocorrência no fim da fila."""
        novo_no = NodeFila(ocorrencia)
        if self.fim is None:
            self.inicio = self.fim = novo_no
            return
        self.fim.proximo = novo_no
        self.fim = novo_no

    def dequeue(self):
        """Remove e retorna a ocorrência do início da fila (Mais antiga)."""
        if self.inicio is None:
            return None
        
        temp = self.inicio
        self.inicio = self.inicio.proximo
        
        if self.inicio is None:
            self.fim = None
            
        return temp.ocorrencia


class GerenciadorFluxo:
    """Centralizador da Lista Geral (Vetor) e da Fila de Chegada."""
    def __init__(self):
        self.lista_geral = [] 
        self.fila_chegada = FilaAtendimento()

    def adicionar_ocorrencia(self, ocorrencia):
        """Guarda na lista geral e coloca na fila de atendimento."""
        self.lista_geral.append(ocorrencia)
        self.fila_chegada.enqueue(ocorrencia)

    def listar_todas(self):
        """Percorre o vetor e lista todas as ocorrências."""
        if not self.lista_geral:
            print("\n[!] Nenhuma ocorrência cadastrada no sistema.")
            return
        
        print("\n===== LISTAGEM GERAL DE OCORRÊNCIAS =====")
        for oc in self.lista_geral:
            oc.exibir()