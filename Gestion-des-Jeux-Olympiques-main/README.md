# Gestion des Jeux Olympiques (JO)

## Description
Application Python pour la gestion et l'analyse d'une base de données relative aux Jeux Olympiques. Ce projet permet de créer, gérer et interroger une base de données SQLite contenant des informations sur les épreuves, les sportifs, les équipes et leurs performances.

## Fonctionnalités
- **Gestion de la base de données** : Création, insertion et suppression de données
- **Extraction de données** : Importation automatique depuis fichiers Excel
- **Requêtes avancées** : 
  - Liste des épreuves par discipline (ex: Ski alpin)
  - Affichage des âges des sportifs
  - Nombre de sportifs par équipe
  - Moyenne d'âge des équipes médaillées
  - Classement des pays
- **Vues SQL** : Génération automatique de vues pour faciliter les analyses

## Structure du projet
```
.
├── main.py                    # Point d'entrée - Menu principal
├── actions/
│   ├── database_functions.py  # Fonctions CRUD sur la BD
│   └── database_queries.py    # Requêtes analytiques
├── utils/
│   ├── db.py                  # Utilitaires de base de données
│   └── excel_extractor.py     # Extraction de données Excel
├── data/
│   ├── LesJO.xlsx            # Fichier source de données
│   ├── v0_createDB.sql       # Script création de la BD
│   ├── v0_deleteDB.sql       # Script suppression de la BD
│   ├── CreateTrigger.sql     # Triggers SQL
│   └── CreateView.sql        # Vues SQL
└── Conception/                # Documentation et schémas

```

## Installation

### Prérequis
- Python 3.7+
- Bibliothèques requises (à spécifier dans un `requirements.txt`)

### Étapes
```bash
git clone https://github.com/Belaidbens/Gestion-des-Jeux-Olympiques.git
cd Gestion-des-Jeux-Olympiques
pip install -r requirements.txt
```

## Utilisation

Lancer le menu interactif :
```bash
python main.py
```

### Menu disponible
1. Créer la base de données
2. Insérer les données du fichier Excel
3. Insérer toutes les données
4. Supprimer la base de données
5. Liste des épreuves de Ski alpin
6. Créer les vues
7. Afficher les âges des sportifs
8. Afficher le nombre de sportifs par équipe
9. Afficher la moyenne d'âge des équipes médaillées
10. Afficher le classement des pays

## Technologies
- **Python** : Langage principal
- **SQLite** : Base de données
- **Excel** : Source de données
- **SQL** : Requêtes et vues

## Auteur
[Belaidbens](https://github.com/Belaidbens)

## Licence
À spécifier (MIT, GPL, etc.)

## Contribution
Les contributions sont bienvenues ! N'hésitez pas à ouvrir des issues ou des pull requests.
