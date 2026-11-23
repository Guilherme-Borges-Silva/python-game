import pygame
import src.config as config
from src.dados import carregar_recorde, salvar_recorde
from src.funcoes import (
    calcular_vies,
    esta_balanceado,
    calcular_pontos,
    verificar_derrota_vies,
    verificar_vitoria,
    direcao_valida,
    calcular_proxima_cabeca,
    mover_cobra,
    colidiu_borda,
    colidiu_corpo,
    encontrar_dado,
    gerar_posicao_livre,
)

TECLAS_DIRECAO = {
    pygame.K_UP: (0, -1),
    pygame.K_DOWN: (0, 1),
    pygame.K_LEFT: (-1, 0),
    pygame.K_RIGHT: (1, 0),
}

def novo_jogo(situacao="jogando"):
    """Cria o estado de uma partida nova."""
    meio = config.COLUNAS // 2
    cobra = [(meio, meio), (meio - 1, meio), (meio - 2, meio)]

    dados = []
    contagem = {}
    for categoria in config.CATEGORIAS:
        posicao = gerar_posicao_livre(cobra, dados, config.COLUNAS, config.LINHAS)
        dados.append({"categoria": categoria, "posicao": posicao})
        contagem[categoria] = 0

    return {
        "situacao": situacao,  # inicio, jogando, pausado, vitoria, vies ou colisao
        "cobra": cobra,
        "direcao": (1, 0),
        "proxima_direcao": (1, 0),
        "dados": dados,
        "contagem": contagem,
        "pontos": 0,
    }


def fim_de_jogo(estado):
    """Retorna True se a partida acabou."""
    return estado["situacao"] in ("vitoria", "vies", "colisao")


def tratar_tecla(estado, tecla):
    """Muda o estado do jogo de acordo com a tecla apertada."""
    if tecla == pygame.K_RETURN:
        if estado["situacao"] == "inicio" or fim_de_jogo(estado):
            return novo_jogo()

    elif tecla == pygame.K_p:
        if estado["situacao"] == "jogando":
            estado["situacao"] = "pausado"
        elif estado["situacao"] == "pausado":
            estado["situacao"] = "jogando"

    elif tecla in TECLAS_DIRECAO and estado["situacao"] == "jogando":
        nova = TECLAS_DIRECAO[tecla]
        if direcao_valida(estado["direcao"], nova):
            estado["proxima_direcao"] = nova

    return estado


def dar_um_passo(estado):
    """Anda uma casa com a cobra e aplica as regras do jogo."""
    estado["direcao"] = estado["proxima_direcao"]
    dados = estado["dados"]

    proxima = calcular_proxima_cabeca(estado["cobra"][0], estado["direcao"])
    indice = encontrar_dado(proxima, dados)
    comeu = indice != -1

    estado["cobra"] = mover_cobra(estado["cobra"], estado["direcao"], comeu)

    if colidiu_borda(estado["cobra"][0], config.COLUNAS, config.LINHAS) or colidiu_corpo(estado["cobra"]):
        estado["situacao"] = "colisao"
        return

    if comeu:
        categoria = dados[indice]["categoria"]
        estado["contagem"][categoria] += 1
        estado["pontos"] += calcular_pontos(estado["contagem"], config.PONTOS_BASE, config.PONTOS_BALANCEADO)

        # o dado comido some e aparece outro da mesma categoria
        dados.pop(indice)
        posicao = gerar_posicao_livre(estado["cobra"], dados, config.COLUNAS, config.LINHAS)
        dados.append({"categoria": categoria, "posicao": posicao})

        if verificar_derrota_vies(estado["contagem"], config.LIMITE_VIES):
            estado["situacao"] = "vies"
        elif verificar_vitoria(estado["contagem"], config.META_POR_CATEGORIA):
            estado["situacao"] = "vitoria"


