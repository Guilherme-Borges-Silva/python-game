"""Testes das funções de lógica do DataSnake (src/funcoes.py e src/dados.py)."""
from src.funcoes import (
    calcular_vies,
    esta_balanceado,
    calcular_pontos,
    verificar_derrota_vies,
    verificar_vitoria,
    direcao_valida,
    mover_cobra,
    colidiu_borda,
    colidiu_corpo,
    encontrar_dado,
    gerar_posicao_livre,
)
from src.dados import carregar_recorde, salvar_recorde


# Viés e pontuação

def test_calcular_vies():
    """O viés é a diferença entre a maior e a menor contagem."""
    assert calcular_vies({"A": 3, "B": 1, "C": 2}) == 2


def test_vies_zero_com_dataset_vazio():
    """No início da partida o viés deve ser zero."""
    assert calcular_vies({"A": 0, "B": 0, "C": 0}) == 0


def test_esta_balanceado_verdadeiro():
    """Diferença de 1 ainda é considerada balanceada."""
    assert esta_balanceado({"A": 2, "B": 2, "C": 1}) is True


def test_esta_balanceado_falso():
    """Diferença maior que 1 não é balanceada."""
    assert esta_balanceado({"A": 4, "B": 1, "C": 2}) is False


def test_calcular_pontos_balanceado_vale_dobro():
    """Com o dataset balanceado o dado vale 20 pontos."""
    assert calcular_pontos({"A": 1, "B": 1, "C": 0}) == 20


def test_calcular_pontos_desequilibrado():
    """Com o dataset desequilibrado o dado vale 10 pontos."""
    assert calcular_pontos({"A": 3, "B": 0, "C": 1}) == 10


def test_derrota_por_vies_no_limite():
    """Atingir o limite de viés encerra a partida."""
    assert verificar_derrota_vies({"A": 5, "B": 0, "C": 2}, 5) is True


def test_sem_derrota_abaixo_do_limite():
    """Abaixo do limite o jogo continua."""
    assert verificar_derrota_vies({"A": 4, "B": 0, "C": 2}, 5) is False


def test_vitoria_quando_todas_categorias_na_meta():
    """Vence quando todas as categorias atingem a meta."""
    assert verificar_vitoria({"A": 10, "B": 10, "C": 10}, 10) is True


def test_sem_vitoria_com_categoria_abaixo_da_meta():
    """Não vence se alguma categoria ainda não atingiu a meta."""
    assert verificar_vitoria({"A": 10, "B": 9, "C": 10}, 10) is False


# Movimento e colisões

def test_direcao_oposta_nao_e_valida():
    """A cobra não pode inverter o sentido de uma vez."""
    assert direcao_valida((1, 0), (-1, 0)) is False


def test_direcao_perpendicular_e_valida():
    """Virar para cima ou para baixo andando para a direita é permitido."""
    assert direcao_valida((1, 0), (0, -1)) is True


def test_mover_cobra_sem_crescer_mantem_tamanho():
    """Sem comer, a cobra anda e mantém o tamanho."""
    cobra = [(5, 5), (4, 5), (3, 5)]
    nova = mover_cobra(cobra, (1, 0), cresceu=False)
    assert nova == [(6, 5), (5, 5), (4, 5)]


def test_mover_cobra_crescendo_aumenta_um():
    """Ao comer, a cobra cresce um segmento."""
    cobra = [(5, 5), (4, 5), (3, 5)]
    nova = mover_cobra(cobra, (1, 0), cresceu=True)
    assert len(nova) == 4
    assert nova[0] == (6, 5)


def test_colidiu_borda_fora_da_grade():
    """Posições fora da grade são colisão."""
    assert colidiu_borda((-1, 5), 20, 20) is True
    assert colidiu_borda((20, 5), 20, 20) is True


def test_nao_colidiu_borda_dentro_da_grade():
    """Posições dentro da grade não são colisão."""
    assert colidiu_borda((0, 0), 20, 20) is False
    assert colidiu_borda((19, 19), 20, 20) is False


def test_colidiu_corpo():
    """A cabeça na mesma posição de outro segmento é colisão."""
    assert colidiu_corpo([(5, 5), (6, 5), (6, 6), (5, 6), (5, 5)]) is True


def test_nao_colidiu_corpo():
    """Cobra em linha reta não colide consigo mesma."""
    assert colidiu_corpo([(5, 5), (4, 5), (3, 5)]) is False


# Dados (itens) 

def test_encontrar_dado_existente():
    """Retorna o índice do dado na posição informada."""
    dados = [{"categoria": "A", "posicao": (1, 1)}, {"categoria": "B", "posicao": (2, 2)}]
    assert encontrar_dado((2, 2), dados) == 1


def test_encontrar_dado_inexistente():
    """Retorna -1 quando não há dado na posição."""
    dados = [{"categoria": "A", "posicao": (1, 1)}]
    assert encontrar_dado((9, 9), dados) == -1


def test_gerar_posicao_livre_nao_sobrepoe():
    """A posição sorteada não pode estar ocupada (grade 2x2 com 3 casas ocupadas)."""
    cobra = [(0, 0), (1, 0)]
    dados = [{"categoria": "A", "posicao": (0, 1)}]
    assert gerar_posicao_livre(cobra, dados, 2, 2) == (1, 1)


# Arquivo de recorde

def test_carregar_recorde_arquivo_inexistente(tmp_path):
    """Sem arquivo, o recorde começa em 0."""
    assert carregar_recorde(tmp_path / "nao_existe.txt") == 0


def test_salvar_e_carregar_recorde(tmp_path):
    """O valor salvo deve ser lido de volta."""
    caminho = tmp_path / "recorde.txt"
    salvar_recorde(caminho, 150)
    assert carregar_recorde(caminho) == 150
