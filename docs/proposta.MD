# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na etapa inicial do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com **Python e Pygame** dentro do prazo disponível. Consulte o enunciado publicado no Canvas para conhecer o eixo temático e as orientações vigentes.

## 1. Nome provisório do jogo

Informe o nome provisório do jogo.

**Nome:**

> **DataSnake: Treinando sem Viés**

## 2. Integrantes do grupo

- Nome 1: Guilherme Borges Silva

## 3. Tema escolhido

Indique qual tema específico o grupo escolheu **dentro do eixo temático definido no enunciado**.

**Tema:**

> Vieses e justiça nas decisões: o efeito de dados desequilibrados no treinamento de sistemas de IA.

**Como esse tema se relaciona com o jogo?** Explique brevemente (2 a 4 linhas) como ele aparecerá nos objetivos, nas regras ou nos desafios, e não apenas nas imagens ou no cenário.

> A cobra representa um modelo de IA que "se alimenta" de dados para aprender. Cada dado coletado pertence a uma de três categorias, e o jogo mede continuamente o equilíbrio do dataset. Coletar só a categoria mais fácil deixa o modelo enviesado e leva à derrota; manter o dataset balanceado dá mais pontos e é a condição de vitória. Assim, o uso responsável (dados equilibrados) é a própria regra central do jogo.

## 4. Tipo de jogo

Indique o estilo do jogo. Exemplos: desviar de obstáculos, coleta de itens, labirinto, perguntas e respostas, memória, Pong, Snake, Breakout, corrida ou sobrevivência simples.

**Tipo escolhido:**

> Snake (coleta de itens em grade), com uma regra adicional de equilíbrio entre categorias.

## 5. Descrição geral do jogo

Explique, em poucas linhas, como o jogo funcionará. O que aparece na tela? O que o jogador controla? O que ele precisa fazer e quais desafios encontrará?

**Descrição:**

> A tela mostra uma grade onde o jogador controla uma cobra (o "modelo"). Sempre existem três dados na tela, um de cada categoria (A, B e C), identificados por cor. Ao comer um dado, a cobra cresce, ganha pontos e a contagem daquela categoria aumenta. Um painel lateral mostra a quantidade de dados de cada categoria e uma barra de viés, que sobe conforme o dataset fica desequilibrado. O desafio é planejar a rota: muitas vezes o dado mais próximo é da categoria que já está sobrando, e pegá-lo aumenta o viés. Com o dataset balanceado, os pontos são multiplicados.

## 6. Objetivo do jogador

Descreva o objetivo principal. Por exemplo: coletar itens, sobreviver por determinado tempo, chegar ao final de um percurso ou completar desafios.

**Objetivo:**

> "Treinar" o modelo coletando 30 dados (10 de cada categoria) sem deixar o viés passar do limite e sem bater a cobra, fazendo a maior pontuação possível.

## 7. Regras principais

Liste até cinco regras que expliquem o funcionamento do jogo. Exemplos: o jogador começa com três vidas; acertos somam pontos; colisões retiram vidas.

- Regra 1: A cobra se move continuamente pela grade; as setas mudam a direção (não é permitido inverter o sentido de uma vez).
- Regra 2: Comer um dado faz a cobra crescer um segmento, soma 10 pontos e incrementa a contagem da categoria dele; um novo dado da mesma categoria surge em posição aleatória livre.
- Regra 3: O viés é a diferença entre a categoria com mais dados e a com menos. Se o viés for no máximo 1, o dataset está balanceado e os pontos valem em dobro.
- Regra 4: Se o viés atingir 5, o modelo é considerado enviesado e a partida termina em derrota.
- Regra 5: Bater na borda da tela ou no próprio corpo encerra a partida. A pontuação máxima (recorde) é salva em arquivo.

## 8. Condição de vitória

Explique como o jogador vence ou conclui a partida. Exemplos: alcançar uma pontuação, finalizar uma fase ou completar todas as tarefas.

**Condição de vitória:**

> Coletar 10 dados de cada categoria (30 no total) sem perder. A tela final mostra "Modelo treinado de forma justa!", a pontuação e se o recorde foi batido.

## 9. Condição de derrota ou encerramento

Explique quando a partida termina ou como o jogador perde. Exemplos: esgotar as vidas, acabar o tempo ou atingir o limite de erros.

**Condição de derrota ou encerramento:**

> A partida termina em derrota quando: (1) o viés atinge o limite de 5 ("Modelo enviesado!"); ou (2) a cobra bate na borda ou no próprio corpo ("Treinamento interrompido!"). Também é possível encerrar a qualquer momento com ESC.

## 10. Elementos previstos no jogo

Descreva brevemente os elementos mais importantes, sem precisar detalhar a implementação.

- **Personagem ou elemento principal:** a cobra, que representa o modelo de IA em treinamento.
- **Obstáculos ou desafios:** bordas da tela, o próprio corpo da cobra (que cresce a cada dado) e o limite de viés, que obriga o jogador a não pegar sempre o dado mais próximo.
- **Itens ou objetos de interação (se houver):** dados das categorias A, B e C (três cores diferentes), sempre um de cada na tela.
- **Pontuação, vidas, tempo ou progresso:** pontuação com multiplicador ×2 quando balanceado; contador por categoria (ex.: A 4/10, B 3/10, C 4/10); barra de viés (0 a 5); recorde salvo em arquivo.

## 11. Controles previstos

Informe como o jogador vai interagir com o jogo (por exemplo, setas para movimentar, espaço para agir ou mouse para selecionar).

**Controles:**

