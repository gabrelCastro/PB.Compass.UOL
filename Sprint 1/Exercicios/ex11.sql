SELECT cdcli, nmcli , sum(qtd*vrunt) as gasto 
FROM tbvendas t 
where status = 'Concluído' 
group by cdcli 
order by gasto DESC 
limit 1;