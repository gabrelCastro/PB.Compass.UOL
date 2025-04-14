CREATE DATABASE meubanco

CREATE EXTERNAL TABLE IF NOT EXISTS meubanco.nomes ( 
    nome STRING, 
    sexo CHAR(1), 
    total INT, 
    ano INT
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES ( 'serialization.format' = ',', 'field.delim' = ','
)
LOCATION 's3://bucket-site-8-04/dados/'


WITH nomes_com_decada AS (
    SELECT 
        nome,
        CASE 
            WHEN ano >= 1950 AND ano < 1960 THEN 'Década de 1950'
            WHEN ano >= 1960 AND ano < 1970 THEN 'Década de 1960'
            WHEN ano >= 1970 AND ano < 1980 THEN 'Década de 1970'
            WHEN ano >= 1980 AND ano < 1990 THEN 'Década de 1980'
            WHEN ano >= 1990 AND ano < 2000 THEN 'Década de 1990'
            WHEN ano >= 2000 AND ano < 2010 THEN 'Década de 2000'
            WHEN ano >= 2010 AND ano < 2020 THEN 'Década de 2010'
            WHEN ano >= 2020 AND ano < 2030 THEN 'Década de 2020'
        END AS decada
    FROM meubanco.nomes
),
frequencia_por_nome_decada AS (
    SELECT 
        nome,
        decada,
        COUNT(*) AS total
    FROM nomes_com_decada
    GROUP BY nome, decada
),
top3_por_decada AS (
    SELECT 
        nome,
        decada,
        total,
        ROW_NUMBER() OVER (PARTITION BY decada ORDER BY total DESC) AS posicao
    FROM frequencia_por_nome_decada
)
SELECT 
    nome,
    decada,
    total
FROM top3_por_decada
WHERE posicao <= 3 and decada <> ''
ORDER BY decada, total DESC;