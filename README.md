<h1 align="center">
    <br>
      Processamento Digital de Imagem com Filtro de Sobel
    <br>
</h1>

<h4 align="center">
  Detecção de arestas em imagens usando Filtro de Sobel com derivadas.
</h4>

<p align="center">
  <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/joaoeliandro/filtro-sobel-pdi.svg">

  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/joaoeliandro/filtro-sobel-pdi.svg">

  <a href="https://www.codacy.com/app/joaoeliandro/filtro-sobel-pdi?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=joaoeliandro/filtro-sobel-pdi&amp;utm_campaign=Badge_Grade">
    <img alt="Codacy grade" src="https://api.codacy.com/project/badge/Grade/691b85e51bf240b997ae6ff82ea41590">
  </a>

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/joaoeliandro/filtro-sobel-pdi.svg">
  <a href="https://github.com/joaoeliandro/filtro-sobel-pdi/commits/master">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/joaoeliandro/filtro-sobel-pdi.svg">
  </a>

  <a href="https://github.com/joaoeliandro/filtro-sobel-pdi/issues">
    <img alt="Repository issues" src="https://img.shields.io/github/issues/joaoeliandro/filtro-sobel-pdi.svg">
  </a>

  <a href="https://github.com/joaoeliandro/filtro-sobel-pdi/blob/master/LICENSE">
    <img alt="GitHub License" src="https://img.shields.io/github/license/joaoeliandro/filtro-sobel-pdi.svg">
  </a>
</p>

<p align="center">
  <a href="#octocat-demo">Demo</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#rocket-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#information_source-referências">Referências</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#memo-licença">Licença</a>
</p>

## Sobre

**Detectando arestas usando Filtro de Sobel e derivadas com python**
> Para detecção de arestas, seguimos alguns conceitos para entendimento. Alguns conceitos utilizamos Image Gradient onde há algumas derivações como o Filtro de Sobel e Filtro de Prewitt para algumas instancias de processamento de imagem.

### Guia

| Prewitt  | Sobel  |
|:---:|:---:|
| <a href="#sobre-prewitt">Sobre</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;  | <a href="#sobre-sobel">Sobre</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;  |
| <a href="#formulação-prewitt">Formulação</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;  | <a href="#formulação-sobel">Formulação</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;  |

#### Sobre Prewitt

> O operador de Prewitt é usado no processamento de imagem, particularmente na detecção de borda algoritmos. Tecnicamente, é uma operador de diferença, calcular uma aproximação do gradiente da imagem de intensidade de função. Em cada ponto da imagem, o resultado do operador de Prewitt é o correspondente vetor gradiente ou a norma deste vetor. O operador de Prewitt é baseado na realização de uma convolução da imagem com um filtro de valores inteiros e separáveis em direções horizontal e vertical e, portanto, é relativamente barato em termos de cálculos, como Sobel e Kayyali operadores. Por outro lado, o gradiente de aproximação que ele produz é relativamente bruto, em particular para a alta frequência de variações na imagem. O operador de Prewitt foi desenvolvido por Judith M. S. Prewitt.

#### Formulação Prewitt

> Matematicamente, o operador usa dois 3×3 kernels que são convolucionadas com a imagem original para calcular aproximações das derivadas - uma para alterações horizontais, e uma para verticais. Se definirmos como a imagem de origem, e são duas imagens que em cada ponto contém a horizontal e a vertical de derivados de aproximações, os últimos são calculados como:
>$$
G_{x} =  \begin{bmatrix}
    -1 & 0 & 1 \\
    -1 & 0 & 1 \\
    -1 & 0 & 1 \\
\end{bmatrix} * A
\quad and \quad 
G_{y} =  \begin{bmatrix}
    -1 & -1 & -1 \\
    0 & 0 & 0 \\
    1 & 1 & 1 \\
\end{bmatrix} * A
>$$
> onde aqui denota uma operação deconvolução 1-dimensional.

> Como os kernels Prewitt podem ser decompostos como produtos de um kernel de média e diferenciação, eles calculam o gradiente com suavização. Portanto, é um filtro separável. Por exemplo, pode ser escrito como:
>$$
\begin{bmatrix}
    -1 & 0 & 1 \\
    -1 & 0 & 1 \\
    -1 & 0 & 1 \\
