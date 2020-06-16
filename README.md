# Linguagem em Código Morse
<br>
Este reposítório contém uma definição de uma linguagem escrita em código morse e um interpretador em Python para ela.

A EBNF da linguagem se encontra no arquivo **MorseLanguage.ebnf** juntamente com uma versão traduzida em comentários.
Segue um trecho da estrutura:
```
program

   : '--- .--. . -. .--. .-. --- --. .-. .- --' statement+ '-.-. .-.. --- ... . .--. .-. --- --. .-. .- --'

   ---...
   ;


statement

   : '.. ..-.' paren_expr statement

   | '.. ..-.' paren_expr statement '. .-..' statement

   | '.-- .-..' paren_expr statement

   | '..-. .-.' for_expr statement '---...'

   | '..-. ..- -. -.-. - .. --- -.' func_name func_inputs statement'---...'

   | '--.- -...' statement* '-.-. -...'

   | expr '---...'

   | term '---...'

   | '---...'

   ---...
   ;
```

Versão traduzida
```
program

   : OPENPROGRAM statement+ CLOSEPROGRAM

   :


statement

   : 'if' paren_expr statement

   | 'if' paren_expr statement 'else' statement

   | 'while' paren_expr statement

   | 'for' for_expr statement ':'

   | 'function' func_name func_inputs statement':'

   | 'OPENBLOCK' statement* 'CLOSEBLOCK'

   | expr ':'

   | term ':'

   | ':'

   :
```

A estrutura da Linguagem e do interpretador se baseiam em PHP, porém a linguagem além das traduções diretas dos tokens para morse, algumas alterações foram necessárias para suprir algumas limitações que existem no alfabeto morse. 
Por exemplo, o *';'* no final de cada *Command*, é substituído por ':' .
Segue a tabela completa de alteração de tokens:
| Token em PHP | Token substituido | Token em Morse                                 |
|--------------|-------------------|------------------------------------------------|
| *            | MULT              | -- ..- .-.. -                                  |
| .            | CONCAT            | -.-. --- -. -.-. .- -                          |
| <?php        | OPENPROGRAM       | --- .--. . -. .--. .-. --- --. .-. .- --       |
| ?>           | CLOSEPROGRAM      | -.-. .-.. --- ... . .--. .-. --- --. .-. .- -- |
| {            | OPENBLOCK         | --- .--. . -. -... .-.. --- -.-. -.-           |
| }            | CLOSEBLOCK        | -.-. .-.. --- ... . -... .-.. --- -.-. -.-     |
| >            | GREATER           | --. .-. . .- - . .-.                           |
| <            | LESS              | .-.. . ... ...                                 |
| $            | @                 | .--.-.                                         |
| ;            | :                 | ---...                                         |


A linguagem possui recursos básicos funcionais, como loops, variáveis, funções, recursões.

Como exemplo de código temos o arquivo input.php, que contem a versão com o alfabeto tradicional, que pode ser traduzido para morse no script morse_encoder.py ou em qualquer ferramenta online que funciona da mesma maneira

**input.php:**
```
OPENPROGRAM
OPENBLOCK
    function independence(@x) OPENBLOCK
        @x = 42:
        return @x:
        CLOSEBLOCK
    @x = 10 MULT 2:
    independence(@x):
    echo @x:
    echo "a" CONCAT "b":

    @x1 = 3:
    @x1 = @x1 +1:

    echo @x1:

    @y1 = @x1 MULT 100:
    echo @y1:

    if (1 == 1) OPENBLOCK
        echo "TRUEEEE":
    CLOSEBLOCK else OPENBLOCK
        echo 0:
    CLOSEBLOCK

    if (1 LESS 0) OPENBLOCK
        echo "0":
    CLOSEBLOCK else OPENBLOCK
        echo "FALSEEEEEEEEEEEEE":
    CLOSEBLOCK


    @a3333 = 5:

    while(@a3333 GREATER 0) OPENBLOCK
        echo @a3333:
        @a3333 = @a3333 - 1:
    CLOSEBLOCK


    function teste() OPENBLOCK
        echo "FUNCTION":
    CLOSEBLOCK

    teste():

    echo 2 MULT 2 MULT 10 / 2 + 500:


CLOSEBLOCK
CLOSEPROGRAM

```

