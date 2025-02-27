select autor.nome 
from autor 
left join livro l 
ON l.autor = codautor 
where l.cod is null;