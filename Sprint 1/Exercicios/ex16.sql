SELECT estado,nmpro,round(avg(qtd),4) AS quantidade_media 
FROM tbvendas 
WHERE status = 'Concluído' 
GROUP BY estado,cdpro 
ORDER BY estado,nmpro;