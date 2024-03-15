## Estágio Target Sistemas - Resolução Desafios

A linguagem que eu resolvi utilizar para a resolução dos desafios foi python, minha segunda linguagem mais forte após o Java. Escolhi resolver por python pois as questões não são tão complexas em questão de lógica, então separar isso em arquivos python até mesmo no repositório ficará mais simples e organizado, além de facilitar a leitura dos recrutadores.

- [Primeira Questao](#primeira-questão)
- [Segunda Questao](#segunda-questão)
- [Terceira Questao](#terceira-questão)
- [Quarta Questao](#quarta-questão)
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

#### Terceira Questão

Para a terceira questão, como acredito que a proposta seja mais respostas lógicas, não fiz nenhum script para resolver elas, porém essas foram as minhas respostas:

a) 1, 3, 5, 7, _ **R: 9** (Aumentando de 2 em 2)
b) 2, 4, 8, 16, 32, 64, _ **R: 128** (Cada termo é o dobro do de antes)
c) 0, 1, 4, 9, 16, 25, 36, _ **R: 49** (Cada termo é o quadrado do número natural, no caso da letra C seria o quadrado de 7)
d) 1, 1, 2, 3, 5, 8, _ **R: 13** (Famosa sequência de fibonacci ou soma dos 2 termos antecedentes hehe)
e) 2, 10, 12, 16, 17, 18, 19, _ **R: 20** (Dividindo a sequência em duas partes, em que a primeira inicialmente se pudéssemos declarar o primeiro termo como 0 incrementa dessa forma: +2, +8, +2, +4. A segunda parte apenas incremente de 1 em 1).

#### Quarta Questão

Antes vou nomear os 3 interruptores pra vocês entenderem melhor meu raciocínio. Eles vão ser (stephen-king, allan-poe e bram-stoker)

Pra resolver esse problema, eu primeiramente ligaria o `stephen-king`, e o deixaria ligado por alguns minutos. Logo após, eu desligaria ele e ligaria o `allan-poe`. Assim já conseguia inferir quais estariam responsabilizados por quais salas.

- A sala da lâmpada que tá acesa é controlada pelo `allan-poe`
- A sala da lâmpada que tá apagada e ainda quente é controlada pelo `stephen-kinhg`.
- A lâmpada que tá apagada e fria é controlada pelo `bram-stoker`

Por pura curiosidade, está na ordem dos meus escritores favoritos. hehe!