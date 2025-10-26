# Astar :

## Cette algo est une variante de djikstra qui fonctionne différement d'une maniere différente mais qui améliore l'éfficacité

---

`Pour le fonctionnement de celui-ci on part du principe que l'on a les coordonnées des villes`

## Le but de cette algo :

- C'est que l'on veut trouver le chemin le plus court en recherchant l'heuristique(la distance euclidienne) le plus court pour trouver le chemin sans avoir a comparer chaqu'une des routes

## Différence avec Djikstra :

1. On veut pouvoir comparer la sommes de heuristiques + celui la distance réel alors que dans djikstra on compare directement la valeur total du weight du noeud seul lequel on est par rapport aux autre et on recherche le voisin de celui qui à le plus petit.
2. Etant donner que l'on ne viste que la valeur avec la somme l'euclidienne + la distance réel du noeud actuelle la plus petite alors on vas éviter les detours inutile. Alors que dans djikstra on allait à partir du moment ou la valeur de la distance du voisin étais plus petite sans rien prendre d'autre en compte

## Définiton :

- Heuristique :

  > C'est l'héstimation de la distance qu'un noeud à jusqu'à la destination.

- Distance euclidienne :

> C'est le chemin le plus court possible entre deux élements en ligne droite. Et elle permet d'avoir une hestimation de la distance réel qu'il y a entre les deux éléments.
