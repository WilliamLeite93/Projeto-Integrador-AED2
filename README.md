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

### 👤 Integrante 3: O Indexador (Tabela Hash Customizada)
*Responsável por criar um índice remissivo em memória para permitir a busca instantânea de ocorrências através de textos.*

* **Arquivo:** `hash_table.py`
* **Estrutura de Dados:** Tabela Hash com tratamento de colisões por Encadeamento (Lista Encadeada).
* **Funções e Responsabilidades:**
    * `*class NodeHash:*` *[Integrante 3: criar o nó para a lista encadeada de colisões]*
    * `*TabelaHash._funcao_hash(chave):*` *[Integrante 3: método interno para transformar a string (Nome/Tipo) em um índice numérico]*
    * `*TabelaHash.inserir(chave, ocorrencia):*` *[Integrante 3: associa a ocorrência ao índice correto na tabela]*
    * `*TabelaHash.buscar(chave):*` *[Integrante 3: busca e retorna a lista de ocorrências vinculadas àquela chave]*

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