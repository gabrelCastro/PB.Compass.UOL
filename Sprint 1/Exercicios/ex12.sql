WITH vendedor AS
(SELECT tb.cdvdd,sum(qtd*vrunt) AS valor_total_vendas  
FROM tbvendas AS tb  
WHERE tb.status = 'Concluído' 
GROUP BY tb.cdvdd 
HAVING  sum(qtd*vrunt) <> 0 
ORDER BY sum(qtd*vrunt) 
LIMIT 1)


SELECT cddep,nmdep,dtnasc,(SELECT valor_total_vendas FROM vendedor ) as valor_total_vendas  
FROM tbdependente t 
WHERE t.cdvdd = (SELECT cdvdd FROM vendedor);