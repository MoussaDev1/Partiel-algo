# Djikstra :

> Le but de l'algo permet de vérifier la distance totale la plus petite d'un lieu A à un lieu Z.

### Initialiser l'algo (variable)

#### Pour ce faire :

> Tout d'abord on créer des variable :

1. distance Node = infini pour chaque distance de chaque node.
   `pour données une distance initiale a toute les distances contenus dans les noeud en dehors de celui initial`.

2. distance[start] = 0 `Pour donnée à notre lieu initale la valeur de 0 pour marqué le début.`

3. visited = set() = Pour enregistrer les valeurs des lieux enregistrer.

4. **optionnel de mon côté : previous = `Pour enregister les valeurs des noeud sur surlesqulles on est passé.(pour avoir l'arbre entier des lieux sur les lesquelles l'on est passer.`**

##### On rentre dans la boucle principale de l'algo :

- Dans le quel on vas mettre une condition pour vérifier lorsque tout les noeud seront vérifier, si c'est le cas alors on en sort. Et qui nous permettra de remettre par défaut les variable du node actuelle et celui de la distance actuelle pour la prochaine itération.

---

> On veut dabord à rechercher quel est la distance la plus petite parmis les noeud qui n'ont pas été visited. Et à attribuer la valeur correspondante à la distance des noeud et ensuite les rendre visited :

#### Pour faire ceci :

- On se met dans un boucle qui nous permettra de vérifier l'intégralité des noeud (non visited).
- Et on regarde pour chaque noeud, si il n'a pas été vérfier et que sa distance est inférieure a la distance que l'on a dans le node sur lequel on itére actuellement, alors assigner sa valeurs a la distance du node ainsi que sa valeurs.

  > `C'est pour cette parti la que initaliement on a mis tout les distance des noeud a infini, comme étant donner que l'on aura pas une valeur plus grande que infini elle sera toujours attribuer lorsque que l'on passera dessus pour la premeire fois`

- On gère le cas des graphes non connexes, pour gerer un cas ou le graphe donnée n'est pas bon.
- Un fois que l'on a vérifier que tout étais bon on peut alors alors ajouter dans visited
  > `pour stipulé que l'on est bien passer dans le node pour ne pas avoir à revenir dessus lorsque l'on vérifiera les noeud sur les prochaines itération.`

---

> On assigne les valeurs des voisins avec les valeurs des distances + leurs weights initiale pour avoir la valeurs(weight) entier du chemin accomplis jusqu'au voisin de node de l'itération.

#### Pour faire ceci :

- On se met dans une boucle dans laquel on récupera le voisin et le le weight de celui-ci.
- Et on ajoute au weight la distance que l'on avait pour le node de notre itération encore une fois.
- Et si le weight est plus petit on assigne la distance au voisin.
  > `Comme ça on peut changer la valeurs du voision si lors d'un autre itération on voit que la distance déja parcourus est moins grande`

---

#### Pour finir on à previous qui nous permet de traquer le chemin emprunter a chaque étapes pour avoir le résultat final.

- On créer d'abord une variable dans laquel on initalise toute les valeurs a None.
- Ensuite on vérifie le node dans lequel on est dans l'itération, si la valeur du weight (distance) est plus petite dans celle de l'itération alors on assigne cette nouvelle valeurs dans previous.
  > `On fait ça pour pouvoir enregistrer la valeurs du meilleur moyens d'aller a un autre node. Et si l'on trouve mieux alors on on le change avec celui que l'on avait précédement `
- On veut ensuite afficher l'abre construit pour appercevoir le chemin final trouver.
