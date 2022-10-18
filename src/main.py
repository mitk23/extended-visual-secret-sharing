import cv2

import util
import vss


def main(args):
    # read image
    sheet1 = util.read_image(args.sheet1)
    sheet2 = util.read_image(args.sheet2)
    secret = util.read_image(args.secret)

    # grayscale
    sheet1 = util.img2gray(sheet1)
    sheet2 = util.img2gray(sheet2)
    secret = util.img2gray(secret)

    # encrypt
    # sheet0, sheet1 = vss.evss(img_sheet0, img_sheet1, img_secret)
    res_sheet1, res_sheet2 = vss.vss(secret)
    encrypted = vss.decode(res_sheet1, res_sheet2)

    # show
    cv2.imshow("Sheet0", res_sheet1)
    cv2.imshow("Sheet1", res_sheet2)
    cv2.imshow("Encrypted", encrypted)

    print("-" * 20, "press any key to terminate viewing", "-" * 20)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("sheet1", help="the first image to be the result of encryption")
    parser.add_argument(
        "sheet2", help="the second image to be the result of encryption"
    )
    parser.add_argument("secret", help="an image to be encrypted")

    args = parser.parse_args()

    main(args)
