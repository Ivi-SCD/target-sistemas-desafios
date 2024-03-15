## Estágio Target Sistemas - Resolução Desafios

A linguagem que eu resolvi utilizar para a resolução dos desafios foi python, minha segunda linguagem mais forte após o Java. Escolhi resolver por python pois as questões não são tão complexas em questão de lógica, então separar isso em arquivos python até mesmo no repositório ficará mais simples e organizado, além de facilitar a leitura dos recrutadores.

- [Primeira Questao](#primeira-questão)
- Segunda Questao
- Terceira Questao
- Quarta Questao
- Quinta Questao

#### Primeira Questão

A resolução foi uma lógica bem simples, basicamente segui o algoritmo dada na questão apenas para obter a resposta.

Arquivo Python: [**Script**](./01-questao/main.py)
R: 91.

#### Segunda Questão

Para resolver a segunda questão pensei inicialmente em fazer com recursividade mas acabei percebendo que caso fosse fornecido um número muito elevado no script o programa perderia perfomance, então eu resolvi fazer utilizando funções normais e arrays.

Como não foi informado casos de números negativos ou tratamento de letras, presumi que seriam sempre números e declarei no próprio script uma váriavel responsável por guardar esse número.

Resolvi por criar duas funções, uma para gerar a sequência de fibonacci utilizando while e outra apenas para verificar se o número fornecido pertence a sequência. Acoplei a função de verificação à de geração da sequência pois presumi também que não seria um grande problema.

Arquivo Python: [**Script**](./02-questao/main.py)