O equivalente desse código em morse está no arquvio **input_morse.php**:
```
--- .--. . -. .--. .-. --- --. .-. .- -- 
--- .--. . -. -... .-.. --- -.-. -.- 
        ..-. ..- -. -.-. - .. --- -.   .. -. -.. . .--. . -. -.. . -. -.-. . -.--. .--.-. -..- -.--.-   --- .--. . -. -... .-.. --- -.-. -.- 
                .--.-. -..-   -...-   ....- ..--- ---... 
                .-. . - ..- .-. -.   .--.-. -..- ---... 
                -.-. .-.. --- ... . -... .-.. --- -.-. -.- 
        .--.-. -..-   -...-   .---- -----   -- ..- .-.. -   ..--- ---... 
        .. -. -.. . .--. . -. -.. . -. -.-. . -.--. .--.-. -..- -.--.- ---... 
        . -.-. .... ---   .--.-. -..- ---... 
        . -.-. .... ---   .-..-. .- .-..-.   -.-. --- -. -.-. .- -   .-..-. -... .-..-. ---... 
        .--.-. -..- .----   -...-   ...-- ---... 
        .--.-. -..- .----   -...-   .--.-. -..- .----   .-.-. .---- ---... 
        . -.-. .... ---   .--.-. -..- .---- ---... 
        .--.-. -.-- .----   -...-   .--.-. -..- .----   -- ..- .-.. -   .---- ----- ----- ---... 
        . -.-. .... ---   .--.-. -.-- .---- ---... 
        .. ..-.   -.--. .----   -...- -...-   .---- -.--.-   --- .--. . -. -... .-.. --- -.-. -.- 
                . -.-. .... ---   .-..-. - .-. ..- . . . . .-..-. ---... 
        -.-. .-.. --- ... . -... .-.. --- -.-. -.-   . .-.. ... .   --- .--. . -. -... .-.. --- -.-. -.- 
                . -.-. .... ---   ----- ---... 
        -.-. .-.. --- ... . -... .-.. --- -.-. -.- 
        .. ..-.   -.--. .----   .-.. . ... ...   ----- -.--.-   --- .--. . -. -... .-.. --- -.-. -.- 
                . -.-. .... ---   .-..-. ----- .-..-. ---... 
        -.-. .-.. --- ... . -... .-.. --- -.-. -.-   . .-.. ... .   --- .--. . -. -... .-.. --- -.-. -.- 
                . -.-. .... ---   .-..-. ..-. .- .-.. ... . . . . . . . . . . . . . .-..-. ---... 
        -.-. .-.. --- ... . -... .-.. --- -.-. -.- 
        .--.-. .- ...-- ...-- ...-- ...--   -...-   ..... ---... 
        .-- .... .. .-.. . -.--. .--.-. .- ...-- ...-- ...-- ...--   --. .-. . .- - . .-.   ----- -.--.-   --- .--. . -. -... .-.. --- -.-. -.- 
                . -.-. .... ---   .--.-. .- ...-- ...-- ...-- ...-- ---... 
                .--.-. .- ...-- ...-- ...-- ...--   -...-   .--.-. .- ...-- ...-- ...-- ...--   -....-   .---- ---... 
        -.-. .-.. --- ... . -... .-.. --- -.-. -.- 
        ..-. ..- -. -.-. - .. --- -.   - . ... - . -.--. -.--.-   --- .--. . -. -... .-.. --- -.-. -.- 
                . -.-. .... ---   .-..-. ..-. ..- -. -.-. - .. --- -. .-..-. ---... 
        -.-. .-.. --- ... . -... .-.. --- -.-. -.- 
        - . ... - . -.--. -.--.- ---... 
        . -.-. .... ---   ..---   -- ..- .-.. -   ..---   -- ..- .-.. -   .---- -----   -..-.   ..---   .-.-.   ..... ----- ----- ---... 
-.-. .-.. --- ... . -... .-.. --- -.-. -.- 
-.-. .-.. --- ... . .--. .-. --- --. .-. .- -- 
```

Saída do interpretador **main_morse.py**
```
20
AB
4
400
TRUEEEE
FALSEEEEEEEEEEEEE
5
4
3
2
1
FUNCTION
520
```
A saída foi como esperado.

A **desvantagem** dessa linguagem é a óbvia dificuldade de programar, pois necessita que o programador decore todos o alfabeto Morse, ou tenha alguma ferramente para que faça a tradução, porém há alguns casos que se forçarmos um pouco, a linguagem possa ser conveniente, como por exemplo um dispositivo com software programado (arduino por exemplo) que possua uma camera, nesse caso, ele pode ser programado a distancia usando um emissor de luz. Outro exemplo é se um náufrago emitisse um assovio em formato da linguagem em morse para um navio que estivesse passando perto e que tivesse um computador com microfone sensível e que pudesse interpretar a linguagem, então o náufrago poderia enviar uma mensagem ou até um e-mail com a linguagem 😂. 

Uma **vantagem** é a conveniência na transmissão de informação direto para um computador, usando luz, som etc.
Detalhe sobre o código morse, é que é possivel escrever com apenas um recurso, como um tom de assovio, um tom de luz. Os caracteres são diferenciados pela distancia de tempo entre cada emissao. O '-' é uma unidade de tempo, '.' é duas unidades de tempo e o espaco que separa os caracteres são 3 unidades de tempo. Cada palavra é separada por 2 ou mais espaços.

A linguagem ainda falta alguns recursos que são necessários suas implementações no futuro, como objetos, arrays, variável do tipo NULL, resources entre outros.




