import sys
import matplotlib.image as mpimg

import labo_2_lib as l2lib

if __name__ == "__main__":
  # lecture de l'argument passé à la CLI
  img_fn = sys.argv[1]
  print("Input path:", img_fn)
  # lecture, traitement et affichage du résultat
  img = mpimg.imread(img_fn)
  runways = l2lib.process(img)
  print("LSZH detected runways:")
  print(runways)

