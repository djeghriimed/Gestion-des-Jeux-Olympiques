import sqlite3
import pandas as pd
from sqlite3 import IntegrityError

# Fonction permettant de lire le fichier Excel des JO et d'insérer les données dans la base
def read_excel_file_V0(data:sqlite3.Connection, file):
    # Lecture de l'onglet du fichier excel LesSportifsEQ, en interprétant toutes les colonnes comme des strings
    # pour construire uniformement la requête
    df_sportifs = pd.read_excel(file, sheet_name='LesSportifsEQ', dtype=str)
    df_sportifs = df_sportifs.where(pd.notnull(df_sportifs), 'null')

    cursor = data.cursor()
    for ix, row in df_sportifs.iterrows():
        try:
            query = "insert into V0_LesSportifsEQ values ({},'{}','{}','{}','{}','{}',{})".format(
                row['numSp'], row['nomSp'], row['prenomSp'], row['pays'], row['categorieSp'], row['dateNaisSp'], row['numEq'])
            # On affiche la requête pour comprendre la construction. A enlever une fois compris.
            print(query)
            cursor.execute(query)
        except IntegrityError as err:
            print(err)

    # Lecture de l'onglet LesEpreuves du fichier excel, en interprétant toutes les colonnes comme des string
    # pour construire uniformement la requête
    df_epreuves = pd.read_excel(file, sheet_name='LesEpreuves', dtype=str)
    df_epreuves = df_epreuves.where(pd.notnull(df_epreuves), 'null')

    cursor = data.cursor()
    for ix, row in df_epreuves.iterrows():
        try:
            query = "insert into V0_LesEpreuves values ({},'{}','{}','{}','{}',{},".format(
                row['numEp'], row['nomEp'], row['formeEp'], row['nomDi'], row['categorieEp'], row['nbSportifsEp'])

            if row['dateEp'] != 'null':
                query = query + "'{}')".format(row['dateEp'])
            else:
                query = query + "null)"
            # On affiche la requête pour comprendre la construction. A enlever une fois compris.
            print(query)
            cursor.execute(query)
        except IntegrityError as err:
            print(f"{err} : \n{row}")
####################################################################################
#♣extraire les sportifs
def extract_sportifs(data:sqlite3.Connection, file):
  dfSportifs=pd.read_excel(file,sheet_name='LesSportifsEQ',dtype=str,usecols=['numSp','nomSp','prenomSp','pays','categorieSp','dateNaisSp'])
  dfSportifs = dfSportifs.where(pd.notnull(dfSportifs), 'null')
  cursor=data.cursor()
  for ix, row in dfSportifs.iterrows():
    try:
      query="insert into LesSportifs values ({},'{}','{}','{}','{}','{}')".format(
        row['numSp'], row['nomSp'], row['prenomSp'], row['pays'], row['categorieSp'], row['dateNaisSp'])
      print(query)
      cursor.execute(query)
    except IntegrityError as err:
      print(err)

################################################################################################
#♣extraire les equipes
def extract_equipes(data:sqlite3.Connection, file):
  dfEquipes=pd.read_excel(file,sheet_name='LesSportifsEQ',dtype=str,usecols=['numEq','pays'])
  #dfEquipes = dfEquipes.where(pd.notnull(dfEquipes), 'null')
  dfEquipes=dfEquipes.dropna(subset=['numEq'])
  cursor=data.cursor()
  for ix, row in dfEquipes.iterrows():
    try:
      query="insert into LesEquipes values ({},'{}')".format(
        row['numEq'],row['pays'])
      print(query)
      cursor.execute(query)
    except IntegrityError as err:
      print(err)
################################################################################################
#♣extraire les equipesportifs
def extract_equipe_sportifs(data:sqlite3.Connection, file):
  dfEquipeSportifs=pd.read_excel(file,sheet_name='LesSportifsEQ',dtype=str,usecols=['numEq','numSp'])
  #dfEquipeSportifs = dfEquipeSportifs.where(pd.notnull(dfEquipeSportifs), 'null')
  # Convertir toutes les cellules vides ou blanches en NaN
  dfEquipeSportifs=dfEquipeSportifs.dropna(subset=['numEq','numSp'])
  cursor=data.cursor()
  for ix, row in dfEquipeSportifs.iterrows():
    try:
      query="insert into EquipeSportif values ({},{})".format(
        row['numSp'], row['numEq'])
      print(query)
      cursor.execute(query)
    except IntegrityError as err:
      print(err)

################################################################################################
#♣extraire les epreuves
def extract_epreuves(data:sqlite3.Connection, file):
  dfEpreuves=pd.read_excel(file,sheet_name='LesEpreuves',dtype=str,usecols=['numEp','nomEp','formeEp','nomDi','categorieEp','nbSportifsEp','dateEp'])
  dfEpreuves = dfEpreuves.where(pd.notnull(dfEpreuves), 'null')
  cursor=data.cursor()
  for ix, row in dfEpreuves.iterrows():
    try:
      query="insert into LesEpreuves values ({},'{}','{}','{}','{}',{},".format(
        row['numEp'], row['nomEp'], row['nomDi'], row['formeEp'], row['categorieEp'], row['nbSportifsEp'])
      if row['dateEp'] != 'null':
        query = query + "'{}')".format(row['dateEp'])
      else:
        query = query + "null)"
      print(query)
      cursor.execute(query)
    except IntegrityError as err:
      print(f"{err} : \n{row}")

################################################################################################
def extract_inscrits(data:sqlite3.Connection, file):
  dfInscrits=pd.read_excel(file,sheet_name='LesInscriptions',dtype=str)
  dfInscrits = dfInscrits.where(pd.notnull(dfInscrits), 'null')
  cursor=data.cursor()
  for ix, row in dfInscrits.iterrows():
    try:
      query="insert into Inscrits values ({},{})".format(
        row['numEp'], row['numIn'])
      print(query)
      cursor.execute(query)
    except IntegrityError as err:
      print(f"{err} : \n{row}")

################################################################################################
def extract_resultats(data:sqlite3.Connection, file):
  dfResultats=pd.read_excel(file,sheet_name='LesResultats',dtype=str)
  dfResultats = dfResultats.where(pd.notnull(dfResultats), 'null')
  cursor=data.cursor()
  for ix, row in dfResultats.iterrows():
    inserts = [
        (row['numEp'], row['gold'], 'or'),
        (row['numEp'], row['silver'], 'argent'),
        (row['numEp'], row['bronze'], 'bronze')
    ]
    for numEp, podium, typeMedaille in inserts:
      query="insert into LesResultats values ({},{},'{}')".format(
        numEp, podium, typeMedaille)       
      try:
         print(query)
         cursor.execute(query)
      except IntegrityError as err:
         print(f"{err} : \n{row}")

################################################################################################
def extract_tout(data:sqlite3.Connection, file):
    extract_sportifs(data, file)
    extract_equipes(data, file)
    extract_equipe_sportifs(data, file)
    extract_epreuves(data, file)
    extract_inscrits(data, file)
    extract_resultats(data, file)
######################################################################################