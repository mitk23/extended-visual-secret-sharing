import sys

import cv2


def read_image():
    """
    read an image file and return its data

    Returns
    -------
    img: numpy.ndarray
    """
    if len(sys.argv) < 2:
        fname = input("image file path -> ")
    else:
        fname = sys.argv[1]

    img = cv2.imread(fname)

    if img is None:
        print("Error: no image file: {}" % fname, file=sys.stderr)
        sys.exit(1)

    return img


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
