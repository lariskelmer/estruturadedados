# Introdução aos Grafos e Assortatividade

Este README fornece uma breve introdução sobre grafos, assortatividade e como o grau dos nós influencia as demais características dos grafos. Também apresenta informações sobre cinco grafos específicos e, no final, inclui um espaço para um dataframe com métricas de grafos.

## Grafos

Um grafo é uma estrutura matemática que consiste em um conjunto de nós (ou vértices) e um conjunto de arestas (ou conexões) que ligam esses nós. Grafos são usados para representar uma variedade de relações e interações em várias áreas, como redes sociais, transporte, circuitos elétricos e muito mais.

## Assortatividade em Grafos

A assortatividade em grafos se refere à tendência de nós com características similares se conectarem uns aos outros. Em outras palavras, nós com graus semelhantes tendem a se ligar. Isso pode influenciar a estrutura e dinâmica de um grafo, afetando a propagação de informações, a resiliência da rede e muito mais.

## Influência do Grau dos Nós

O grau de um nó em um grafo representa o número de arestas conectadas a ele. A distribuição dos graus dos nós em um grafo pode afetar significativamente suas propriedades. Por exemplo, uma rede com uma distribuição de grau mais uniforme pode ser mais resiliente a falhas, enquanto uma rede com nós de alto grau pode ser mais eficiente na propagação de informações.

## Grafos Específicos

### email-Eu-core

