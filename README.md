# Sistema de Gerenciamento de Ocorrências Acadêmicas 🏫

Este projeto é uma aplicação de linha de comando desenvolvida para a disciplina de **Algoritmos e Estruturas de Dados II (AED2)**. O objetivo principal é demonstrar a aplicação prática e integrada de diversas estruturas de dados na memória RAM, sem o uso de bancos de dados relacionais.

---

## 🛠️ Organização do Projeto e Divisão de Tarefas

Para evitar conflitos de código e permitir que todos trabalhem em paralelo usando branches no Git, o sistema foi dividido em módulos independentes. A classe central que conecta todas as partes é a `Ocorrencia`.

Abaixo está a descrição detalhada das funções de cada integrante:

### 👤 Integrante 1: O Arquiteto (Menu CLI & Motor da Pilha)
*Responsável por gerenciar a interface com o usuário no terminal e controlar o histórico de ações para a função de desfazer.*

* **Arquivo:** `main.py`
* **Estrutura de Dados:** Pilha (*Stack* - LIFO) implementada de forma manual.
* **Funções e Responsabilidades:**
    * `*class NodePilha:*` *[Integrante 1: criar a estrutura de nó para a pilha encadeada]*
    * `*class PilhaHistorico:*` *[Integrante 1: criar a classe que controla a pilha]*
    * `*PilhaHistorico.push(acao):*` *[Integrante 1: insere uma string de histórico no topo da pilha]*
    * `*PilhaHistorico.pop():*` *[Integrante 1: remove e retorna a última ação do topo (usado no Desfazer)]*
    * `*menu_principal():*` *[Integrante 1: loop com o menu interativo (Opções de 0 a 9) e inputs do terminal]*

---

### 👤 Integrante 2: O Guardião do Fluxo (Registro Geral & Fila)
*Responsável pelo armazenamento central de todas as ocorrências na memória e pelo controle do atendimento cronológico por ordem de chegada.*

* **Arquivo:** `fluxo.py`
* **Estruturas de Dados:** Vetor Dinâmico (Lista Geral) e Fila Encadeada (*Queue* - FIFO).
* **Funções e Responsabilidades:**
    * `Ocorrencia`: Classe molde com os atributos obrigatórios (`id`, `nome`, `tipo`, `descricao`, `prioridade`, `ordem_chegada` e `status`).
    * `Ocorrencia.exibir()`: Formata e exibe todos os dados de uma ocorrência específica na tela.
    * `FilaAtendimento.enqueue(ocorrencia)`: Insere de forma manual um nó com a ocorrência no fim da fila.
    * `FilaAtendimento.dequeue()`: Remove e retorna a ocorrência que está no início da fila (a mais antiga).
    * `GerenciadorFluxo.adicionar_ocorrencia(ocorrencia)`: Salva o objeto na lista geral (vetor) e o envia para a fila de atendimento.
    * `GerenciadorFluxo.listar_todas()`: Varre a lista geral inteira exibindo cada chamado cadastrado.

---

### 👤 Integrante 3: O Indexador e Gerenciador de Prioridade
*Responsável por implementar a busca rápida de ocorrências usando tabela hash e o atendimento por prioridade usando heap.*

#### Tabela Hash

* **Arquivo:** `indice_hash.py`
* **Estrutura de Dados:** Tabela Hash com tratamento de colisões por encadeamento usando lista ligada.
* **Funções e Responsabilidades:**
    * `class NoHash:` cria o nó utilizado no encadeamento das colisões.
    * `funcao_hash(chave):` transforma uma chave textual em um índice da tabela.
    * `inserir_indice(chave, ocorrencia):` insere uma ocorrência na tabela hash usando uma chave.
    * `indexar_ocorrencia(ocorrencia):` indexa a ocorrência pelo nome do solicitante e pelo tipo.
    * `buscar_no_indice(chave):` busca ocorrências associadas a uma chave.
    * `inserir_hash(ocorrencia):` adiciona a ocorrência na tabela hash.
    * `buscar_hash(chave):` retorna as ocorrências encontradas por nome ou tipo.

A tabela hash foi usada para permitir buscas rápidas por nome do solicitante ou por tipo de ocorrência. Ao cadastrar uma ocorrência, ela é inserida na hash usando duas chaves: o nome e o tipo.

#### Heap de Prioridade

* **Arquivo:** `heap_prioridade.py`
* **Estrutura de Dados:** Heap máxima (*Max Heap*), usada como fila de prioridade.
* **Funções e Responsabilidades:**
    * `class HeapPrioridade:` controla a estrutura da heap em memória.
    * `inserir(ocorrencia):` insere uma ocorrência na heap de acordo com sua prioridade.
    * `remover_maior_prioridade():` remove e retorna a ocorrência com maior prioridade.
    * `tem_maior_prioridade(ocorrencia_a, ocorrencia_b):` compara duas ocorrências pela prioridade.
    * `subir(indice):` reorganiza a heap após uma inserção.
    * `descer(indice):` reorganiza a heap após uma remoção.
    * `esta_vazia():` verifica se a heap está vazia.

A heap foi usada para atender primeiro as ocorrências mais críticas. Como a prioridade varia de 1 a 5, a ocorrência com prioridade 5 deve ser atendida antes das ocorrências com prioridade menor. Em caso de empate, a ordem de chegada pode ser usada como critério de desempate.

---

### 👤 Integrante 4: O Mestre dos Algoritmos (Ordenação Manual)
*Responsável por aplicar algoritmos manuais de ordenação sobre os dados armazenados sempre que o usuário solicitar.*

* **Arquivo:** `ordenacao.py`
* **Estrutura de Dados:** Algoritmo de Ordenação por comparação (Bubble Sort, Insertion Sort ou Selection Sort).
* **Funções e Responsabilidades:**
    * `*ordenar_por_id(lista_geral):*` *[Integrante 4: recebe a lista do Integrante 2 e ordena no local (in-place) de forma crescente por ID]*
    * `*ordenar_por_prioridade(lista_geral):*` *[Integrante 4: ordena a lista de forma decrescente pela prioridade (Crítica para Baixa)]*
    * `*ordenar_por_nome(lista_geral):*` *[Integrante 4: ordena a lista em ordem alfabética pelo nome do solicitante]*

---

## 🚀 Como Executar o Projeto

1. Certifique-se de ter o **Python 3** instalado em sua máquina.
2. Baixe ou clone este repositório.
3. Abra o terminal na pasta do projeto e execute o comando:
   ```bash
   python main.py
