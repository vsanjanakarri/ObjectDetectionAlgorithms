import cv as a

o = a.LoadImage('s.png', a.CV_LOAD_IMAGE_COLOR)
i = a.CreateImage(a.GetSize(o), 8, 1)
a.CvtColor(o, i, a.CV_BGR2GRAY)


element = a.CreateStructuringElementEx(5*2+1, 5*2+1, 5, 5, a.CV_SHAPE_RECT)

a.MorphologyEx(i, i, None, element, a.CV_MOP_OPEN) 
a.MorphologyEx(i, i, None, element, a.CV_MOP_CLOSE)
a.Threshold(i, i, 128, 255, a.CV_THRESH_BINARY_INV)



vals = a.CloneImage(i) 
contours=a.FindContours(vals, a.CreateMemStorage(0), a.CV_RETR_LIST, a.CV_CHAIN_APPROX_SIMPLE, (0,0))

_red = (0, 0, 255); #Red for external contours
_green = (0, 255, 0);# Green internal contours
levels=2 #1 contours drawn, 2 internal contours as well 
a.DrawContours (o, contours, _red, _green, levels, 2, a.CV_FILLED) 

a.ShowImage("Image", o)
a.WaitKey(0)
