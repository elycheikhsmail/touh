# contexte :
le fichiers merged.txt contient les données de plus tableaux ayant des structures similaires, l'un est dessous de l'autre. chacun tables est composée de deux colonne : le premier colone resent x et le deuxième représente y et de plusieurs lignes comme dans l'exemple : ..
```
         Frequency / GHz                S1,1 (1)/abs,dB
----------------------------------------------------------------------
                       3                      -3.3716478
               3.0120001                      -3.3356269
               3.0239999                      -3.3022492
                   3.036                      -3.2715356
               3.0480001                      -3.2434861
```

le debut de chaque table est de la form :

```
         Frequency / GHz                S1,1 (n)/abs,dB
----------------------------------------------------------------------

```
où n designe un entier naturel positif comme : 1, 14 ,31 etc

# tache 
dooner un script python3 qui permet de extraitre le contenu contenue de chaque tableau et fusionner les dans un fichier tables.csv qui contient trois valeur x, y et tabeleIdex qui donne le numero du table