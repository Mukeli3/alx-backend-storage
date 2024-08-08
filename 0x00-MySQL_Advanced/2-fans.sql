-- SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans
-- mysql -u root -p database_name < path_to_metal_bands.sql (import table dump)
SELECT origin, COUNT(*) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
