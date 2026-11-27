# Fonction permettant lister les épreuves d'une discipline donnée
def liste_epreuves(data, discipline):
    print("\nListe des épreuves de " + discipline + " :")
    try:
        cursor = data.cursor()
        result = cursor.execute(
            """
                SELECT DISTINCT nomEp, formeEp
                FROM V0_LesEpreuves
                WHERE nomDi = ?
                ORDER BY nomEp
            """,
            [discipline])
    except Exception as e:
        print("Impossible d'afficher les résultats : " + repr(e))
    else:
        for epreuve in result:
            print(epreuve[0] + " - " + epreuve[1])


def afficher_ages_sportifs(data):
    print("\nL'âge des sportifs")
    try:
        cursor = data.cursor()
        cursor.execute("SELECT * FROM LesAgesSportifs")
        for sportifs in cursor.fetchall():
            print(sportifs)
    except Exception as e:
        print("Impossible d'afficher les résultats : " + repr(e))


def afficher_nbs_equipiers(data):
    print("\nLe nombre de sportifs par équipe")
    try:
        cursor = data.cursor()
        cursor.execute("SELECT * FROM LesNbsEquipiers")
        for equipiers in cursor.fetchall():
            print(equipiers)
    except Exception as e:
        print("Impossible d'afficher les équipiers : " + repr(e))


def afficher_age_moy_eq_or(data):
    print("\nL'âge moyen des équipes ayant gagné l'or")
    try:
        cursor = data.cursor()
        cursor.execute("SELECT * FROM AgeMoyEqMedOr")
        for equipe in cursor.fetchall():
            print(equipe)
    except Exception as e:
        print("Impossible d'afficher les résultats : " + repr(e))

def afficher_ClassementPays(data):
    print("\n Le classement des pays ")
    try:
        cursor = data.cursor()
        cursor.execute("SELECT * FROM ClassementPays ")
        for res in cursor.fetchall():
            print(res)
    except Exception as e:
        print("Impossible d'afficher le classement : " + repr(e))
