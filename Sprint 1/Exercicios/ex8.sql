select t.cdvdd,t.nmvdd 
from tbvendedor t 
left join tbvendas v 
on v.cdvdd = t.cdvdd 
group by t.nmvdd 
order by count(v.cdven) DESC 
limit 1;