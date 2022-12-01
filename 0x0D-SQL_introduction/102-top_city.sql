-- Script that displays the average temperature
-- Query to display the average temperature by city ordered by temperature
SELCT city, AVG(value) AS avg_tenp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY ctiy
ORDER BY avg_temp DESC
LIMIT 3;
