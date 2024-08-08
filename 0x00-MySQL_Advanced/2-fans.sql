-- SQL script that ranks number of (non-unique) fans
-- mysql -u root -p database_name < metal_bandspath.sql
SELECT origin, SUM(total_fans) AS nb_fans
FROM metal_bands GROUP BY origin ORDER BY nb_fans DESC;
