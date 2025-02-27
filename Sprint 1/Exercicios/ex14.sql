SELECT estado,round(avg(qtd*vrunt),2) 
AS gastomedio 
FROM tbvendas 
where status= 'Concluído' 
GROUP BY estado 
ORDER BY gastomedio DESC;