> Setas do teclado para mudar a direção da cobra; ENTER para iniciar ou reiniciar a partida; P para pausar; ESC para sair.

## 12. Principais dificuldades esperadas

Cite até três dificuldades que o grupo espera enfrentar. Exemplos: movimentação, colisões, controle de tempo, testes ou uso do GitHub.

- Dificuldade 1: Movimentação da cobra em grade (atualizar a lista de segmentos e impedir a inversão de direção).
- Dificuldade 2: Detecção de colisões (borda, corpo e dados) e geração de novos dados apenas em posições livres.
- Dificuldade 3: Ajustar o balanceamento (velocidade, limite de viés e meta de dados) para que o jogo seja desafiador sem ser frustrante.

## 13. Escopo mínimo para a entrega final

Descreva a **versão mais simples que já seria jogável**, com as interações e regras essenciais. Evite planejar funcionalidades demais.

**Escopo mínimo:**

> Janela do Pygame com a grade, cobra controlada pelas setas, três dados (um por categoria) na tela, crescimento ao comer, contagem por categoria, cálculo e exibição do viés, multiplicador de pontos quando balanceado, derrota por colisão ou por viés, vitória ao completar 10 dados de cada categoria, tela final com pontuação e recorde salvo/lido em arquivo de texto, e testes das funções de lógica.

## 14. Possíveis melhorias, caso haja tempo

Liste até três funcionalidades extras para implementar somente depois que a versão mínima estiver funcionando. Exemplos: sons, fases, ranking, animações ou menu inicial.

- Melhoria 1: "Dado ruidoso" (item cinza que aparece de vez em quando): se for comido, reduz a "precisão" do modelo e tira pontos, reforçando a ideia de qualidade dos dados.
- Melhoria 2: Menu inicial com uma tela curta explicando o que é viés em dados, e ranking dos 5 melhores salvos em arquivo.
- Melhoria 3: Fases com velocidade crescente e limite de viés menor, além de sons ao comer e ao perder.

---

## 15. Organização inicial do código e estruturas de dados

Seção complementar, com os itens pedidos no enunciado para a Entrega 1 (estruturas de dados, organização do código e uso de arquivos).

- **Cobra:** lista de tuplas `(coluna, linha)`, onde o primeiro elemento é a cabeça.
- **Direção:** tupla `(dx, dy)`, por exemplo `(1, 0)` para a direita.
- **Dados na tela:** lista de dicionários, por exemplo `{"categoria": "A", "posicao": (5, 7)}`.
- **Contagem do dataset:** dicionário `{"A": 0, "B": 0, "C": 0}`.
- **Cores e configurações:** dicionário de cores por categoria e constantes (tamanho da grade, velocidade, limite de viés, meta por categoria).

Funções previstas (lógica separada do desenho, para facilitar os testes):

- `mover_cobra(cobra, direcao, cresceu)`: retorna a nova lista de segmentos.
- `colidiu_borda(cabeca, colunas, linhas)` e `colidiu_corpo(cobra)`: retornam `True` ou `False`.
- `gerar_posicao_livre(cobra, dados, colunas, linhas)`: sorteia uma posição não ocupada.
- `calcular_vies(contagem)`: retorna `max - min` das contagens.
- `esta_balanceado(contagem)`: `True` se o viés for no máximo 1.
- `calcular_pontos(contagem)`: retorna 20 se balanceado, senão 10.
- `verificar_vitoria(contagem, meta)` e `verificar_derrota_vies(contagem, limite)`.
- `ler_recorde(caminho)` e `salvar_recorde(caminho, pontos)`.
- Funções de desenho (`desenhar_grade`, `desenhar_cobra`, `desenhar_dados`, `desenhar_painel`) e o loop principal em `main()`.

## 16. Uso de arquivos

- `recorde.txt`: guarda a maior pontuação; lido ao iniciar e atualizado no fim da partida se o recorde for batido. Se o arquivo não existir, o recorde começa em 0.

## 17. Testes planejados

Testes simples (com `assert` ou `pytest`, conforme o template) para as funções de lógica:

- `calcular_vies({"A": 3, "B": 1, "C": 2})` deve retornar `2`.
- `esta_balanceado({"A": 2, "B": 2, "C": 1})` deve retornar `True`; com `{"A": 4, "B": 1, "C": 2}`, `False`.
- `calcular_pontos` deve retornar 20 com o dataset balanceado e 10 caso contrário.
- `colidiu_borda` deve retornar `True` para posições fora da grade e `False` dentro dela.
- `colidiu_corpo` deve detectar quando a cabeça ocupa a mesma posição de outro segmento.
- `mover_cobra` deve manter o tamanho quando não cresce e aumentar 1 quando cresce.
- `verificar_vitoria` deve retornar `True` apenas quando todas as categorias atingem a meta.
- `ler_recorde` deve retornar 0 quando o arquivo não existe.

## 18. Recursos externos

Por enquanto, o jogo usará apenas formas geométricas e fontes padrão do Pygame. Qualquer imagem, som, fonte ou trecho de código externo usado será identificado no `README.md`, com origem e licença quando possível. O uso de ferramentas de IA como apoio no desenvolvimento também será informado no `README.md`.

## 19. Declaração de originalidade

Declaro que esta proposta é original e foi elaborada para este trabalho. A mecânica clássica do Snake é usada como base, mas a regra de equilíbrio entre categorias de dados, o cálculo de viés, o multiplicador por balanceamento e as condições de vitória e derrota ligadas ao viés são criação própria, alinhadas ao tema "IA no Cotidiano e Uso Responsável".

— Guilherme Borges Silva
