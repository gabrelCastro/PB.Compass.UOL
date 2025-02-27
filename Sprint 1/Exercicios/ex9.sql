select cdpro,t.nmpro 
from tbvendas t 
where t.status = 'Concluído' and dtven BETWEEN '2014-02-03' AND '2018-02-02' 
group by t.cdpro 
ORDER by COUNT(*) DESC 
LIMIT 1;
