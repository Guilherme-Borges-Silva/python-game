# DataSnake: Treinando sem Viés

Projeto final da disciplina de Introdução a Algoritmos, desenvolvido com Python e Pygame.

Tema: **IA no Cotidiano e Uso Responsável**, com o recorte **vieses e justiça nas decisões** (efeito de dados desequilibrados no treinamento de sistemas de IA).

## Integrantes do grupo

- Guilherme Borges Silva

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo.
  - `jogo.py`: loop principal, eventos, atualização do estado e desenho.
  - `config.py`: constantes (grade, cores, regras e caminhos).
  - `funcoes.py`: funções puras de regra (viés, pontuação, movimento, colisões).
  - `dados.py`: leitura e gravação do recorde.
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes (`recorde.txt`).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo a proposta inicial.

## Descrição do jogo

O jogador controla uma cobra que representa um **modelo de IA em treinamento**. Na grade sempre existem três dados, um de cada categoria (A, B e C, identificados por cor). Ao comer um dado, a cobra cresce, ganha pontos e a contagem daquela categoria no dataset aumenta. Um painel lateral mostra a contagem de cada categoria e uma **barra de viés**. Pegar sempre o dado mais próximo deixa o dataset desequilibrado e o modelo enviesado; por isso o jogador precisa planejar a rota para coletar as três categorias de forma equilibrada.

## Objetivo do jogador

Treinar o modelo de forma justa: coletar 10 dados de cada categoria (30 no total) sem deixar o viés chegar ao limite e sem bater a cobra, fazendo a maior pontuação possível.

## Regras do jogo

- A cobra anda sozinha; as setas mudam a direção (não é possível inverter o sentido de uma vez).
- Cada dado coletado faz a cobra crescer e soma pontos; um novo dado da mesma categoria aparece em outro lugar.
- O viés é a diferença entre a categoria com mais dados e a com menos. Com viés de no máximo 1 (dataset balanceado), o dado vale 20 pontos; caso contrário, vale 10.
- Se o viés chegar a 5, o modelo fica enviesado e a partida termina em derrota.
- Bater na borda ou no próprio corpo encerra a partida.
- Coletar 10 dados de cada categoria é a vitória. O recorde é salvo em `data/recorde.txt`.

## Controles

- Setas: mudar a direção da cobra
- ENTER: iniciar / jogar de novo
- P: pausar / continuar
- ESC: sair do jogo

## Como executar o projeto

```bash
git clone LINK_DO_REPOSITORIO
cd NOME_DA_PASTA
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Situação atual (Entrega 2 – versão parcial)

Já implementado:

- Janela do Pygame, loop principal e tela inicial.
- Movimento da cobra em grade com as setas, pausa e reinício.
- Três dados (A, B, C) na tela, crescimento e geração em posição livre.
- Contagem do dataset, cálculo do viés, barra de viés e multiplicador de pontos.
- Derrota por viés e por colisão, vitória ao completar a meta.
- Recorde salvo e lido em arquivo.
- Testes das funções de lógica em `tests/test_logica.py`.

Próximos passos (se houver tempo): dado ruidoso, ranking dos 5 melhores, fases com velocidade crescente e sons.

## Recursos externos

- Gráficos feitos apenas com formas do Pygame e a fonte padrão do Pygame.
- Ferramentas de IA (Claude) foram usadas como apoio na elaboração da proposta e do código; o código foi revisado e adaptado pelo autor.
