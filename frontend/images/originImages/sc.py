import os
import cv2

def work(ptht, cnt, ord) :
	pth = "./" + ptht + ".png"
	print pth
	image = cv2.imread(pth, -1)
	cropImg = image[0:128, 23:23 + 82]
	for i in range(0, cnt) :
		cv2.imwrite("./" + str(ord + i) + ".png", cropImg)

for i in range(1, 10) :
	pth = "./man" + str(i) + ".png"
	image = cv2.imread(pth, -1)
	cropImg = image[0:128, 23:23 + 82]
	if i != 5 :
		cv2.imwrite("./" + str((i - 1) * 4) + ".png", cropImg)
	cv2.imwrite("./" + str((i - 1) * 4 + 1) + ".png", cropImg)
	cv2.imwrite("./" + str((i - 1) * 4 + 2) + ".png", cropImg)
	cv2.imwrite("./" + str((i - 1) * 4 + 3) + ".png", cropImg)
for i in range(1, 10) :
	pth = "./pin" + str(i) + ".png"
	image = cv2.imread(pth, -1)
	cropImg = image[0:128, 23:23 + 82]
	if i != 5 :
		cv2.imwrite("./" + str(36 + (i - 1) * 4) + ".png", cropImg)
	cv2.imwrite("./" + str(36 + (i - 1) * 4 + 1) + ".png", cropImg)
	cv2.imwrite("./" + str(36 + (i - 1) * 4 + 2) + ".png", cropImg)
	cv2.imwrite("./" + str(36 + (i - 1) * 4 + 3) + ".png", cropImg)
for i in range(1, 10) :
	pth = "./bamboo" + str(i) + ".png"
	image = cv2.imread(pth, -1)
	cropImg = image[0:128, 23:23 + 82]
	if i != 5 :
		cv2.imwrite("./" + str(72 + (i - 1) * 4) + ".png", cropImg)
	cv2.imwrite("./" + str(72 + (i - 1) * 4 + 1) + ".png", cropImg)
	cv2.imwrite("./" + str(72 + (i - 1) * 4 + 2) + ".png", cropImg)
	cv2.imwrite("./" + str(72 + (i - 1) * 4 + 3) + ".png", cropImg)

work("red-dora-man5", 1, 16)
work("red-dora-pin5", 1, 52)
work("red-dora-bamboo5", 1, 88)
work("wind-east", 4, 108)
work("wind-south", 4, 112)
work("wind-west", 4, 116)
work("wind-north", 4, 120)
work("dragon-haku", 4, 124)
work("dragon-green", 4, 128)
work("dragon-chun", 4, 132)