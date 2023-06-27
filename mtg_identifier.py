import cv2
import numpy as np
import csv

def imgList():
   names=[]
   with open("mtgcards.csv", 'r') as file:
      csvreader = csv.reader(file)
      for row in csvreader:
         names.append(row)
   return names

def error(img1, img2):
   diff = cv2.subtract(img1, img2)
   err = np.sum(diff**2)
   mse = err/(float(h*w))
   return mse, diff

cam = cv2.VideoCapture(0)
while True:
    check, frame = cam.read()
    cv2.imshow('video', frame)
    key = cv2.waitKey(1)
    if key == ord('c'):
        check, frame = cam.read()
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        break
cam.release()
cv2.destroyAllWindows()

errorList = []
names = imgList()
for i in range(len(names)):
   current = str((names[i][0]))
   img1 = cv2.imread(current+".jpg")
   img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
   h, w = img1.shape
   img2 = cv2.resize(frame, (w, h))
   img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
   match_error12, diff12 = error(img1, img2)
   errorList.append([match_error12, current])
match = min(errorList)
print("The card is most similar to", match[1], "with an error of", match[0])
cv2.imshow('image',frame)
cv2.waitKey(0)

