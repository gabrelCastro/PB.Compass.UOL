select codautor, autor.nome, count(livro.titulo) as quantidade_publicacoes 
from autor 
left join livro 
on livro.autor = codautor 
group by autor.nome 
order by quantidade_publicacoes DESC 
LIMIT 1;