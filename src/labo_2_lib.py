import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage import data, filters, morphology, feature
from skimage.transform import hough_line, hough_line_peaks
from matplotlib import cm

 # Transformation de l’image en gris
def image_gray(img):
  img_gray = rgb2gray(img[:, :, 0:3])
  plt.imsave('fig/img_gray.png', img_gray, cmap='gray')
  return img_gray

  # Application du filtre
def filtres_threshold(img_gray):
  t = filters.threshold_otsu(img_gray)
  return t
  
# Binarisation de l’aimmagine
def image_binarize(img_gray, t):
  img_bin = img_gray
  img_bin[img_bin < t] = 0
  img_bin[img_bin >= t] = 1
  plt.imsave('fig/img_bin.png', img_bin, cmap='gray')
  return img_bin

  #Detection des bords
def canny(img_bin):
  edges = feature.canny(img_bin, 6.3)
  plt.imsave('fig/img_edges.png', edges, cmap='gray')
  return edges

# Process

def process(img):

  runways = []

  img_gray = image_gray(img)
  t = filtres_threshold(img_gray)
  img_bin = image_binarize(img_gray, t)

  #Detection des bords
  edges = canny(img_bin)

  # Hough transform
  # précision degrés de 0,5
  tested_angles = np.linspace(-np.pi / 2, np.pi / 2, 360, endpoint=False)
  h, theta, d = hough_line(edges, theta=tested_angles)

  # Plot Figure 1
  fig, axes = plt.subplots(1, 3, figsize=(15, 6))
  ax = axes.ravel()

  ax[0].imshow(img, cmap=cm.gray)
  ax[0].set_title('Input image')
  ax[0].set_axis_off()

  angle_step = 0.5 * np.diff(theta).mean()
  d_step = 0.5 * np.diff(d).mean()
  bounds = [np.rad2deg(theta[0] - angle_step),
              np.rad2deg(theta[-1] + angle_step),
              d[-1] + d_step, d[0] - d_step]

  ax[1].imshow(np.log(1 + h), extent=bounds, cmap=cm.gray, aspect=1 / 1.5)
  ax[1].set_title('Hough transform')
  ax[1].set_xlabel('Angles (degrees)')
  ax[1].set_ylabel('Distance (pixels)')
  ax[1].axis('image')

  ax[2].imshow(edges, cmap=cm.gray)
  ax[2].set_ylim((edges.shape[0], 0))
  ax[2].set_axis_off()
  ax[2].set_title('Detected lines')

  #Application de la fonction hough_line_peaks
  for _, angle, dist in zip(*hough_line_peaks(h, theta, d, 15)):
      (x0, y0) = dist * np.array([np.cos(angle), np.sin(angle)])
      ax[2].axline((x0, y0), slope=np.tan(angle + np.pi/2))
      #Étant une droite, si je trouve l’angle d’un point, pour trouver l’autre angle, il suffit d’ajouter 180 degrés
      my_angle = np.degrees(angle)+180
      runways.append((round(my_angle/10), (round((my_angle/10)+180/10))))

  plt.savefig('fig/tight_layout.png', dpi=300)

  return runways
