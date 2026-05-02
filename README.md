# INF 451 - Yin-Yang

Ce projet est un solveur de puzzles Yin-Yang utilisant une approche par **SAT Solving**. Il transforme les règles du jeu en logique propositionnelle (format DIMACS) et utilise le solveur **minisat** pour trouver une solution valide.

## 📋 Description du Problème

Le Yin-Yang se joue sur une grille. Le but est de remplir chaque case avec un cercle noir ou blanc selon les règles suivantes:

* **Connectivité** : Toutes les cases blanches doivent être connectées entre elles (horizontalement ou verticalement).
* **Connectivité (Noir)** : Il en va de même pour toutes les cases noires.
* **Pas de carré 2x2** : Aucun carré de $2 \times 2$ ne doit être rempli de la même couleur.

## 🚀 Fonctionnalités

* **Interface Graphique (Pygame)** : Pour dessiner la grille initiale et visualiser la solution.
* **Système de Sauvegarde** : Possibilité de sauvegarder et charger des grilles personnalisées au format JSON.
* **Moteur SAT** : Encodage automatique des contraintes de jeu en format DIMACS.
* **Interfaçage Minisat** : Utilisation du solveur minisat pour une résolution rapide et efficace.

## 🛠️ Prérequis

Pour faire fonctionner ce projet, vous devez avoir installé :

* **Python 3.x** 
* **Pygame** : `pip install pygame` 
* **Minisat** : Le binaire minisat doit être accessible dans votre variable d'environnement PATH (utilisé par la fonction `subprocess`).

## 📁 Structure du Projet

* `main.py` : Point d'entrée principal. Gère le flux logique (input -> encodage -> minisat -> décodage -> output).
* `interface.py` : Contient les classes `InputInterface` et `OutputInterface` pour la gestion de la fenêtre Pygame.
* `dimac_coder.py` : Cœur algorithmique gérant la conversion de la matrice de jeu en variables et clauses logiques.
* `/custom_matrices` : Dossier contenant vos grilles sauvegardées.
* `/dimac` : Dossier temporaire stockant les fichiers d'entrée/sortie pour le solveur SAT.

## 🕹️ Utilisation

### 1. Lancement
Lancez le script principal:
```bash
python main.py
```

### 2. Configuration de la grille
À l'invite de commande:
* Entrez un nombre (ex: 6) pour créer une grille vide de $6 \times 6$.
* Entrez `load <nom_du_fichier>` pour charger une grille existante depuis le dossier `custom_matrices`.

### 3. Édition (Interface Input)
* **Clic gauche** : Alterne l'état d'une case (Vide -> Blanc -> Noir).
* **Touche S** : Sauvegarde la configuration actuelle.
* **Touche ENTRÉE** : Lance la résolution.

### 4. Résultat (Interface Output)
* Si une solution est trouvée, elle s'affiche à l'écran.
* Si le problème est **UNSATISFIABLE**, un message s'affichera dans la console.
* Appuyez sur **ENTRÉE** pour quitter.

## 🧠 Détails de l'Encodage

Le script `dimac_coder.py` transforme la grille en variables booléennes:

* **Variables de cellule** : Une variable par case (Vrai si Blanc, Faux si Noir).
* **Variables de connectivité** : Variables additionnelles gérant les relations entre les cases pour garantir qu'aucune île de couleur n'est isolée.
* **Clauses** :
    * Clauses unitaires pour les indices imposés.
    * Clauses d'exclusion pour empêcher les blocs de $2 \times 2$.
    * Contraintes de connectivité (modélisation de chemins).