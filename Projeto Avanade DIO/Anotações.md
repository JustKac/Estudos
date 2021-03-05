# Instruções para início de um projeto

## Instruções iniciais

<p>Inicialmente, confira se a sua IDLE está prontamente configurada, e em seguida, além de criar os arquivos iniciais, é importante organizar o seu repositório local. Uma boa dica é criar pastas para separar os arquivos, tornando a busca mais fácil.

## Dando início ao projeto

No seu arquivo HTML, um bom costume é montar logo de cara o "Esqueleto" do seu site. O padrão é:

<p><!DOCTYPE html>

<html lang="pt-br">

​	<head>

        <meta charset="UTF-8">

        <meta http-equiv="X-UA-Compatible" content="IE=edge">

        <meta name="viewport" content="width=device-width, initial-scale=1.0">

​    <title></title>

​	</head>

​	<body>

​	</body>

</html>

## Dando continuidade ao projeto

### Sobre HTLM

#### Divs

É um elemento de divisão HTML que gera um "container" genérico para conteúdo de fluxo.  Ele pode ser utilizado para agrupar elementos para fins de estilos (usando **class** ou **id**), ou porque eles compartilham valores de atributos, como **lang**. Ele deve ser utilizado somente quando não tiver outro elemento de semântica (tal como article ou nav).    [Divs - Mozila Developer](https://developer.mozilla.org/pt-BR/docs/Web/HTML/Element/div)

#### Tag Body

É onde se encontra o conteúdo so seu site. O body pode ser preenchido com diversas tags, como por exemplo:

- **header** (Cabeçalho) - Onde ficam os conteúdos do topo de sua página.

- **div** (Caixa ou Container) - Bloco onde vão ficar agrupados alguns elementos da página

- **h1 ao h6** - Caixas de texto destacadas

- **nav** (Navegação) - Utilizada pra criar menus de navegação

- **a** - Âncora que interliga vários conteúdos na web, como hiperlinks

   **Exemplo para links de sites**

  - a href="site aqui">nome do site<   

  - a href="mailto:email aqui">email<

  **Exemplo para direcionamento de email**

  - a target="_blank">link<    **Utilizado para abrir página em nova guia**

- **link** - Utilizado para fazer um link entre arquivos, como por exemplo, um link com o CSS

- **button** - Utilizado para criar um botão na página

- **role** - Quando necessário, é utilizado para definir a função de determinada tag. Por exemplo, em um botão pode ser utilizada a **role="button"**

#### Links e Dicas Úteis

##### Font Awesome

O [Font Awesome](https://fontawesome.com/) é uma biblioteca online com vários ícones para uso em aplicações.

##### Owl Carousel

O [Owl Carousel](https://owlcarousel2.github.io/OwlCarousel2/) é um jQuery plugin que permite a criação de um carrossel (slide) responsivo, com função Touch em dispositivos móveis.

### Sobre CSS

<p>CSS é o arquivo onde será processado o estilo ou aparência da página.

Primeiramente deve ser feito um link entre o arquivo HTML e o arquivo CSS. Para isso, deve ser usada a tag **link** dentro do **head** no arquivo HTML e passar as informações de **rel** (rel="stylesheet") e de diretório **href** (href="diretório_aqui").

Em seguida, se necessário, pode ser feito um "reset" da **margin** e do **padding** definindo o valor "0" como padrão global do arquivo. Para deixar o padrão como global, basta usar o comando * , abrir chaves "{}" e colocar a margin e o padding dentro dele. Outra dica é deixar a **box-sizing** com o padrão (*box-sizing*: border-box;) para evitar que o limite de pixels de uma determinada caixa (**box**) não seja excedido.

#### Variáveis em CSS

##### É possível definir variáveis em arquivos CSS e para isso devemos:

1. Chamar o elemento **:root{}**
2. Defini-la dentro desse elemento, exemplo: **:root{ --vermelho: #E50914 }**
3. Para chamar a variável, basta utilizar o comando **var(nome_da_variável)**

##### Comandos dentro do CSS:

- **:root{}** - Permite adicionar elementos dentro da raiz do arquivo
- **:hover{}** - Aplica o estilo associado quando o cursor (mouse pointer) passa sobre um elemento
- **.class** - Chama uma class definida no arquivo HTML

##### Edição de Box:

- **height:** - Utilizado para definir o tamanho da caixa (box)
- **display:** - Especifica o tipo de caixa de renderização usada por um elemento. [Display - Mozila Developer](https://developer.mozilla.org/pt-BR/docs/Web/CSS/display)
- **flex-direction:** - Define como os itens flexíveis são colocados no contêiner flexível, definindo o eixo principal e a direção (normal ou invertido). [Flex-Direction - Mozila Developer](https://developer.mozilla.org/pt-BR/docs/Web/CSS/flex-direction)
- **align-items:** - Estabelece o alinhamento de um certo item dentro do bloco que o contém [Align-Itens - Mozila Developer](https://developer.mozilla.org/pt-BR/docs/Web/CSS/align-items)
- **justify-content:** - Define o padrão para todos os itens da caixa, dando-lhes todas uma maneira padrão de justificar cada caixa ao longo do eixo apropriado. [Justify-Content - Mozila Developer](https://developer.mozilla.org/en-US/docs/Web/CSS/justify-items)

##### Edição de Background

- **-color:** - Define a cor
- **-size:** - Define o tamanho. Específico ou por tipo
  - **cover** - Se ajusta ao tamanho da caixa (box)
- **: url():** - Faz a busca de um arquivo para ser usado como background
-  

##### Efeitos de Transição

- **cursor:** - Muda a visualização do ponteiro do mouse
- **transition:** - Ela permite definir a transição entre dois estados de um elemento. Estados diferentes podem ser definidos usando pseudo-classes tais como **:hover** ou **:active;** ou dinamicamente, usando **javascript**. [Transition - Mozila Developer](https://developer.mozilla.org/pt-BR/docs/Web/CSS/transition)

##### Edição de Texto:

- **font-family** - Define as fontes de texto a serem utilizadas, tendo uma como principal e outras como "emergência" caso a principal não funcione.
- **font-size** - Define o tamanho da fonte.
- **text-decoration** - Define o tipo de decoração da do texto, como por exemplo o <u>texto sublinhado</u>

##### Class Wrapper (Envelopar)

Wrap vem do inglês "embrulhar". Uma wrapper class é uma classe que "embrulha", envolve, outros objetos afim de adicionar algum atributo ao conjunto ou melhor organizar seu código. Com wrapper você também pode blocar conteúdo, separar header e footer do resto do site, posicionar de maneira diferente um grupo de classes, pra facilitar na hora de especificar uma classe no seu CSS ou Javascript, etc.

### Sobre JavaSricpt

<p>JavaScript é uma linguagem de scripting baseada em protótipos, multi-paradigma e dinâmica, suportando os estilos orientado a objetos, imperativo e funcional.

Primeiramente deve ser feito um link entre o arquivo HTML e o arquivo JavaScript. Para isso, deve ser usada a tag **script** dentro do **head** no arquivo HTML e passar as informações de **type** (type="text/javascript") e de diretório **src** (src="diretório_aqui").



#### Atalhos úteis (VS CODE)

- **ctrl + shift + seta para baixo** - Duplica a linha de código selecionada para a linha de baixo.
- **div.nome_da_classe** - Será criada uma div com uma classe já atribuída.