# Parisian-Metro-Graph // Vianavigo

> Graph and shortest path theory applied to the parisian subway network.
>
> Dev date : 23/01/2015 (Re-upload)

This project is an implementation of the Vianavigo application that offers
a route search on the Parisian rail network (subway).

To start the route search, use this type of syntax :

`python mon_via_navigo.py Station_1 Station_2`

If your station's name have a space (for example "Gare de l'est")
please use '_' to separate the words (so you have "Gare_de_l*est")

`python mon_via_navigo.py Blanche Gare_de_l*est`

## Example

```
[code]$ python3 mon_via_navigo.py Blanche Jussieu
*******************************************************
                     VIA_NAVIO
*******************************************************
Depart  : Blanche
Arrivee : Jussieu
*******************************************************
ligne 2B :
| Blanche
| Place de Clichy
v
ligne 13A1:
| Place de Clichy
| Liège
| Saint-Lazare
v
ligne 3A:
| Saint-Lazare
| Havre Caumartin
| Opéra
v
ligne 7A2:
| Opéra
| Pyramides
| Palais Royal, Musée du Louvre
| Pont-Neuf
| Châtelet
| Pont-Marie
| Sully Morland
| Jussieu
v
*******************************************************
Duree estimee : 13.0 Min
```

## Install

```
python pip install math numpy matplotlib 
```

## Note

- You can plot the map of the subway only with Python 2.7 so run `python mon_via_navigo.py Blanche Gare_du_Nord` if you want to have a graph, and `python3 mon_via_navigo.py Blanche Gare_du_Nord` otherwise
- If you have a space " " in the name of your station use a "_" to fake it
- If you have a coma "'" in the name of your station use a "*" to fake it :) 

## Licence

- MIT
