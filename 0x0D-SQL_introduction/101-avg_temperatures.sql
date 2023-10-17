-- a script that displays the average temperature in F by city
-- ordered by temperature in DESC
SELECT city, AVG(value) AS avg_temp
FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
