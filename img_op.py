import cv2

im1=cv2.imread('lena.jpg',-1)       #for grayscale,1 for color, -1 for original //
print(im1)                          #prints matrix of image
cv2.imshow('image',im1)             #show image
k=cv2.waitKey(0) & 0xFF                     #pause image    #oxff is for some 64 bits in case it doesnt work
if k == 27:                             #if esc
    cv2.destroyAllWindows()             #close all windows
    print("not saved")
elif  k== ord('s'):
    cv2.imwrite('lena_copy.png',im1)    #copy image to new file name lena_copy
    cv2.destroyAllWindows()
    print("saved")
