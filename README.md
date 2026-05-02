# INF 451 - Solveur de Yin-Yang par SAT

## Membres

Brosse Arsene, L2 MIN, 12308501

## Description du Problème

Le Yin-Yang se joue sur une grille. Le but est de remplir chaque case avec un cercle noir ou blanc selon les règles suivantes:

* **Connectivité** : Toutes les cases d'une meme couleure doivent être connectées entre elles (horizontalement ou verticalement).
* **Pas de carré 2x2** : Aucun carré de $2 \times 2$ de la même couleur.

## Fonctionnalités

* **Interface Graphique (Pygame)** : Pour dessiner la grille initiale et visualiser la solution.
* **Système de Sauvegarde** : Possibilité de sauvegarder et charger des grilles personnalisées au format JSON.
* **Moteur SAT** : Encodage automatique des contraintes de jeu en format DIMACS.
* **Interfaçage Minisat** : Utilisation du solveur minisat pour une résolution rapide et efficace.

##  Prérequis

Pour faire fonctionner ce projet, vous devez avoir installé :

* **Python 3.x** 
* **Pygame** : `pip install pygame` ou `apt install python3-pygame`
* **Minisat** : Le binaire minisat doit être accessible dans votre variable d'environnement PATH (utilisé par la fonction `subprocess`).

## Structure du Projet

* `main.py` : Point d'entrée principal. (input -> encodage -> minisat -> décodage -> output).
* `interface.py` : Contient les classes `InputInterface` et `OutputInterface` pour la gestion de la fenêtre Pygame.
* `dimac_coder.py` : Cœur algorithmique gérant la conversion de la matrice de jeu en variables et clauses logiques.
* `/custom_matrices` : Dossier contenant vos grilles sauvegardées.
* `/dimac` : Dossier temporaire stockant les fichiers d'entrée/sortie pour le solveur SAT.

## Utilisation

### 1. Lancement
Une fois placez dans le repertoire principal, accordez les droits d'executions si necessaire:
```bash
chmod +x run.sh
```
puis executez:
```bash
./run.sh
```

### 2. Configuration de la grille
Dans l'invite de commande:
* Entrez un nombre (ex: 6) pour créer une grille vide de $6 \times 6$.
* Entrez `load <nom_du_fichier>` pour charger une grille existante depuis le dossier `custom_matrices`.

### 3. Édition (Interface Input)
* **Clic gauche** : Alterne l'état d'une case (Vide -> Blanc -> Noir).
* **Touche S** : Sauvegarde la configuration actuelle.
* **Touche ENTRÉE** : Lance la résolution.

### 4. Résultat (Interface Output)
* Si une solution est trouvée, elle s'affiche à l'écran.
* Si le problème est **UNSATISFIABLE**, un message s'affichera dans la console.
* Rappuyez sur **ENTRÉE** pour quitter.