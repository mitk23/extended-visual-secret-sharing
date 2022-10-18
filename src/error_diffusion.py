import numpy as np

from constants import (
    BLACK,
    FILTER_FLOYD_STEINBERG,
    FILTER_JARVIS_JUDICE_NINKE,
    THRESH,
    WHITE,
)


def halftoning(img, diffusion_filter="jarvis"):
    """
    halftoning an image by error diffusion
    default filter: Jarvis-Judice-Ninke

    Parameters
    ----------
    img: np.ndarray[np.ndarray[np.uint8]]
        grayscale image

    Returns
    -------
    halftoned: np.ndarray[np.ndarray[np.uint8]]
        halftoned image
    """
    if diffusion_filter == "jarvis":
        halftoned = error_diffusion_jarvis(img)
    elif diffusion_filter == "floyd":
        halftoned = error_diffusion_floyd(img)
    else:
        raise ValueError("invalid diffusion filter")

    return halftoned


def error_diffusion_jarvis(img):
    """
    error diffusion by Jarvis-Judice-Ninke filter
    """
    H, W = img.shape[:2]

    img_diffused = img.astype(np.float64)

    for row in range(H - 2):
        for col in range(2, W - 2):
            if img_diffused[row, col] < THRESH:
                err = img_diffused[row, col] - BLACK
                img_diffused[row, col] = BLACK
            else:
                err = img_diffused[row, col] - WHITE
                img_diffused[row, col] = WHITE

            img_diffused[row : row + 3, col - 2 : col + 3] += (
                err * FILTER_JARVIS_JUDICE_NINKE
            )

    img_diffused = np.clip(img_diffused, BLACK, WHITE).astype(np.uint8)

    return img_diffused


def error_diffusion_floyd(img):
    """
    error diffusion by Floyd-Steinberg filter
    """
    H, W = img.shape[:2]

    img_diffused = img.astype(np.float64)

    for row in range(H - 1):
        for col in range(1, W - 1):
            if img_diffused[row, col] < THRESH:
                err = img_diffused[row, col] - BLACK
                img_diffused[row, col] = BLACK
            else:
                err = img_diffused[row, col] - WHITE
                img_diffused[row, col] = WHITE

            img_diffused[row : row + 2, col - 1 : col + 2] += (
                err * FILTER_FLOYD_STEINBERG
            )

    img_diffused = np.clip(img_diffused, BLACK, WHITE).astype(np.uint8)

    return img_diffused


def parallel_error_diffusion(img0, img1, img2):
    pass
