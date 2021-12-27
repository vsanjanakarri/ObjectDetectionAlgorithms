import cv as a
import math 

i = a.LoadImage("s.png", a.CV_LOAD_IMAGE_GRAYSCALE)
i2 = a.CloneImage(i)


eigImage = a.CreateMat(i.height, i.width, a.IPL_DEPTH_32F)
tempImage = a.CloneMat(eigImage)
cornerCount = 500
quality = 0.01
minDistance = 10

corners = a.GoodFeaturesToTrack(i, eigImage, tempImage, cornerCount, quality, minDistance)

radius = 3
thickness = 2

for (x,y) in corners:
    a.Circle(i, (int(x),int(y)), radius, (255,255,255), thickness)

a.ShowImage("Corner Detection", i)



a.WaitKey(0)
