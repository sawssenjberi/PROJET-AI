# Application Clinique de Détection et Diagnostic des Lésions Cutanées par Intelligence Artificielle

## Contexte
Dans la pratique clinique courante, la forte demande d'expertises dermatologiques et la subtilité visuelle des lésions cutanées peuvent retarder les diagnostics. Ce projet s'inscrit dans le développement de la e-santé en proposant une solution d'assistance numérique. Il s'appuie sur la synergie entre le développement web et le deep learning pour mettre les algorithmes de pointe au service du personnel médical, optimisant ainsi le flux de prise en charge des patients.

## Objectifs
- Fournir un outil d'aide à la décision clinique capable de classifier instantanément les images dermatologiques en catégories bénignes ou malignes.
- Développer une interface utilisateur hautement sécurisée qui respecte la confidentialité des données médicales et limite l'accès aux professionnels de santé.
- Garantir une excellente transparence des résultats fournis par l'intelligence artificielle en calculant et en affichant un score de confiance précis pour chaque analyse.
- Permettre un suivi médical continu et structuré à travers l'archivage automatique de l'historique des consultations.

## Fonctionnalités

### Système d'Authentification Clinique
Portail de connexion obligatoire et sécurisé pour filtrer les accès de l'établissement de santé, protégeant ainsi l'application et les dossiers confidentiels.

### Tableau de Bord Centralisé
Interface d'accueil épurée facilitant la navigation globale du médecin et offrant un accès rapide aux différents espaces de travail de la plateforme.

### Analyse IA et Diagnostic en Temps Réel
Module de téléchargement d'images dermatologiques qui transmet les clichés au modèle de réseau de neurones VGG16, générant une prédiction immédiate accompagnée d'une jauge visuelle de certitude.

### Registre de l'Historique des Analyses
Banque de données centralisée regroupant l'ensemble des fiches des patients et les bilans des examens passés pour faciliter la consultation et le suivi à long terme.

## Technologies Utilisées
- **Python :** Langage principal utilisé pour le développement de la logique serveur et l'intégration des scripts scientifiques.
- **TensorFlow & Keras :** Frameworks de deep learning exploités pour charger le modèle de réseau de neurones convolutif (CNN) et exécuter les prédictions algorithmiques.
- **VGG16 :** Architecture de réseau pré-entraînée et fine-tunée, spécialisée dans la reconnaissance de motifs complexes et l'extraction de caractéristiques sur les images médicales.
- **Flask :** Micro-framework Python choisi pour orchestrer le routage de l'application, gérer les sessions utilisateurs et faire le pont entre l'interface utilisateur et le modèle IA.
- **SQLite / Base de données locale :** Système de stockage léger implémenté pour enregistrer de manière structurée les informations des patients et l'historique de leurs diagnostics.
---

## Guide Visuel et Captures d'Écran du Projet

### 1. Page de Connexion (Login)
![Login Screen](screenshots/login.png.png)

### 2. Tableau de Bord (Dashboard)
![Dashboard Screen](screenshots/dashboard.png.png)

### 3. Page de Diagnostic (Upload)
![Upload Screen](screenshots/upload.png.png)

### 4. Résultat du Diagnostic (Analyse)
![Result Screen](screenshots/resultat.png.png)

### 5. Registre de l'Historique des Analyses
![Historique Screen](screenshots/historique.png.png)
