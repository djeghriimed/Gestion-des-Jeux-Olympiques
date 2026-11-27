import sys
from utils import db
from utils import excel_extractor

# Fonction permettant de créer la base de données
def database_create(data):
    print("\nCréation de la base de données")
    try:
        # On exécute les requêtes du fichier de création
        db.updateDBfile(data, "data/v0_createDB.sql")
        db.updateDBfile(data,"data/createTrigger.sql",True)
    except Exception as e:
        # En cas d'erreur, on affiche un message
        print("L'erreur suivante s'est produite pendant lors de la création de la base : " + repr(e) + ".")
    else:
        # Si tout s'est bien passé, on affiche le message de succès et on commit
        print("La base de données a été créée avec succès.")
        data.commit()
##########################################################################################
# Fonction permettant d'insérer les données dans la base

def database_insert(data):
    print("\nInsertion des données dans la base.")
    try:
        # on lit les données dans le fichier Excel
        #excel_extractor.read_excel_file_V0(data, "data/LesJO.xlsx")
         excel_extractor.read_excel_file_V0(data, "data/LesJO.xlsx")
    except Exception as e:
        # En cas d'erreur, on affiche un message
        print("L'erreur suivante s'est produite lors de l'insertion des données : " + repr(e) + ".", file=sys.stderr)
    else:
        # Si tout s'est bien passé, on affiche le message de succès et on commit
        print("Un jeu de test a été inséré dans la base avec succès.")
        data.commit()

##########################################################################################
def database_insertSp(data):
    print("\nInsertion des données dans la base.")
    try:
        # on lit les données dans le fichier Excel
        #excel_extractor.read_excel_file_V0(data, "data/LesJO.xlsx")
         excel_extractor.extract_sportifs(data, "data/LesJO.xlsx")
    except Exception as e:
        # En cas d'erreur, on affiche un message
        print("L'erreur suivante s'est produite lors de l'insertion des données : " + repr(e) + ".", file=sys.stderr)
    else:
        # Si tout s'est bien passé, on affiche le message de succès et on commit
        print("Un jeu de test a été inséré dans la base avec succès.")
        data.commit()
##########################################################################################
def database_insertEq(data):
    print("\nInsertion des données dans la base.")
    try:
        # on lit les données dans le fichier Excel
        #excel_extractor.read_excel_file_V0(data, "data/LesJO.xlsx")
         excel_extractor.extract_equipes(data, "data/LesJO.xlsx")
    except Exception as e:
        # En cas d'erreur, on affiche un message
        print("L'erreur suivante s'est produite lors de l'insertion des données : " + repr(e) + ".", file=sys.stderr)
    else:
        # Si tout s'est bien passé, on affiche le message de succès et on commit
        print("Un jeu de test a été inséré dans la base avec succès.")
        data.commit()
##########################################################################################
def database_insertEp(data):
    print("\nInsertion des données dans la base.")
    try:
        # on lit les données dans le fichier Excel
        #excel_extractor.read_excel_file_V0(data, "data/LesJO.xlsx")
         excel_extractor.extract_epreuves(data, "data/LesJO.xlsx")
    except Exception as e:
        # En cas d'erreur, on affiche un message
        print("L'erreur suivante s'est produite lors de l'insertion des données : " + repr(e) + ".", file=sys.stderr)
    else:
        # Si tout s'est bien passé, on affiche le message de succès et on commit
        print("Un jeu de test a été inséré dans la base avec succès.")
        data.commit()        
##########################################################################################
def database_insertEqSp(data):
    print("\nInsertion des données dans la base.")
    try:
        # on lit les données dans le fichier Excel
        #excel_extractor.read_excel_file_V0(data, "data/LesJO.xlsx")
         excel_extractor.extract_equipe_sportifs(data, "data/LesJO.xlsx")
    except Exception as e:
        # En cas d'erreur, on affiche un message
        print("L'erreur suivante s'est produite lors de l'insertion des données : " + repr(e) + ".", file=sys.stderr)
    else:
        # Si tout s'est bien passé, on affiche le message de succès et on commit
        print("Un jeu de test a été inséré dans la base avec succès.")
        data.commit()   
##########################################################################################        
def database_insertInsc(data):
    print("\nInsertion des données dans la base.")
    try:
        # on lit les données dans le fichier Excel
        #excel_extractor.read_excel_file_V0(data, "data/LesJO.xlsx")
         excel_extractor.extract_inscrits(data, "data/LesJO.xlsx")
    except Exception as e:
        # En cas d'erreur, on affiche un message
        print("L'erreur suivante s'est produite lors de l'insertion des données : " + repr(e) + ".", file=sys.stderr)
    else:
        # Si tout s'est bien passé, on affiche le message de succès et on commit
        print("Un jeu de test a été inséré dans la base avec succès.")
        data.commit() 
##########################################################################################
def database_insertRes(data):
    print("\nInsertion des données dans la base.")
    try:
        # on lit les données dans le fichier Excel
        #excel_extractor.read_excel_file_V0(data, "data/LesJO.xlsx")
         excel_extractor.extract_resultats(data, "data/LesJO.xlsx")
    except Exception as e:
        # En cas d'erreur, on affiche un message
        print("L'erreur suivante s'est produite lors de l'insertion des données : " + repr(e) + ".", file=sys.stderr)
    else:
        # Si tout s'est bien passé, on affiche le message de succès et on commit
        print("Un jeu de test a été inséré dans la base avec succès.")
        data.commit() 
##########################################################################################        
# Fonction permettant de supprimer la base de données
def database_delete(data):
    print("\nSuppression de la base de données.")
    try:
        # On exécute les requêtes du fichier de suppression
        db.updateDBfile(data, "data/v0_deleteDB.sql")
    except Exception as e:
        # En cas d'erreur, on affiche un message
        print("Erreur lors de la suppression de la base de données : " + repr(e) + ".")
    else:
        # Si tout s'est bien passé, on affiche le message de succès (le commit est automatique pour un DROP TABLE)
        print("La base de données a été supprimée avec succès.")

##########################################################################################
def database_createView(data):
    print("\nCréation de la base de données")
    try:
        # On exécute les requêtes du fichier de création
        db.updateDBfile(data, "data/CreateView.sql")
    except Exception as e:
        # En cas d'erreur, on affiche un message
        print("L'erreur suivante s'est produite pendant lors de la création des views : " + repr(e) + ".")
    else:
        # Si tout s'est bien passé, on affiche le message de succès et on commit
        print("Les views ont  été créée avec succès.")
        data.commit()
##########################################################################################
def database_insertAll(data):
    database_insertSp(data)
    database_insertEq(data)
    database_insertEp(data)
    database_insertEqSp(data)
    database_insertInsc(data)
    database_insertRes(data)
