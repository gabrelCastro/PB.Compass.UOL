select distinct a.nome 
from autor as a 
left join livro as l 
on l.autor = a.codautor 
left join editora e 
on e.codeditora = l.editora 
left join endereco 
on endereco.codendereco = e.endereco 
where (endereco.estado not in ('RIO GRANDE DO SUL','PARANÁ')); 