Este grafo representa interações de e-mail na comunidade de pesquisa de uma universidade e pode ser encontrado em: [Dataset](https://snap.stanford.edu/data/email-Eu-core.html)

![email-Eu-core](images/email-Eu-core.png)

Com base no gráfico assortatividadeXgrau dos nós é possível afirmar que:

O gráfico é de dispersão e conta com uma linha de regressão, a fim de representar tendências. Nesse gráfico é exibida a relação entre o grau de um nó e o grau médio dos vizinhos desse nó na rede de e-mail de uma grande instituição de pesquisa europeia (assortatividade). A rede foi gerada usando dados de e-mail da instituição, onde existe arestsa (u, v) na rede se a pessoa u enviou, pelo menos, um e-mail para a pessoa v.

A linha de regressão no gráfico aponta para uma correlação positiva entre o grau de um nó e o grau médio dos vizinhos desse nó. Isso sugere que nós com muitas conexões tendem a se conectar com outros com também muitas conexões. Esse fenômeno é uma característica comum em redes com assortatividade positiva.

A dispersão dos pontos indica que há uma variação considerável no grau médio dos vizinhos para um dado grau de nó. Ou seja, há uma parte considerável dos dados que não seguem o padrão da assortatividade mencionada. 

Dessa forma, a análise do gráfico sugere que a rede de e-mail da instituição de pesquisa tem vários padrões de conexão entre seus membros, apesar de ser diversificada. 

### soc-Epinions1

Este grafo descreve interações de avaliação de produtos em uma rede social e pode ter seus dados disponibilizados em: [Dataset](https://snap.stanford.edu/data/soc-Epinions1.html)

![soc-Epinions1](images/soc-Epinions1.png)

Com base no gráfico assortatividadeXgrau dos nós é possível afirmar que 

Esse é um gráfico de dispersão com uma linha de regressão, mostrando a relação entre o grau de um nó e o grau de assortatividade do nó na rede social do site de avaliações de consumidores Epinions.com. A rede é formada por usuários que podem decidir se “confiam” uns nos outros. Essas relações geram, então, a Web de Confiança, que é combinada com as avaliações para determinar quais avaliações serão mostradas ao usuário.

A linha de regressão no gráfico sugere uma correlação quase neutra entre o grau de um nó e a assortatividade desse nó. Ou seja, o coeficiente de assortatividade é quase neutro, indicando que não há uma tendência para que usuários com muitas conexões se conectem com usuários que têm muitas ou poucas conexões. Isso é uma característica de redes com assortatividade próxima de zero e sugere uma estrutura de rede complexa com padrões de conexão variados entre os usuários.

### Wiki-Vote

Este grafo é derivado das votações de administração na Wikipedia e pode ter seus dados disponibilizados em: [Dataset](https://snap.stanford.edu/data/wiki-Vote.html)

![Wiki-Vote](images/wiki-Vote.png)

Com base no gráfico assortatividadeXgrau dos nós é possível afirmar que 

O gráfico representa a relação entre o grau de um nó e o grau de assortatividade desse nó. Nele, há uma tendência positiva no gráfico, o que sugere que os nós com mais conexões (usuários que votaram em muitos outros usuários ou receberam muitos votos) tendem a estar conectados a outros nós com muitas conexões. Isso é uma característica de redes com assortatividade positiva, onde nós de alto grau tendem a se conectar a outros nós de alto grau.

Além disso, a dispersão dos pontos indica que há uma variação considerável no grau médio dos vizinhos para um dado grau de nó. Isso sugere que, embora haja uma tendência geral de assortatividade, também existem muitos nós que não seguem essa tendência.

### twitter_combined

Este grafo representa conexões entre usuários do Twitter e pode ter seus dados disponibilizados em: [Dataset](https://snap.stanford.edu/data/ego-Twitter.html)

![twitter_combined](images/twitter_combined.png)

Com base no gráfico assortatividadeXgrau dos nós é possível afirmar que 

Este é um gráfico de dispersão com uma linha de regressão, mostrando a relação entre o grau de um nó e o coeficiente de assortatividade do Twitter. A rede é formada por usuários que formam círculos (ou listas) e foi gerada a partir de dados públicos do Twitter.

A linha de regressão no gráfico sugere uma correlação quase neutra entre o grau de um nó e o coeficiente de assortatividade. Isso indica que não há uma tendência nítida para usuários com muitas conexões se conectarem com usuários que têm muitas ou poucas conexões. Isso é uma característica de redes com assortatividade próxima de zero.

A dispersão dos pontos indica que há uma variação considerável no coeficiente de assortatividade para um dado grau de nó. Isso sugere que não há uma tendência geral de assortatividade e que a estrutura da rede é complexa e os padrões de conexão variam muito entre os usuários.

### com-youtube

Este grafo modela conexões entre vídeos no YouTube e pode ter seus dados disponibilizados em: ![com-youtube](images/com-youtube.png)

[Dataset](https://snap.stanford.edu/data/com-Youtube.html)

Com base no gráfico assortatividadeXgrau dos nós é possível afirmar que:

O gráfico é de dispersão com uma linha de regressão, mostrando a relação entre o grau de um nó e o coeficiente de assortatividade do YouTube. A rede é formada por usuários que formam amizades e podem criar grupos, nesses grupos outros usuários também podem se juntar. Cada componente conectado em um grupo é considerado uma comunidade distinta.

A linha de regressão no gráfico sugere uma correlação quase neutra entre o grau de um nó e o coeficiente de assortatividade. Isso indica que não há uma tendência clara para usuários com muitas conexões se conectarem com usuários que têm muitas ou poucas conexões. Isso é uma característica de redes com assortatividade próxima de zero.

A dispersão dos pontos indica que há uma variação considerável no coeficiente de assortatividade para um dado grau de nó. Isso sugere que, embora não haja uma tendência geral de assortatividade, a estrutura da rede é complexa e os padrões de conexão variam amplamente entre os usuários.


## Métricas de Grafos

Aqui estão algumas métricas comuns usadas para analisar grafos e suas respectivas descrições:

| Métrica              | Descrição                                         |
|----------------------|---------------------------------------------------|
| Número de Nós       | Total de nós no grafo                            |
| Número de Arestas    | Total de arestas no grafo                         |
| Grau Médio           | Média dos graus dos nós                          |
| Diâmetro             | Maior distância entre dois nós no grafo          |
| Coeficiente de Clustering Médio | Mede a tendência de formação de agrupamentos no grafo |
| Centralidade de Grau | Mede a importância dos nós com base em seu grau  |

Essas métricas ajudam a entender e as características de um grafo e, com base nelas, criou-se a seguinte tabela para analisar os dados acima:

![Métricas](images/df.png)


