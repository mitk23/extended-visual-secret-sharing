import sys

import cv2


def is_equal_img_size(*img_list):
    """
    Parameters
    ----------
    img_list: List[numpy.ndarray]
        list of cv2 images
    """
    res = all(img.shape == img_list[0].shape for img in img_list)
    return res


def read_image(img_fname):
    """
    read an image file and return its data

    Parameters
    ----------
    img_fname: str
        image file name

    Returns
    -------
    img: numpy.ndarray
    """
    img = cv2.imread(img_fname)

    if img is None:
        print(f"no image file: {img_fname}", file=sys.stderr)
        sys.exit(1)

    return img


def img2gray(img):
    """
    grayscale an image

    Parameters
    ----------
    img: numpy.ndarray
        cv2 image file

    Returns
    -------
    gray: numpy.ndarray
        cv2 image file (grayscale)
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray
