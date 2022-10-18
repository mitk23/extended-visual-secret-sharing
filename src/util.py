import sys

import cv2


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
    '''
    grayscale an image

    Parameters
    ----------
    img: numpy.ndarray
        cv2 image file

    Returns
    -------
    gray: numpy.ndarray
        cv2 image file (grayscale)
    '''
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray


def read_3images():
    """
    read three image files and return the data
    """
    if len(sys.argv) > 1:
        f1, f2, f3 = sys.argv[1:4]
    else:
        f1 = input("image file for sheet0 -> ")
        f2 = input("image file for sheet1 -> ")
        f3 = input("image file for secret -> ")

    img_sheet0 = cv2.imread(f1)
    img_sheet1 = cv2.imread(f2)
    img_secret = cv2.imread(f3)

    if img_sheet0 is None:
        print("Error: no image file: {}" % f1, file=sys.stderr)
        sys.exit(1)
    if img_sheet1 is None:
        print("Error: no image file: {}" % f2, file=sys.stderr)
        sys.exit(1)
    if img_secret is None:
        print("Error: no image file: {}" % f3, file=sys.stderr)
        sys.exit(1)

    if (
        (img_sheet0.shape != img_sheet1.shape)
        or (img_sheet0.shape != img_sheet1.shape)
        or (img_sheet1.shape != img_secret.shape)
    ):
        print("Error: images should have the same size", file=sys.stderr)
        sys.exit(1)

    return img_sheet0, img_sheet1, img_secret
