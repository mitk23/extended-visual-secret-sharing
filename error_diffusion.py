import numpy as np

import constants


def error_diffusion(img):
    """
    halftoning an image by error diffusion
    default filter: Jarvis-Judice-Ninke

    Parameters
    ----------
    img: np.ndarray[np.ndarray, np.uint8]
        grayscale image

    Returns
    -------
    img_diffused: np.ndarray[np.ndarray, np.uint8]
        halftoned image
    """
    err_filter = constants.FILTER_JARVIS_JUDICE_NINKE

    H, W = img.shape[:2]

    img_diffused = img.astype(np.float64)

    for row in range(H - 2):
        for col in range(2, W - 2):
            if img_diffused[row, col] < constants.THRESH:
                err = img_diffused[row, col] - constants.BLACK
                img_diffused[row, col] = constants.BLACK
            else:
                err = img_diffused[row, col] - constants.WHITE
                img_diffused[row, col] = constants.WHITE

            img_diffused[row : row + 3, col - 2 : col + 3] += err * err_filter

    img_diffused = np.clip(img_diffused, constants.BLACK, constants.WHITE).astype(
        np.uint8
    )

    return img_diffused


def parallel_error_diffusion(img0, img1, img2):
    pass
