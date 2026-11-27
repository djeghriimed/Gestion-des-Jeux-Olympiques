PRAGMA foreign_keys=on;
CREATE TABLE V0_LesSportifsEQ
(
  numSp NUMBER(4),
  nomSp VARCHAR2(20),
  prenomSp VARCHAR2(20),
  pays VARCHAR2(20),
  categorieSp VARCHAR2(10),
  dateNaisSp DATE,
  numEq NUMBER(4),
  CONSTRAINT SP_CK1 CHECK(numSp > 0),
  CONSTRAINT SP_CK2 CHECK(categorieSp IN ('feminin','masculin')),
  CONSTRAINT SP_CK3 CHECK(numEq > 0)
);

CREATE TABLE V0_LesEpreuves
(
  numEp NUMBER(3),
  nomEp VARCHAR2(20),
  formeEp VARCHAR2(13),
  nomDi VARCHAR2(25),
  categorieEp VARCHAR2(10),
  nbSportifsEp NUMBER(2),
  dateEp DATE,
  CONSTRAINT EP_PK PRIMARY KEY (numEp),
  CONSTRAINT EP_CK1 CHECK (formeEp IN ('individuelle','par equipe','par couple')),
  CONSTRAINT EP_CK2 CHECK (categorieEp IN ('feminin','masculin','mixte')),
  CONSTRAINT EP_CK3 CHECK (numEp > 0),
  CONSTRAINT EP_CK4 CHECK (nbSportifsEp > 0)
);

Create Table LesEpreuves
(
  numEp NUMBER(5),
  nomEp VARCHAR2(20),
  nomDi VARCHAR2(25),
  formeEp VARCHAR2(13),
  categorieEp VARCHAR2(10),
  nbSportifsEp NUMBER(2),
  dateEp DATE,
  CONSTRAINT EP_PK PRIMARY KEY (numEp),
  CONSTRAINT EP_CK1 CHECK (formeEp IN ('individuelle','par equipe','par couple')),
  CONSTRAINT EP_CK2 CHECK (categorieEp IN ('feminin','masculin','mixte')),
  CONSTRAINT EP_CK3 CHECK (nbSportifsEp > 0),
  CONSTRAINT EP_CK4 CHECK (numEp > 0)
);

Create Table LesSportifs
(
  numSp NUMBER(4) PRIMARY KEY,
  nomSp VARCHAR2(20),
  prenomSp VARCHAR2(20),
  paysSp VARCHAR2(20),
  categorieSp VARCHAR2(10),
  dateNaisSp DATE,
  CONSTRAINT SP_CK1 CHECK(numSp between 1000 and 1500),
  CONSTRAINT SP_CK2 CHECK(categorieSp IN ('feminin','masculin')),
  CONSTRAINT SP_CK3 UNIQUE(nomSp, prenomSp)
);
Create Table LesEquipes
(
 numEq NUMBER(4) PRIMARY KEY,
 paysEq VARCHAR2(20),
 CONSTRAINT EQ_ck1 CHECK(numEq between 1 and 100)

);

Create Table EquipeSportif
(
  numSp NUMBER(4),
  numEq NUMBER(4),
  CONSTRAINT ES_PK PRIMARY KEY (numSp, numEq),
  CONSTRAINT ES_FK1 FOREIGN KEY (numSp) REFERENCES LesSportifs(numSp),
  CONSTRAINT ES_FK2 FOREIGN KEY (numEq) REFERENCES LesEquipes(numEq)
);

Create Table Inscrits(
  numEp NUMBER(5),
  participant NUMBER(4),
  CONSTRAINT I_PK PRIMARY KEY (numEp, participant),
  CONSTRAINT I_FK1 FOREIGN KEY (numEp) REFERENCES LesEpreuves(numEp)
);

Create Table LesResultats
(
  numEp NUMBER(5),
  podium NUMBER(4),
  typeMedaille VARCHAR2(10) CHECK (typeMedaille IN ('or','argent','bronze')),
  CONSTRAINT R_PK PRIMARY KEY (numEp, podium),
  CONSTRAINT R_FK1 FOREIGN KEY (numEp, podium) REFERENCES Inscrits(numEp, participant)
);

/*je peux ajouter trigger que forme epreuve et partciants doivent se correspndre meme pour categorie*/
