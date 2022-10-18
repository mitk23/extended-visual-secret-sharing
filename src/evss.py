import random

import numpy as np

from constants import EVSS_BITS, EVSS_PATTERN, THRESH
from error_diffusion import halftoning


def evss_bits_combination(px1, px2, px3, combination_list=EVSS_PATTERN):
    ind = (px1 < THRESH) << 2 | (px2 < THRESH) << 1 | (px3 < THRESH)
    pattern = combination_list[ind]

    return pattern


def get_evss_bits(px1, px2, px3, combination_list=EVSS_PATTERN, bits_list=EVSS_BITS):
    pat1, pat2 = evss_bits_combination(px1, px2, px3, combination_list=combination_list)

    bits1 = bits_list[pat1]
    bits2 = bits_list[pat2]

    return bits1, bits2


def evss(sheet1, sheet2, secret, halftone=True, diffusion_filter="jarvis"):
    """
    implementation of EVSS (extended visual secret sharing)
    create two sheets and an encrypted secret image by EVSS scheme

    Parameters
    ----------
    sheet1: np.ndarray[np.ndarray]
        first image to be distributed
    sheet2: np.ndarray[np.ndarray]
        second image to be distributed
    secret: np.ndarray[np.ndarray]
        secret image to be encrypted
    """
    if halftone:
        sheet1 = halftoning(sheet1, diffusion_filter=diffusion_filter)
        sheet2 = halftoning(sheet2, diffusion_filter=diffusion_filter)
        secret = halftoning(secret, diffusion_filter=diffusion_filter)

    H, W = secret.shape[:2]

    res_sheet1 = np.zeros((H * 2, W * 2), np.uint8)
    res_sheet2 = np.zeros((H * 2, W * 2), np.uint8)

    for row in range(H):
        for col in range(W):
            bits1, bits2 = get_evss_bits(
                sheet1[row, col], sheet2[row, col], secret[row, col]
            )

            rand = random.sample(range(4), 4)
            for r in range(2):
                for c in range(2):
                    i = rand[r * 2 + c]
                    res_sheet1[row * 2 + r, col * 2 + c] = bits1[i]
                    res_sheet2[row * 2 + r, col * 2 + c] = bits2[i]

    return res_sheet1, res_sheet2
