import cv as c

i=c.LoadImage('s.png')


a = c.CloneImage(i)
c.MorphologyEx(i, a, None, None, c.CV_MOP_GRADIENT)

c.Threshold(a, a, 30, 255, c.CV_THRESH_BINARY_INV)

c.ShowImage("original",i)
c.ShowImage("Object Detected",a)

c.WaitKey(0)
