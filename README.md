Analyse du Marché Immobilier Marocain avec Darkom.ma – Data Warehouse & Power BI
📌 Contexte du Projet

Darkom.ma est une plateforme marocaine spécialisée dans les annonces immobilières permettant aux particuliers et professionnels de publier des offres de vente et de location de biens immobiliers à travers le Maroc.

Les données collectées sont souvent hétérogènes, incomplètes ou inconsistantes. L'objectif de ce projet est de mettre en place un pipeline de données complet permettant de transformer des données brutes issues d'un fichier CSV en une architecture analytique prête à être exploitée par Power BI.

L'architecture du projet suit une approche moderne de Data Engineering :

CSV → Staging → Clean Data → Data Warehouse → Power BI

🎯 Objectifs du Projet
Construire un pipeline ETL complet.
Nettoyer et standardiser les données immobilières.
Concevoir un Data Warehouse dimensionnel optimisé pour l'analyse.
Développer des indicateurs métiers pertinents.
Réaliser des tableaux de bord interactifs avec Power BI.
Fournir une vision claire du marché immobilier marocain.
🛠️ Technologies Utilisées
PostgreSQL
SQL
Python (Pandas)
Power BI
Power Query
DAX
Git & GitHub
📂 Architecture du Projet
DARKOM_DWH_PROJECT/
│
├── .venv/
│
├── scripts/
│   ├── clean.ipynb
│   ├── annonces_clean.csv
│   └── darkom-annonces.csv
│
└── sql/
    ├── create_schemas.sql
    ├── create_staging_tables.sql
    ├── create_clean_tables.sql
    ├── create_dim_tables.sql
    ├── create_fact_tables.sql
    └── test.sql
🗄️ Couche Staging

Cette couche sert de zone temporaire pour le chargement des données brutes.

Source des données

Fichier :

darkom_annonces.csv
Colonnes disponibles
annonce_id
date_publication
titre
ville
quartier
type_bien
transaction
prix
surface
nb_chambres
nb_salles_bain
etage
annee_construction
Traitements réalisés
Importation du CSV vers PostgreSQL
Vérification du chargement
Journalisation des opérations (logs)
🧹 Couche Clean Data

Cette étape garantit la qualité et la cohérence des données.

Nettoyage effectué
Suppression des doublons
Détection des enregistrements dupliqués
Conservation des lignes uniques
Gestion des valeurs manquantes

Traitement des colonnes :

date_publication
quartier
nb_chambres
nb_salles_bain
etage
annee_construction
type_bien
transaction
Traitement des valeurs aberrantes

Analyse des anomalies sur :

prix
surface
nb_chambres
Standardisation

Uniformisation :

des villes
des types de biens
des transactions
Conversion des types
DATE pour les dates
INTEGER pour les variables quantitatives
NUMERIC pour les montants et surfaces
⚙️ Feature Engineering

Création de nouvelles variables métier :

Prix par m²
prix_m2 = prix / surface
Âge du bien
age_bien = année_actuelle - annee_construction
Catégories de prix
Économique
Moyen
Haut Standing
Luxe
Catégories de surface
Petit (< 80 m²)
Moyen (80 - 150 m²)
Grand (> 150 m²)
Variables temporelles

Extraction de :

Année
Mois
Trimestre
🏗️ Modélisation du Data Warehouse

Le Data Warehouse est construit dans le schéma :

bi_schema
Modèle adopté

Schéma en étoile (Star Schema)

Table de faits
fact_annonces

Mesures :

prix
surface
prix_m2
age_bien
Dimensions
dim_date
date_publication
annee
mois
trimestre
dim_localisation
ville
quartier
dim_bien
type_bien
nb_chambres
nb_salles_bain
etage
dim_transaction
transaction
categorie_prix
categorie_surface
🚀 Chargement du Data Warehouse
Processus ETL
Chargement Staging
Nettoyage
Création des dimensions
Création de la table de faits
Vérification de cohérence
Indexation
Publication pour Power BI
Optimisations
Clés primaires
Clés étrangères
Index SQL
Validation des relations
📊 Power BI

Connexion directe à PostgreSQL :

PostgreSQL → bi_schema → Power BI
🔍 Power Query

Utilisé pour :

Vérification des types
Nettoyage mineur
Contrôle qualité
Optimisation du modèle Power BI
📈 Mesures DAX

Principaux indicateurs développés :

Nombre total d'annonces
Total Annonces = COUNT(fact_annonces[annonce_id])
Prix moyen
Prix Moyen = AVERAGE(fact_annonces[prix])
Surface moyenne
Surface Moyenne = AVERAGE(fact_annonces[surface])
Prix moyen par m²
Prix Moyen m² = AVERAGE(fact_annonces[prix_m2])
Croissance des annonces

Analyse temporelle basée sur la dimension date.

📊 Dashboards Réalisés
Dashboard 1 — Vue Globale du Marché
Nombre total d'annonces
Prix moyen
Surface moyenne
Répartition par ville
Répartition par type de bien
Vente vs Location
Évolution des annonces
Dashboard 2 — Analyse des Prix
Distribution des prix
Prix moyen par m²
Comparaison des segments immobiliers
Prix par type de bien
Analyse des catégories de prix
Dashboard 3 — Analyse Géographique
Répartition des annonces par ville
Prix moyen par ville
Prix moyen par quartier
Top zones les plus chères
Concentration des annonces
Dashboard 4 — Analyse des Tendances
Évolution des prix
Évolution du volume d'annonces
Analyse saisonnière
Comparaison N vs N-1
Tendances du marché
🎛️ Filtres Interactifs

Tous les tableaux de bord sont pilotés par des slicers dynamiques :

Ville
Quartier
Type de bien
Transaction
Catégorie de prix
Surface
Période

Les visualisations se mettent automatiquement à jour selon les filtres sélectionnés.

✅ Résultats

Ce projet permet :

La centralisation des données immobilières.
L'amélioration de la qualité des données.
La création d'un Data Warehouse analytique.
La production d'indicateurs métiers fiables.
L'analyse dynamique du marché immobilier marocain via Power BI.
