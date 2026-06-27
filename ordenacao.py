def _obter_valor(ocorrencia, campo):
    if isinstance(ocorrencia, dict):
        return ocorrencia.get(campo)
    return getattr(ocorrencia, campo, None)


def _chave_id(ocorrencia):
    valor = _obter_valor(ocorrencia, "id")
    try:
        return (0, int(valor))
    except (TypeError, ValueError):
        return (1, str(valor).strip().lower())


def _chave_nome(ocorrencia):
    valor = _obter_valor(ocorrencia, "nome")
    return str(valor or "").strip().lower()


def _chave_prioridade(ocorrencia):
    valor = _obter_valor(ocorrencia, "prioridade")
    try:
        return int(valor)
    except (TypeError, ValueError):
        return 0


def _deve_trocar(atual, proximo, criterio, decrescente=False):
    chave_atual = criterio(atual)
    chave_proximo = criterio(proximo)

    if decrescente:
        return chave_atual < chave_proximo
    return chave_atual > chave_proximo


def _bubble_sort(lista_geral, criterio, decrescente=False):
    tamanho = len(lista_geral)

    for fim in range(tamanho - 1, 0, -1):
        trocou = False

        for indice in range(fim):
            if _deve_trocar(
                lista_geral[indice],
                lista_geral[indice + 1],
                criterio,
                decrescente,
            ):
                lista_geral[indice], lista_geral[indice + 1] = (
                    lista_geral[indice + 1],
                    lista_geral[indice],
                )
                trocou = True

        if not trocou:
            break

    return lista_geral


def ordenar_por_id(lista_geral):
    """Ordena a lista geral no local pelo ID em ordem crescente."""
    return _bubble_sort(lista_geral, _chave_id)


def ordenar_por_nome(lista_geral):
    """Ordena a lista geral no local pelo nome em ordem alfabetica."""
    return _bubble_sort(lista_geral, _chave_nome)


def ordenar_por_prioridade(lista_geral):
    """Ordena a lista geral no local pela maior prioridade primeiro."""
    return _bubble_sort(lista_geral, _chave_prioridade, decrescente=True)