def retangulo_celula(posicao, margem=2):
    """Converte uma posição da grade em um retângulo na tela."""
    x = posicao[0] * config.TAMANHO_CELULA + margem
    y = posicao[1] * config.TAMANHO_CELULA + margem
    tamanho = config.TAMANHO_CELULA - 2 * margem
    return pygame.Rect(x, y, tamanho, tamanho)


def escrever(tela, fonte, texto, cor, x, y, centralizado=False):
    """Escreve um texto na tela."""
    imagem = fonte.render(texto, True, cor)
    if centralizado:
        x = x - imagem.get_width() // 2
    tela.blit(imagem, (x, y))


def desenhar_grade(tela):
    """Desenha o fundo e as linhas da grade."""
    pygame.draw.rect(tela, config.FUNDO_JOGO, (0, 0, config.LARGURA_AREA_JOGO, config.ALTURA_TELA))
    for i in range(config.COLUNAS + 1):
        x = i * config.TAMANHO_CELULA
        pygame.draw.line(tela, config.LINHA_GRADE, (x, 0), (x, config.ALTURA_TELA))
    for i in range(config.LINHAS + 1):
        y = i * config.TAMANHO_CELULA
        pygame.draw.line(tela, config.LINHA_GRADE, (0, y), (config.LARGURA_AREA_JOGO, y))


def desenhar_cobra(tela, cobra):
    """Desenha a cobra."""
    for pedaco in cobra:
        pygame.draw.rect(tela, config.COR_COBRA, retangulo_celula(pedaco))


def desenhar_dados(tela, dados, fonte):
    """Desenha os dados com a cor e a letra da categoria."""
    for dado in dados:
        retangulo = retangulo_celula(dado["posicao"], 4)
        pygame.draw.ellipse(tela, config.CORES_CATEGORIAS[dado["categoria"]], retangulo)
        escrever(tela, fonte, dado["categoria"], config.FUNDO_PAINEL, retangulo.centerx, retangulo.y + 4, True)


def desenhar_painel(tela, estado, recorde, fontes):
    """Desenha o painel da direita com pontos, dataset e viés."""
    x = config.LARGURA_AREA_JOGO + 16
    pygame.draw.rect(tela, config.FUNDO_PAINEL, (config.LARGURA_AREA_JOGO, 0, config.LARGURA_PAINEL, config.ALTURA_TELA))

    escrever(tela, fontes["grande"], "DataSnake", config.BRANCO, x, 16)
    escrever(tela, fontes["media"], "Pontos: " + str(estado["pontos"]), config.BRANCO, x, 64)
    escrever(tela, fontes["media"], "Recorde: " + str(recorde), config.CINZA, x, 92)

    escrever(tela, fontes["media"], "Dataset", config.BRANCO, x, 140)
    y = 172
    for categoria in config.CATEGORIAS:
        pygame.draw.rect(tela, config.CORES_CATEGORIAS[categoria], (x, y + 2, 16, 16))
        texto = categoria + ": " + str(estado["contagem"][categoria]) + "/" + str(config.META_POR_CATEGORIA)
        escrever(tela, fontes["media"], texto, config.BRANCO, x + 26, y)
        y += 30

    # barra de viés
    vies = calcular_vies(estado["contagem"])
    balanceado = esta_balanceado(estado["contagem"], config.TOLERANCIA_BALANCEADO)
    escrever(tela, fontes["media"], "Viés: " + str(vies) + "/" + str(config.LIMITE_VIES), config.BRANCO, x, 278)

    if balanceado:
        cor = config.VERDE
    elif vies < config.LIMITE_VIES - 1:
        cor = config.AMARELO
    else:
        cor = config.VERMELHO

    largura_barra = 186
    preenchido = int(largura_barra * min(vies / config.LIMITE_VIES, 1))
    pygame.draw.rect(tela, config.LINHA_GRADE, (x, 308, largura_barra, 18))
    pygame.draw.rect(tela, cor, (x, 308, preenchido, 18))

    if balanceado:
        escrever(tela, fontes["pequena"], "Balanceado: pontos x2", config.VERDE, x, 336)
    else:
        escrever(tela, fontes["pequena"], "Desequilibrado: pontos x1", config.AMARELO, x, 336)

    controles = ["Setas: mover", "P: pausar", "ENTER: iniciar", "ESC: sair"]
    y = config.ALTURA_TELA - 90
    for linha in controles:
        escrever(tela, fontes["pequena"], linha, config.CINZA, x, y)
        y += 22


