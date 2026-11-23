import random


def calcular_vies(contagem):
    """Retorna a diferença entre a categoria com mais dados e a com menos."""
    valores = list(contagem.values())
    return max(valores) - min(valores)


def esta_balanceado(contagem, tolerancia=1):
    """Retorna True se o viés estiver dentro da tolerância."""
    return calcular_vies(contagem) <= tolerancia


def calcular_pontos(contagem, pontos_base=10, pontos_balanceado=20):
    """Retorna quantos pontos o dado vale (o dobro se o dataset estiver balanceado)."""
    if esta_balanceado(contagem):
        return pontos_balanceado
    return pontos_base


def verificar_derrota_vies(contagem, limite):
    """Retorna True se o viés chegou no limite."""
    return calcular_vies(contagem) >= limite


def verificar_vitoria(contagem, meta):
    """Retorna True se todas as categorias chegaram na meta."""
    for quantidade in contagem.values():
        if quantidade < meta:
            return False
    return True


def direcao_valida(atual, nova):
    """Impede a cobra de virar para o lado oposto de uma vez."""
    return nova != (-atual[0], -atual[1])


def calcular_proxima_cabeca(cabeca, direcao):
    """Retorna a próxima posição da cabeça."""
    return (cabeca[0] + direcao[0], cabeca[1] + direcao[1])


def mover_cobra(cobra, direcao, cresceu):
    """Move a cobra uma casa. Se ela não cresceu, tira o último pedaço."""
    nova_cobra = [calcular_proxima_cabeca(cobra[0], direcao)] + cobra
    if not cresceu:
        nova_cobra.pop()
    return nova_cobra


def colidiu_borda(cabeca, colunas, linhas):
    """Retorna True se a cabeça saiu da grade."""
    x, y = cabeca
    return x < 0 or x >= colunas or y < 0 or y >= linhas


def colidiu_corpo(cobra):
    """Retorna True se a cabeça encostou no próprio corpo."""
    return cobra[0] in cobra[1:]


def encontrar_dado(posicao, dados):
    """Retorna o índice do dado nessa posição, ou -1 se não tiver nenhum."""
    for i in range(len(dados)):
        if dados[i]["posicao"] == posicao:
            return i
    return -1


def gerar_posicao_livre(cobra, dados, colunas, linhas):
    """Sorteia uma posição que não tenha cobra nem outro dado."""
    ocupadas = list(cobra)
    for dado in dados:
        ocupadas.append(dado["posicao"])

    livres = []
    for x in range(colunas):
        for y in range(linhas):
            if (x, y) not in ocupadas:
                livres.append((x, y))

    return random.choice(livres)
