select autor.nome,codautor, nascimento,count(livro.titulo) as quantidade
from autor 
left join livro 
on autor.codautor = livro.autor
group by autor.nome 
order by autor.nome;
