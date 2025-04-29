# Resumo (Feedback dos cursos)

**Fundamentals of Analytics**: Este curso foi muito importante para mim, pois reforçou conteúdos que eu já havia estudado, como ETL. Além disso, apresentou, de forma clara, ferramentas extremamente úteis e suas formas de uso, como o AWS Glue — empregado para limpar e normalizar dados antes da análise — em conjunto com outros serviços da AWS. Aprender sobre os 5 V’s (Volume, Variedade, Velocidade, Veracidade e Valor) e compreender como a AWS contribui para cada um deles foi essencial.

**Introduction to Amazon Athena**: Embora o Amazon Athena já tivesse sido abordado em outras sprints, este curso foi fundamental para relembrar conceitos e explorar novas possibilidades da ferramenta. Considero especialmente valioso o fato de o conteúdo cobrir todo o fluxo, desde a criação de um bucket no S3 para armazenar dados e logs até o acesso ao histórico de consultas.

**Serverless Analytics**: Na minha opinião, este curso não foi tão didático quanto os das sprints anteriores. Eu e outros bolsistas percebemos que as legendas em português não estão funcionando corretamente. Ainda assim, o conteúdo é relevante, pois demonstra como utilizar o Amazon QuickSight.


# Exercícios


# Apache Spark (Contador de palavras)

##### OBS: Para comprovar os resultados e evitar redundância nas capturas de tela, cada imagem contém algum indício de que sou eu quem está executando o procedimento. Nas telas do console, normalmente aparece meu usuário da AWS; nas telas do terminal, vê-se o usuário do meu sistema operacional.

[Arquivos utilizados](./Exercicios/ApacheSpark_Contador_de_palavras/)


#### Primeiro foi feito o pull da imagem na máquina

![Upload da Imagem](./Exercicios/ApacheSpark_Contador_de_palavras/Evidencias/downloadImage.png)

#### Criando um container a partir da imagem, com um comando no terminal

![Upload da Imagem](./Exercicios/ApacheSpark_Contador_de_palavras/Evidencias/runContainer.png)
![Upload da Imagem](./Exercicios/ApacheSpark_Contador_de_palavras/Evidencias/runContainerpt2.png)

        sudo docker run -it -p 8888:8888 jupyter/all-spark-notebook

- O comando -it para já abrir o terminal, e o -p para ser possível o tunelamento das portas(8888 do container para 8888 do sistema operacional da máquina)


#### Entrando na página web do servidor web que o spark gera:

![Upload da Imagem](./Exercicios/ApacheSpark_Contador_de_palavras/Evidencias/jupiterLab.png)


É possível notar que o tunelamento funcionou corretamente, umas vez que o container está enviando os dados de sua porta 8888 para a porta 8888 do S0, de acordo com a URL.


#### Conectando ao terminal

![Upload da Imagem](./Exercicios/ApacheSpark_Contador_de_palavras/Evidencias/conectando.png)

**Com o objetivo de ficar mais visível, foi escolhido utilizar o terminal pela interface provida pelo Jupyter**


![Upload da Imagem](./Exercicios/ApacheSpark_Contador_de_palavras/Evidencias/terminal.png)


O código se baseou em conceitos de extrema importância do Spark

- A função **map** pega cada elemento e o coloca junto com o par 1, representando uma unidade.
- A função **filter**, como o próprio nome já diz, filtra os dados. Ela recebe um array e retorna um subconjuto. Nesse caso, as strings vazias retornam false, portanto são tiradas do array
- A função **reduceByKey** pega elementos de chave igual e realiza alguma operação, nesse caso a soma. Essa soma é com o número que representa sua unidade. Vamos supor que a palavra "teste" já foi achada 20 vezes, seu par seria ("teste",20), se encontrasse mais uma com a mesma chave, seria 20 + 1 = 21 e assim em diante.
- A função **sortBy** apenas ordena a partir do número de unidades do par


```
# 4) Pipeline RDD -------------------------------------------------------------
contagem = (
              sc.textFile(ARQUIVO_FONTE)     # lê o arquivo em N partições
              .flatMap(quebrar_em_palavras) # quebra cada linha em palavras
              .filter(lambda p: p)          # remove vazios (evita '' gerado pelo split)
              .map(lambda p: (p, 1))        # vira par (palavra, 1)
              .reduceByKey(lambda a, b: a+b) # soma as ocorrências
              .sortBy(lambda par: par[1], ascending=False)
           )
```


Além disso, para pegar os dados do README, foi utilizado um token gerado pelo GitHub

![Upload da Imagem](./Exercicios/ApacheSpark_Contador_de_palavras/Evidencias/criandoToken.png)

No código, bastou fazer a requisição...

        resposta = requests.get(url, headers=headers)

- header com o token
- Url com o README do repositório


O resultado do código, como mostrado acima, teve como seus primeiros resultados: 

```
p: 18
de: 9
style: 8
e: 8
margin: 7
left: 7
50px: 6
sprint: 6
javascript: 5
b: 4
br: 4
dados: 4
express: 4
ufla: 3
end: 3
sequelize: 3

```

OBS: Alguns deles se referem à tags que foram colocadas no README, como 'p' por exemplo.


![Upload da Imagem](./Exercicios/ApacheSpark_Contador_de_palavras/Evidencias/Rodando.png)


# TMDB

[Arquivos utilizados](./Exercicios/Exercicios_TMDB/)

#### Conta no TMDB criada

![Upload da Imagem](./Exercicios/Exercicios_TMDB/Evidencias/Perfil.png)

#### Realizando a requisição

![Upload da Imagem](./Exercicios/Exercicios_TMDB/Evidencias/dados2.png)


# Evidências

[Fotos de Confirmação](./Evidencias)



# DESAFIO

[DESAFIO](./Desafio)