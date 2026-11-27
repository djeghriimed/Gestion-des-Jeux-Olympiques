
CREATE TRIGGER Verif_Pays_Equipe_Sportif
BEFORE INSERT ON EquipeSportif
FOR EACH ROW
BEGIN
SELECT
  CASE
  WHEN (SELECT paysEq FROM LesEquipes WHERE numEq = NEW.numEq)
      <> (SELECT paysSp FROM LesSportifs WHERE numSp = NEW.numSp)
  THEN RAISE(ABORT, 'Le pays du sportif doit être le même que celui de l''équipe')
  END;
END;
/
CREATE TRIGGER verif_nb_medaille
BEFORE INSERT ON LesResultats
FOR EACH ROW
WHEN EXISTS (
    SELECT 1
    FROM LesResultats
    WHERE numEp = NEW.numEp
    AND typeMedaille = NEW.typeMedaille
)
BEGIN
    SELECT RAISE(ABORT, 'Une seule médaille de chaque type par épreuve');
END;
/
CREATE TRIGGER verif_participant
BEFORE INSERT ON Inscrits
FOR EACH ROW
WHEN NOT (
   (NEW.participant BETWEEN 1000 AND 1500
    AND EXISTS (SELECT 1 FROM LesSportifs WHERE numSp = NEW.participant))
OR (NEW.participant BETWEEN 1 AND 100
    AND EXISTS (SELECT 1 FROM LesEquipes WHERE numEq = NEW.participant))
)
BEGIN
    SELECT RAISE(ABORT, 'participant doit être un sportif ou une équipe');
END;
/
CREATE TRIGGER Inscriptions_categorie_individuelle
BEFORE INSERT ON Inscrits
WHEN EXISTS (
    SELECT 1
    FROM LesSportifs S
    JOIN LesEpreuves E ON E.numEp = NEW.numEp
    WHERE S.numSp = NEW.participant
      AND E.formeEp = 'individuelle'
      AND S.categorieSp <> E.categorieEp
)
BEGIN
    SELECT RAISE(ABORT, 'Catégorie incompatible pour une épreuve individuelle');
END;
