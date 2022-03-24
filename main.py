import cv2
import vss
import util

def main():
  img_sheet0, img_sheet1, img_secret = util.read_3images()

  # grayscale
  img_sheet0 = cv2.cvtColor(img_sheet0, cv2.COLOR_BGR2GRAY)
  img_sheet1 = cv2.cvtColor(img_sheet1, cv2.COLOR_BGR2GRAY)
  img_secret = cv2.cvtColor(img_secret, cv2.COLOR_BGR2GRAY)

  # encrypt
  sheet0, sheet1 = vss.evss(img_sheet0, img_sheet1, img_secret)
  decoded = vss.decode(sheet0, sheet1)

  # show
  cv2.imshow('Sheet0', sheet0)
  cv2.imshow('Sheet1', sheet1)
  cv2.imshow('Decoded', decoded)

  print('press any key to terminate viewing')

  cv2.waitKey(0)
  cv2.destroyAllWindows()


if __name__ == '__main__':
  main()
