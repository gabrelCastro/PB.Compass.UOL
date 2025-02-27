SELECT editora.nome, count(*) as quantidade,estado,cidade  
from livro 
left join editora 
on livro.editora = editora.codeditora 
left join endereco 
on endereco.codendereco = editora.endereco 
group by editora.nome 
LIMIT 5;
