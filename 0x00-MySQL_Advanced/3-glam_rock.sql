-- SQL script lists all bands with Glam rock as their main style, ranked by their longevity
SELECT name as band_name,
CASE
    WHEN split IS NOT NULL THEN split - formed
    ELSE 2022 - formed
END AS lifespan
FROM metal_bands WHERE main_style = 'Glam rock' ORDER BY lifespan DESC;