\end{bmatrix} =
\begin{bmatrix}
    1 \\
    1  \\
    1  \\
\end{bmatrix}
\begin{bmatrix}
    -1 & 0 & 1\\
\end{bmatrix}
>$$

> O x-coordenar é aqui definido como o aumento no "direito"-direção, e o y-coordenadas é definido como o aumento no "de baixo"-direção. Em cada ponto da imagem, resultante do gradiente de aproximações podem ser combinadas para dar a magnitude do gradiente, usando:
>
> $G = \sqrt {G_{x}^{2} + G_{y}^{2}}$

> Usando esta informação, podemos também calcular o gradiente de direção:
> 
> $\Theta = \operatorname {atan2}(G_{y}, G_{x})$
> 
> onde, por exemplo, 
> $\Theta$  0 para uma aresta vertical, que é mais escuro no lado direito.

#### Sobre Sobel

> O operador de Prewitt é usado no processamento de imagem, particularmente na detecção de borda algoritmos. Tecnicamente, é uma operador de diferença, calcular uma aproximação do gradiente da imagem de intensidade de função. Em cada ponto da imagem, o resultado do operador de Prewitt é o correspondente vetor gradiente ou a norma deste vetor. O operador de Prewitt é baseado na realização de uma convolução da imagem com um filtro de valores inteiros e separáveis em direções horizontal e vertical e, portanto, é relativamente barato em termos de cálculos, como Sobel e Kayyali operadores. Por outro lado, o gradiente de aproximação que ele produz é relativamente bruto, em particular para a alta frequência de variações na imagem. O operador de Prewitt foi desenvolvido por Judith M. S. Prewitt.

#### Formulação Sobel

> Matematicamente este operador utiliza duas matrizes 3×3 que são convoluídas com a imagem original para calcular aproximações das derivadas - uma para as variações horizontais e uma para as verticais. Sendo $A$ a imagem inicial então, $G_{x}$ e $G_{y}$ serão duas imagens que em cada ponto contêm uma aproximação às derivadas horizontal e vertical de $A$.
> 
> $$ G_{x} = 
> \begin{bmatrix}
>    -1 & 0 & +1 \\
>    -2 & 0 & +2 \\
>    -1 & 0 & +1 \\
> \end{bmatrix} * A
>\quad and \quad 
>G_{y} =  
>  \begin{bmatrix}
>    +1 & +2 & +1 \\
>    0 & 0 & 0 \\
>    -1 & -2 & -1 \\
> \end{bmatrix} * A
>$$
>
>Portanto a magnitude, $G$, e a direcção, $\Theta$, do gradiente são dados por:
>
> $G = \sqrt {G_{x}^{2} + G_{y}^{2}} \\$ 
> 
>${\Theta } = \operatorname {arctan} \left({G_{y}} \over {G_{x}}\right)$

---

## :octocat: Demo

<h3 align="center">Aplicação funcional</h3>
<p align="center">
    <img src="https://drive.google.com/uc?export=view&id=15krmtBk-AjxkCl4PiwAQFWk3TpOVPjO1" alt="composia-demo" />
</p>

---

## :rocket: Tecnologias

Esta aplicação foi desenvolvida com as seguintes tecnologias:

> - [Python](https://www.python.org/)
> - [VS Code](https://code.visualstudio.com/)
> - E outras tecnologias...

## :information_source: Referências

1. [«Alternative Approach for Satellite Cloud Classification: Edge Gradient Application»](https://www.hindawi.com/journals/amete/2013/584816/). Advances in Meteorology. 2013. ISSN [1687-9309](https://www.worldcat.org/title/advances-in-meteorology/oclc/1117264174). doi:[10.1155/2013/584816](https://www.hindawi.com/journals/amete/2013/584816/)
2. [«Comparisions of Robert, Prewitt, Sobel operator based edge detection methods for real time uses on FPGA - IEEE Conference Publication»](https://ieeexplore.ieee.org/abstract/document/7095920). ieeexplore.ieee.org.

## :memo: Licença

Este projeto está sob o MIT license. Veja a [LICENSE](https://github.com/joaoeliandro/filtro-sobel-pdi/blob/master/LICENSE) para mais informações.

[python]: https://www.python.org/downloads/release/python-370/