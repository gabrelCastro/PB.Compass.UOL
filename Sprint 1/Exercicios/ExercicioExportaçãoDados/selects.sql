select cod as CodLivro,titulo as Titulo, autor as NomeAutor, valor as Valor, editora as CodEditora, e.nome as NomeEditora 
from livro l 
left join editora e 
on e.codeditora= l.editora 
order by l.valor DESC 
LIMIT 10;

SELECT codeditora as CodEditora, e.nome as NomeEditora, count(l.titulo) as QuantidadeLivros 
from livro l 
left join editora e 
on e.codeditora = l.editora 
group by e.codeditora 
order by QuantidadeLivros DESC 
LIMIT 5;