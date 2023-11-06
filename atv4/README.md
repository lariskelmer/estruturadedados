# Introdução aos Grafos e Assortatividade

Este README fornece uma breve introdução sobre grafos, assortatividade e como o grau dos nós influencia as demais características dos grafos. Também apresenta informações sobre cinco grafos específicos e, no final, inclui um espaço para um dataframe com métricas de grafos.

## Grafos

Um grafo é uma estrutura matemática que consiste em um conjunto de nós (ou vértices) e um conjunto de arestas (ou conexões) que ligam esses nós. Grafos são usados para representar uma variedade de relações e interações em várias áreas, como redes sociais, transporte, circuitos elétricos e muito mais.

## Assortatividade em Grafos

A assortatividade em grafos se refere à tendência de nós com características semelhantes se conectarem uns aos outros. Em outras palavras, nós com graus semelhantes tendem a se ligar. Isso pode influenciar a estrutura e dinâmica de um grafo, afetando a propagação de informações, a resiliência da rede e muito mais.

## Influência do Grau dos Nós

O grau de um nó em um grafo representa o número de arestas conectadas a ele. A distribuição dos graus dos nós em um grafo pode afetar significativamente suas propriedades. Por exemplo, uma rede com uma distribuição de grau mais uniforme pode ser mais resiliente a falhas, enquanto uma rede com nós de alto grau pode ser mais eficiente na propagação de informações.

## Grafos Específicos

### email-Eu-core

![email-Eu-core](images/email-Eu-core.png)

Este grafo representa interações de e-mail na comunidade de pesquisa de uma universidade.

### soc-Epinions1

![soc-Epinions1](images/soc-Epinions1.png)

Este grafo descreve interações de avaliação de produtos em uma rede social.

### Wiki-Vote

![Wiki-Vote](images/Wiki-Vote.png)

Este grafo é derivado das votações de administração na Wikipedia.

### twitter_combined

![twitter_combined](images/twitter_combined.png)

Este grafo representa conexões entre usuários do Twitter.

### com-youtube

![com-youtube](images/com-youtube.png)

Este grafo modela conexões entre vídeos no YouTube.

## Métricas de Grafos

Aqui estão algumas métricas comuns usadas para analisar grafos:

| Métrica              | Descrição                                         |
|----------------------|---------------------------------------------------|
| Número de Nós       | Total de nós no grafo                            |
| Número de Arestas    | Total de arestas no grafo                         |
| Grau Médio           | Média dos graus dos nós                          |
| Diâmetro             | Maior distância entre dois nós no grafo          |
| Coeficiente de Clustering Médio | Mede a tendência de formação de agrupamentos no grafo |
| Centralidade de Grau | Mede a importância dos nós com base em seu grau  |

Estas métricas ajudam a entender a topologia e as características de um grafo.

Este README.md fornece uma visão geral de grafos, assortatividade e grafos específicos, bem como uma tabela para incluir métricas de grafos. Você pode adicionar as métricas específicas de cada grafo na tabela conforme necessário.
