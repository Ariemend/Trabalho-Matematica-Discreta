# Trabalho matemática discreta 2026.2
A ideia desse trabalho é implementar um sistema de grafos, permitindo o calculo dos caminhos entre os pontos especificados pelo usuário,
além de demonstrar a complexidade do problema com cada operação realizada. Abaixo irei falar sobre a estrutura do programa e como operá-lo.
## Inserção dos pontos
Os pontos são lidos diretamente do arquivo "instancia-cidades.txt", seguindo o formato especificado pelo professor, não existe limite sobre a quantidade de
pontos que podem ser inseridos, porém, grandes quantidades de pontos podem causar demora nos cálculos, visto que python não é uma linguagem muito rápida.
## Definição das conexões
A primeira opção do menu é "Gerenciar as conexões entre pontos", ao entrar nesse sub-menu, você terá 4 opções, elas são:
**1."Todos os pontos conectados entre si"**: Relaciona todos os pontos com todos os outros pontos.

**2."Criar conexões manuais"**: Permite que o usuário crie as proprias conexões uma a uma.

**3."Apagar as conexões de um ponto**: Deleta todas as conexões que um ponto possui.

**4."Apagar todas as conexões**: Deleta todas as conexões de todos os pontos.

Essas 4 operações são uma das partes vitais do programa, possibilitando a criação de relações entre os pontos.

## Encontrando caminhos
A outra operação vital desse programa está presente no menu 2, que permite calcular todos os caminhos de um ponto ao outro. Os caminhos tem tamanho
limitado, que é definido pelo usuário, tudo isso gera diversos resultados dependendo das relações inseridas pelo usuário. Além disso, o programa calcula
automaticamente a complexidade do problema, e exibe ao usuário antes de aprensentar quaiquer resultado.

## Menus complementares
Os outros menus servem apenas para permitir que o usuário veja o estado em que o programa está naquele momento, além de contextualizar em algumas
informações, como distância.

## Como Rodar
O programa pode ser acessado rodando o arquivo "main.py".
