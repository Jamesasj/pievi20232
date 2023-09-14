create table dim_tempo as
select 
	tblData.date as "date"
	, extract ( day from tblData.date) dia_do_mes
	, extract ( month from tblData.date) mes
	, extract ( year from tblData.date) ano
	, date_part('week',tblData.date) semana_ano 
	, date_part('doy',tblData.date) doy 
	, date_part('dow',tblData.date) dow 
from (
SELECT
  '2019-01-01'::DATE + SEQUENCE.number AS date
FROM
  GENERATE_SERIES(0, 900) AS SEQUENCE (number)
) tblData;
