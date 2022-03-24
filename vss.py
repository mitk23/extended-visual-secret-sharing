import random
import numpy as np
from error_diffusion import error_diffusion
import constants

def vss(img):
  '''
  this function implements VSS (visual secret sharing)
  create two sheets sharing the secret image with 2x2 subpixels

  Parameters
  ----------
  img: np.ndarray[np.ndarray, np.uint8]
    secret image to be encrypted in unsigned int8

  Returns
  -------
  sheet0: np.ndarray[np.ndarray, np.uint8]
  sheet1: np.ndarray[np.ndarray, np.uint8]
  '''

  H, W = img.shape[:2]
  
  sheet0 = np.zeros((H*2, W*2), np.uint8)
  sheet1 = np.zeros((H*2, W*2), np.uint8)

  for row in range(H):
    for col in range(W):
      pat = 0 if img[row, col] > constants.THRESH else 1

      # randomize subpixel bit pattern
      rand = random.sample(range(4), 4)
      for r in range(2):
        for c in range(2):
          sheet0[row*2 + r, col*2 + c] = constants.VSS_BITS[constants.VSS_PATTERN[pat][0]][rand[r*2+c]]
          sheet1[row*2 + r, col*2 + c] = constants.VSS_BITS[constants.VSS_PATTERN[pat][1]][rand[r*2+c]]

  return sheet0, sheet1


def evss(img_sheet0, img_sheet1, img_secret, halftoning=True):
  '''
  this function implements EVSS (extended visual secret sharing)
  create two sheets and an encrypted secret image by EVSS scheme

  Parameters
  ----------
  img_sheet0: np.ndarray[np.ndarray]
    to be first distributed image
  img_sheet1: np.ndarray[np.ndarray]
    to be second distributed image
  img_secret: np.ndarray[np.ndarray]
    secret image to be encrypted 
  '''
  if halftoning:
    img_sheet0 = error_diffusion(img_sheet0)
    img_sheet1 = error_diffusion(img_sheet1)
    img_secret = error_diffusion(img_secret)
  
  H, W = img_secret.shape[:2]
  
  sheet0 = np.zeros((H*2, W*2), np.uint8)
  sheet1 = np.zeros((H*2, W*2), np.uint8)

  for row in range(H):
    for col in range(W):
      pat = (img_sheet0[row, col] < constants.THRESH) << 2 \
        | (img_sheet1[row, col] < constants.THRESH) << 1 \
        | (img_secret[row, col] < constants.THRESH)
      
      rand = random.sample(range(4), 4)
      for r in range(2):
        for c in range(2):
          sheet0[row*2+r, col*2+c] = constants.EVSS_BITS[constants.EVSS_PATTERN[pat][0]][rand[r*2+c]]
          sheet1[row*2+r, col*2+c] = constants.EVSS_BITS[constants.EVSS_PATTERN[pat][1]][rand[r*2+c]]
  
  return sheet0, sheet1


def decode(sheet0, sheet1):
  return np.minimum(sheet0, sheet1)
