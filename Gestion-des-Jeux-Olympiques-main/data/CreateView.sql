
CREATE VIEW LesAgesSportifs AS
SELECT numSp, nomSp, prenomSp, paysSp, categorieSp, dateNaisSp,
(
    strftime('%Y','now') - strftime('%Y', dateNaisSp)
    - (strftime('%m-%d','now') < strftime('%m-%d', dateNaisSp))
) AS agesSp
FROM LesSportifs;

CREATE VIEW LesNbsEquipiers AS
SELECT numEq, COUNT(numSp) AS nbEquipiersEq
FROM EquipeSportif
GROUP BY numEq;

CREATE VIEW MoyAgeEq AS
SELECT E.numEq, AVG(A.agesSp) AS AgeMoy
FROM LesAgesSportifs A
JOIN EquipeSportif E ON A.numSp = E.numSp
GROUP BY E.numEq;

CREATE VIEW AgeMoyEqMedOr AS
SELECT R.podium, M.AgeMoy
FROM LesResultats R 
JOIN MoyAgeEq M ON R.podium = M.numEq
WHERE R.typeMedaille = 'or';


CREATE VIEW ClassementPays AS
SELECT 
    pays,
    SUM(nbOr) AS nbOr,
    SUM(nbArgent) AS nbArgent,
    SUM(nbBronze) AS nbBronze,
    SUM(totalMed) AS totalMed
FROM (

    SELECT 
        E.paysEq AS pays,
        SUM(CASE WHEN R.typeMedaille = 'or' THEN 1 ELSE 0 END) AS nbOr,
        SUM(CASE WHEN R.typeMedaille = 'argent' THEN 1 ELSE 0 END) AS nbArgent,
        SUM(CASE WHEN R.typeMedaille = 'bronze' THEN 1 ELSE 0 END) AS nbBronze,
        COUNT(*) AS totalMed
    FROM LesResultats R
    JOIN LesEquipes E ON R.podium = E.numEq
    WHERE R.typeMedaille IN ('or','argent','bronze')
    GROUP BY E.paysEq

    UNION ALL

    SELECT 
        S.paysSp AS pays,
        SUM(CASE WHEN R.typeMedaille = 'or' THEN 1 ELSE 0 END) AS nbOr,
        SUM(CASE WHEN R.typeMedaille = 'argent' THEN 1 ELSE 0 END) AS nbArgent,
        SUM(CASE WHEN R.typeMedaille = 'bronze' THEN 1 ELSE 0 END) AS nbBronze,
        COUNT(*) AS totalMed
    FROM LesResultats R
    JOIN LesSportifs S ON R.podium = S.numSp
    WHERE R.typeMedaille IN ('or','argent','bronze')
    GROUP BY S.paysSp

)
GROUP BY pays
ORDER BY nbOr DESC, nbArgent DESC, nbBronze DESC;
