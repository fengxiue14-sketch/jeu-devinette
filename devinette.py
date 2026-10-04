#!/usr/bin/env python3
"""
Jeu du Devinette - Projet 04 de la Forteresse YUAN.
L'utilisateur doit deviner un nombre aleatoire.
"""

import json
import random
import sys
from pathlib import Path
from datetime import datetime


SCORES_FILE = Path(__file__).parent / "scores.json"

DIFFICULTES = {
    "1": {"nom": "Facile",    "max": 50,  "essais": 10},
    "2": {"nom": "Moyen",     "max": 100, "essais": 7},
    "3": {"nom": "Difficile", "max": 500, "essais": 10},
}


def charger_scores():
    """Charge les scores depuis scores.json."""
    if not SCORES_FILE.exists():
        return {}
    try:
        with open(SCORES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}


def sauvegarder_scores(scores):
    """Sauvegarde les scores dans scores.json."""
    try:
        with open(SCORES_FILE, "w", encoding="utf-8") as f:
            json.dump(scores, f, ensure_ascii=False, indent=2)
    except IOError as e:
        print(f"[AVERTISSEMENT] Impossible de sauvegarder : {e}", file=sys.stderr)


def afficher_titre(titre):
    """Affiche un titre encadre."""
    print()
    print("=" * 50)
    print(f"  {titre}")
    print("=" * 50)


def choisir_difficulte():
    """Menu de choix de difficulte."""
    afficher_titre("Choisis ta difficulte")
    for key, diff in DIFFICULTES.items():
        print(f"  {key}. {diff['nom']:10} (1-{diff['max']:3}, {diff['essais']} essais max)")
    print("  0. Retour")
    print("=" * 50)
    
    while True:
        choix = input("Ton choix : ").strip()
        if choix == "0":
            return None
        if choix in DIFFICULTES:
            return choix
        print("Choix invalide.")


def jouer_partie(diff_key):
    """Boucle d'une partie."""
    diff = DIFFICULTES[diff_key]
    cible = random.randint(1, diff["max"])
    max_essais = diff["essais"]
    essais = 0
    
    afficher_titre(f"Partie - {diff['nom']}")
    print(f"J'ai choisi un nombre entre 1 et {diff['max']}.")
    print(f"Tu as {max_essais} essais pour le trouver.\n")
    
    while essais < max_essais:
        reste = max_essais - essais
        print(f"[Essai {essais + 1}/{max_essais} - {reste} restant(s)]")
        
        try:
            ligne = input("Ton nombre : ").strip()
            if ligne.lower() in ("quit", "q", "abandon"):
                print(f"\nTu abandonnes. Le nombre etait : {cible}")
                return None
            
            proposition = int(ligne)
            essais += 1
            
            if proposition < 1 or proposition > diff["max"]:
                print(f"Hors limites ! Entre 1 et {diff['max']}.\n")
                essais -= 1
                continue
            
            if proposition == cible:
                print(f"[BINGO] Trouve en {essais} essai(s) ! Le nombre etait {cible}.")
                return essais
            elif proposition < cible:
                print("Trop petit !\n")
            else:
                print("Trop grand !\n")
        
        except ValueError:
            print("Entre un nombre valide.\n")
    
    print(f"[PERDU] Tu as epuise tes essais. Le nombre etait : {cible}")
    return None


def afficher_scores(scores):
    """Affiche les meilleurs scores."""
    afficher_titre("Meilleurs scores")
    
    if not scores:
        print("  Aucun score enregistre. Joue une partie !")
        return
    
    for diff_key, diff in DIFFICULTES.items():
        key = diff["nom"]
        if key in scores and scores[key]:
            meilleur = min(scores[key])
            parties = len(scores[key])
            print(f"  {key:10} : meilleur = {meilleur} essai(s), {parties} partie(s)")
        else:
            print(f"  {key:10} : aucun score")


def enregistrer_score(scores, diff_key, essais):
    """Ajoute un score."""
    diff = DIFFICULTES[diff_key]
    key = diff["nom"]
    
    if key not in scores:
        scores[key] = []
    
    scores[key].append({
        "essais": essais,
        "timestamp": datetime.now().isoformat(),
    })
    
    # Garder seulement les 20 meilleurs
    scores[key] = sorted(scores[key], key=lambda x: x["essais"])[:20]


def menu_principal():
    """Menu principal."""
    scores = charger_scores()
    
    while True:
        afficher_titre("JEU DU DEVINETTE")
        print("  1. Nouvelle partie")
        print("  2. Voir les scores")
        print("  3. Quitter")
        print("=" * 50)
        
        choix = input("Ton choix : ").strip()
        
        if choix == "1":
            diff_key = choisir_difficulte()
            if diff_key is None:
                continue
            
            essais = jouer_partie(diff_key)
            if essais is not None:
                enregistrer_score(scores, diff_key, essais)
                sauvegarder_scores(scores)
                print("Score enregistre !")
        
        elif choix == "2":
            afficher_scores(scores)
        
        elif choix == "3":
            print("\nAu revoir !")
            break
        
        else:
            print("Choix invalide.")


def main():
    """Point d'entree."""
    print("=" * 50)
    print("  JEU DU DEVINETTE v1.0")
    print("  Projet 04 - Forteresse YUAN")
    print("=" * 50)
    
    try:
        menu_principal()
    except KeyboardInterrupt:
        print("\n\nInterrompu. Au revoir !")
        return 1
    except Exception as e:
        print(f"\n[FATAL] {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

