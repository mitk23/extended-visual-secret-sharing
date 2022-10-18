import random

import numpy as np

import constants


def vss_bits_combination(pix_val):
    pattern_dict = {"black": (0, 1), "white": (0, 0)}

    if pix_val > constants.THRESH:
        pattern = pattern_dict["white"]
    else:
        pattern = pattern_dict["black"]

    return pattern


def get_vss_bits(pix_val):
    pat1, pat2 = vss_bits_combination(pix_val)

    bits1 = constants.VSS_BITS[pat1]
    bits2 = constants.VSS_BITS[pat2]

    return bits1, bits2


def vss(secret):
    """
    implementation of VSS: visual secret sharing
    create two sheets sharing the secret image with 2x2 subpixels

    Parameters
    ----------
    secret: np.ndarray[np.ndarray, np.uint8]
        secret image to be encrypted in unsigned int8

    Returns
    -------
    res_sheet1: np.ndarray[np.ndarray, np.uint8]
    res_sheet2: np.ndarray[np.ndarray, np.uint8]
    """

    H, W = secret.shape[:2]

    res_sheet1 = np.zeros((H * 2, W * 2), np.uint8)
    res_sheet2 = np.zeros((H * 2, W * 2), np.uint8)

    for row in range(H):
        for col in range(W):
            bits1, bits2 = get_vss_bits(secret[row, col])

            # randomize subpixel bit pattern
            rand = random.sample(range(4), 4)
            for r in range(2):
                for c in range(2):
                    i = rand[r * 2 + c]
                    res_sheet1[row * 2 + r, col * 2 + c] = bits1[i]
                    res_sheet2[row * 2 + r, col * 2 + c] = bits2[i]

    return res_sheet1, res_sheet2


def decode(sheet1, sheet2):
    return np.minimum(sheet1, sheet2)
