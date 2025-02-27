SELECT t2.nmvdd as vendedor, sum(vrunt * qtd) as valor_total_vendas,  round((CAST(t2.perccomissao as float)/100)*sum(vrunt * qtd) ,2) as comissao 
FROM tbvendas t 
left join tbvendedor t2 
on t2.cdvdd = t.cdvdd 
where status = 'Concluído' 
group by t.cdvdd 
order by comissao DESC;
