# Resumo

**Python:** Achei o curso execelente, principalmente pra quem já sabia alguma linguagem de programação, pois ele não ensinou do zero e sim foi passando a sintaxe da linguagem python, além de seus métodos mais uteis

**Curso de Ciência de Dados:** Não gostei muito do curso, achei ele bem simples e não muito explicativo. Não senti muita confiança do instrutor com essse conteúdo também. Como eu já tinha feito outro curso, que tinha uma qualidade significativamente maior, tive essa percepção.

**Estatística Descritiva:** Gostei bastante do curso, bem explicativo e com detalhes, como a remoção de outliers, importantes.

# Exercícios


1. Exercício 1
[Resposta Ex1.](./Exercicios/ex1.py)


2. Exercício 2
[Resposta Ex2.](./Exercicios/ex2.py)


3. Exercício 3
[Resposta Ex3.](./Exercicios/ex3.py)


4. Exercício 4
[Resposta Ex4.](./Exercicios/ex4.py)


5. Exercício 5
[Resposta Ex5.](./Exercicios/ex5.py)


6. Exercício 6
[Resposta Ex6.](./Exercicios/ex6.py)

7. Exercício 7
[Resposta Ex7.](./Exercicios/ex7.py)


8. Exercício 8
[Resposta Ex8.](./Exercicios/ex8.py)


9. Exercício 9
[Resposta Ex9.](./Exercicios/ex9.py)


10. Exercício 10
[Resposta Ex10.](./Exercicios/ex10.py)


11. Exercício 11
[Resposta Ex11.](./Exercicios/ex11.py)


12. Exercício 12
[Resposta Ex12.](./Exercicios/ex12.py)

13. Exercício 13
[Resposta Ex13.](./Exercicios/ex13.py)


14. Exercício 14
[Resposta Ex14.](./Exercicios/ex14.py)

15. Exercício 15
[Resposta Ex15.](./Exercicios/ex15.py)

16. Exercício 16
[Resposta Ex16.](./Exercicios/ex16.py)

17. Exercício 17
[Resposta Ex17.](./Exercicios/ex17.py)

18. Exercício 18
[Resposta Ex18.](./Exercicios/ex18.py)

19. Exercício 19
[Resposta Ex19.](./Exercicios/ex19.py)

20. Exercício 20
[Resposta Ex20.](./Exercicios/ex20.py)

21. Exercício 21
[Resposta Ex21.](./Exercicios/ex21.py)

22. Exercício 22
[Resposta Ex22.](./Exercicios/ex22.py)

23. Exercício 23
[Resposta Ex23.](./Exercicios/ex23.py)

24. Exercício 24
[Resposta Ex24.](./Exercicios/ex24.py)

25. Exercício 25
[Resposta Ex25.](./Exercicios/ex25.py)

26. Exercício 26
[Resposta Ex26.](./Exercicios/ex26.py)



#### Exercício de ETL

###### Arquivo 

[Arquivo ipynb com a resolução](./Exercicios/Exercicio2_ETL/exETL.ipynb)

###### Resultado das Etapas

- [Etapa 1](./Exercicios/Exercicio2_ETL/etapa-1.txt)
- [Etapa 2](./Exercicios/Exercicio2_ETL/etapa-2.txt)
- [Etapa 3](./Exercicios/Exercicio2_ETL/etapa-3.txt)
- [Etapa 4](./Exercicios/Exercicio2_ETL/etapa-4.txt)
- [Etapa 5](./Exercicios/Exercicio2_ETL/etapa-5.txt)


###### Principais pontos do ETL

Acretito que ter usado a função split tenha facilitado bastante o processo, além de utilizar essa função que desenvolvi para resolver os problemas que ocorreram:

``` 
    def verificacaoDeVirgula(linha):
    intervalo = False
    linha = list(linha)
    for x in range(len(linha)):
        if linha[x] == '"':
            linha[x] = ""
            intervalo = not intervalo
        if linha[x] == "," and intervalo:
            linha[x] = "."
    return "".join(linha)


```

Durante a resolução do exercício fiz dois tipos de resolução, uma com remoção de outlier (ensinada no curso de estatística) e outra sem. O método sem remoção foi o "printado" no txt.

# Evidências


[Fotos de Confirmação](./Exercicios/Evidencias)



# DESAFIO

[DESAFIO](./Desafio)