SELECT cdpro, nmcanalvendas ,nmpro, sum(qtd) AS quantidade_vendas 
FROM tbvendas t 
WHERE status = 'Concluído' AND nmcanalvendas IN ('Matriz','Ecommerce') 
GROUP BY cdpro,nmcanalvendas 
ORDER BY quantidade_vendas 
LIMIT 10;