def desenhar_mensagem(tela, fontes, linhas):
    """Desenha uma caixa no meio da tela com as linhas de texto. Cada linha é (texto, cor)."""
    altura = 40 + 36 * len(linhas)
    caixa = pygame.Rect(30, (config.ALTURA_TELA - altura) // 2, config.LARGURA_AREA_JOGO - 60, altura)
    pygame.draw.rect(tela, config.FUNDO_PAINEL, caixa)
    pygame.draw.rect(tela, config.LINHA_GRADE, caixa, 2)

    y = caixa.y + 24
    for texto, cor in linhas:
        escrever(tela, fontes["media"], texto, cor, caixa.centerx, y, True)
        y += 36


def desenhar_tela(tela, estado, recorde, fontes):
    """Desenha tudo de acordo com a situação da partida."""
    desenhar_grade(tela)
    desenhar_dados(tela, estado["dados"], fontes["pequena"])
    desenhar_cobra(tela, estado["cobra"])
    desenhar_painel(tela, estado, recorde, fontes)

    situacao = estado["situacao"]
    placar = "Pontos: " + str(estado["pontos"]) + "   Recorde: " + str(recorde)

    if situacao == "inicio":
        desenhar_mensagem(tela, fontes, [
            ("Colete os dados A, B e C de forma equilibrada", config.BRANCO),
            ("ENTER para começar", config.VERDE),
        ])
    elif situacao == "pausado":
        desenhar_mensagem(tela, fontes, [("Pausado (P para continuar)", config.BRANCO)])
    elif situacao == "vitoria":
        desenhar_mensagem(tela, fontes, [
            ("Modelo treinado de forma justa!", config.VERDE),
            (placar, config.BRANCO),
            ("ENTER para jogar de novo", config.CINZA),
        ])
    elif situacao == "vies":
        desenhar_mensagem(tela, fontes, [
            ("Modelo enviesado! Dataset desequilibrado.", config.VERMELHO),
            (placar, config.BRANCO),
            ("ENTER para jogar de novo", config.CINZA),
        ])
    elif situacao == "colisao":
        desenhar_mensagem(tela, fontes, [
            ("A cobra bateu! Treinamento interrompido.", config.VERMELHO),
            (placar, config.BRANCO),
            ("ENTER para jogar de novo", config.CINZA),
        ])


def executar_jogo():
    """Abre a janela e roda o loop principal do jogo."""
    pygame.init()
    tela = pygame.display.set_mode((config.LARGURA_TELA, config.ALTURA_TELA))
    pygame.display.set_caption(config.TITULO_JOGO)
    relogio = pygame.time.Clock()

    fontes = {
        "grande": pygame.font.Font(None, 40),
        "media": pygame.font.Font(None, 28),
        "pequena": pygame.font.Font(None, 22),
    }

    recorde = carregar_recorde(config.CAMINHO_RECORDE)
    estado = novo_jogo("inicio")
    ultimo_passo = pygame.time.get_ticks()
    rodando = True

    while rodando:
        relogio.tick(config.FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False
                else:
                    estado = tratar_tecla(estado, evento.key)

        # a cobra anda em intervalos fixos, não a cada quadro
        agora = pygame.time.get_ticks()
        if estado["situacao"] == "jogando" and agora - ultimo_passo >= config.INTERVALO_MOVIMENTO_MS:
            ultimo_passo = agora
            dar_um_passo(estado)

            if fim_de_jogo(estado) and estado["pontos"] > recorde:
                recorde = estado["pontos"]
                salvar_recorde(config.CAMINHO_RECORDE, recorde)

        desenhar_tela(tela, estado, recorde, fontes)
        pygame.display.flip()

    pygame.quit()
