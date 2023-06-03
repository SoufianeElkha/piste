---
title:  "VISNUM: Projet 2"
author: Soufiane El kharmoudi
---

# Détecter l'orientation des pistes

### Ligne de commande pour exécuter le programme
```python
python3 labo_2.py lszh.png
```
## Description de ma procédure

1. tout d’abord, j’ai lu l’image en rgb
## Image Originale

![Iszh](src/lszh.png)

2. J’ai effectué la transformation de l’image en gris

![img_gray](src/fig/img_gray.png)

4. Effectué la binarisation de l’image de couleur grise

![img_bin](src/fig/img_bin.png)

3. J’ai appliqué la fonction Canny pour déterminer les contours. Déviation du filtre gaussien réglée à 6.3

![img_edges](src/fig/img_edges.png)

4. Application de la fonction hough_line_peaks après avoir préparé les données d’angle via np.linspace et l’utilisation de la fonction hough_line en passant les coins à calculer la transformée.

5. Le but de la transformation de Hough est d’identifier quels contours représentent une ligne droite : si plusieurs pixels de Edge sont alignés, même s’ils ne sont pas connectés entre eux, une ligne est détectée dans l’image.

6. Threshold : seuil sur le nombre d’intersections à obtenir pour qu’une ligne soit identifiée comme telle.

7. theta : mesure en radians l’angle de quantification dans la représentation sous forme normale.

8. La fonction me retourne un point d’angle. Étant une droite, si je trouve l’anclation d’un point, pour trouver l’autre angle, il suffit d’ajouter 180 degrés.

![tight_layout](src/fig/tight_layout.png)

9. Ci-dessous, mon programme a identifié 3 pistes avec les angles suivants par rapport au nord :

![tight_layout](src/fig/resultat.png)
