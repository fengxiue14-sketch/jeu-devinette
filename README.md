# Jeu du Devinette

Quatrieme projet de la **Forteresse YUAN**.

## Objectif

Jeu interactif en Python : trouver un nombre aleatoire choisi par l'ordinateur.

## Fonctionnalites

- 3 niveaux de difficulte :
  - Facile : 1-50, 10 essais
  - Moyen : 1-100, 7 essais
  - Difficile : 1-500, 10 essais
- Retour utilisateur (trop grand / trop petit)
- Historique des scores (top 20 par difficulte)
- Persistance JSON
- Gestion d'abandon (taper quit/q)

## Installation

Aucune dependance externe. Python 3.10+ requis.

## Usage

    python devinette.py

Puis naviguer :

    1. Nouvelle partie
    2. Voir les scores
    3. Quitter

## Exemple de partie

    Partie - Facile
    J'ai choisi un nombre entre 1 et 50.
    Tu as 10 essais.

    [Essai 1/10 - 10 restant(s)]
    Ton nombre : 25
    Trop petit !

    [Essai 2/10 - 9 restant(s)]
    Ton nombre : 40
    Trop grand !

    [Essai 3/10 - 8 restant(s)]
    Ton nombre : 32
    [BINGO] Trouve en 3 essai(s) !

## Competences acquises

- Module random (random.randint)
- Boucles imbriquees (jeu dans menu)
- Comparaisons conditionnelles
- Persistance de scores en JSON
- Gestion d'abandon
- Structure de game loop
- Validation d'entree (hors limites)

## Auteur

**FENG XIUE** - https://github.com/fengxiue14-sketch

## Licence

MIT
