# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 22:47:34 2019

@author: Rakhee
"""

import cv2
import numpy as np

#cap = cv2.VideoCapture('white.mp4')
done = 1
publish = 0
count0 = 0
count1 = 0
count2 = 0 
count3 = 0
count4 = 0
count5 = 0 
count6 = 0
count7 = 0
count8 = 0 
count9 = 0
count10 = 0
count11 = 0 
count12 = 0 
count13 = 0
count14 = 0
count15 = 0
count16 = 0
while(True):
    #_, bgr_image = cap.read()
    
    bgr_image = cv2.imread('houghlines (2).jpg', 1)
    hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)
    
    # convert the images from bgr to hsv
    #hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)
    upper_green_range0 = np.array([50,50,50], dtype = "uint8")
    upper_green_range1 = np.array([70,255,255], dtype = "uint8")
    mask1 = cv2.inRange(hsv_image,  upper_green_range0 ,upper_green_range1)

    result = cv2.bitwise_and(bgr_image, bgr_image, mask = mask1)
    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred,25 , 255, cv2.THRESH_BINARY)[1]
    kernel = np.ones((5,5),np.uint8)
    thresh = cv2.erode(thresh,kernel,iterations = 1)

    upper_blue_range0 = np.array([110,50,50], dtype = "uint8")
    upper_blue_range1 = np.array([130,255,255], dtype = "uint8")
    mask2 = cv2.inRange(hsv_image,  upper_blue_range0 ,upper_blue_range1)
    #print("Input Image Shape is %d, %d" %(bgr_image.shape[0], bgr_image.shape[1]))
    
    result2 = cv2.bitwise_and(bgr_image, bgr_image, mask = mask2)
    gray2 = cv2.cvtColor(result2, cv2.COLOR_BGR2GRAY)
    blurred2 = cv2.GaussianBlur(gray2, (5, 5), 0)
    thresh2 = cv2.threshold(blurred2,25 , 255, cv2.THRESH_BINARY)[1]
    kernel = np.ones((5,5),np.uint8)
    thresh2 = cv2.erode(thresh2,kernel,iterations = 1)

    x_start = 159
    y_start = 70
    y_end = 408
    x_end = 505
    x_stride = int((x_end - x_start)/4)
    y_stride = int((y_end - y_start)/4)

    x1 = 159
    x2 = x1 + x_stride
    x3 = x2 + x_stride
    x4 = x3 + x_stride
    x5 = x4 + x_stride

    y1 = 70
    y2 = y1 + y_stride
    y3 = y2 + y_stride
    y4 = y3 + y_stride
    y5 = y4 + y_stride
    print(x1,x2,x3,x4,x5)
    print(y1,y2,y3,y4,y5)
    #print(int(x_stride), int(y_stride))
    # Tic Tac Toe Board Construction
    cv2.line(bgr_image,(int(x1),0),(int(x1),y_end),(0,0,0),1)
    cv2.line(bgr_image,(int(x2),0),(int(x2),y_end),(0,0,0),1)
    cv2.line(bgr_image,(int(x3),0),(int(x3),y_end),(0,0,0),1)
    cv2.line(bgr_image,(int(x4),0),(int(x4),y_end),(0,0,0),1)
    cv2.line(bgr_image,(int(x5),0),(int(x5),y_end),(0,0,0),1)

    cv2.line(bgr_image,(0,int(y2)),(int(x1),int(y3)),(0,0,0),2)
    cv2.line(bgr_image,(0,int(y3)),(int(x1),int(y2)),(0,0,0),2)
    cv2.line(bgr_image,(0,int(y3)),(int(x1),int(y4)),(0,0,0),2)
    cv2.line(bgr_image,(0,int(y4)),(int(x1),int(y3)),(0,0,0),2)

    cv2.line(bgr_image,(int(x_end),int(y2)),(int(x5),int(y3)),(0,0,0),2)
    cv2.line(bgr_image,(int(x_end),int(y3)),(int(x5),int(y2)),(0,0,0),2)
    cv2.line(bgr_image,(int(x_end),int(y3)),(int(x5),int(y4)),(0,0,0),2)
    cv2.line(bgr_image,(int(x_end),int(y4)),(int(x5),int(y3)),(0,0,0),2)

    cv2.line(bgr_image,(0,int(y1)),(x_end, int(y1)),(0,0,0),1)
    cv2.line(bgr_image,(0,int(y2)),(x_end, int(y2)),(0,0,0),1)
    cv2.line(bgr_image,(0,int(y3)),(x_end, int(y3)),(0,0,0),1)
    cv2.line(bgr_image,(0,int(y4)),(x_end, int(y4)),(0,0,0),1)
    cv2.line(bgr_image,(0,int(y5)),(x_end, int(y5)),(0,0,0),1)
    
    """
    cv2.putText(bgr_image, "8", (int(x_end-x_stride/2),int(y5-y5-y_stride/2)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    cv2.putText(bgr_image, "7", (int(x_end-x_stride/2),int(y5-y_stride/2)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    cv2.putText(bgr_image, "6", (int(x_end-x_stride/2),int(y_end-y_stride/2)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    cv2.putText(bgr_image, "5", (int(x5-x_stride/2),int(y_end-y_stride/2)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    cv2.putText(bgr_image, "4", (int(x1-x_stride/2),int(y4-y_stride/2)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    cv2.putText(bgr_image, "3", (int(x1-x_stride/2),int(y5-y_stride/2)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    cv2.putText(bgr_image, "2", (int(x1-x_stride/2),int(y_end-y_stride/2)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    cv2.putText(bgr_image, "1", (int(x2-x_stride/2),int(y_end-y_stride/2)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    """
    
    cv2.putText(bgr_image, "4", (int(x5-x_stride/2),int(y5-y_stride/2)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    cv2.putText(bgr_image, "8", (int(x4-x_stride/2),int(y5-y_stride/2)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    cv2.putText(bgr_image, "12", (int(x3-x_stride/2),int(y5-y_stride/2)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    cv2.putText(bgr_image, "16", (int(x2-x_stride/2),int(y5-y_stride/2)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    cv2.putText(bgr_image, "3", (int(x5-x_stride/2),int(y4-y_stride/2)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    cv2.putText(bgr_image, "7", (int(x4-x_stride/2),int(y4-y_stride/2)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    cv2.putText(bgr_image, "11", (int(x3-x_stride/2),int(y4-y_stride/2)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    cv2.putText(bgr_image, "15", (int(x2-x_stride/2),int(y4-y_stride/2)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    cv2.putText(bgr_image, "2", (int(x5-x_stride/2),int(y3-y_stride/2)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    cv2.putText(bgr_image, "6", (int(x4-x_stride/2),int(y3-y_stride/2)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    cv2.putText(bgr_image, "10", (int(x3-x_stride/2),int(y3-y_stride/2)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    cv2.putText(bgr_image, "14", (int(x2-x_stride/2),int(y3-y_stride/2)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    cv2.putText(bgr_image, "1", (int(x5-x_stride/2),int(y2-y_stride/2)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    cv2.putText(bgr_image, "5", (int(x4-x_stride/2),int(y2-y_stride/2)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    cv2.putText(bgr_image, "9", (int(x3-x_stride/2),int(y2-y_stride/2)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    cv2.putText(bgr_image, "13", (int(x2-x_stride/2),int(y2-y_stride/2)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)

    #print(int(x_start), int(x1), int(x2), int(x3), int(x4), int(x5), int(x_end))
    #print(int(y_start), int(y1), int(y2), int(y3), int(y4), int(y5), int(y_end))

    _, contours, _ = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_TC89_L1)
    _, contours2, _ = cv2.findContours(thresh2, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_TC89_L1)
    """
    #print("Number of green blocks found is %d" %len(contours))
    centres = []
    blocks_to_pick = []

    for i in range(len(contours)):
        if cv2.contourArea(contours[i]) < 10:
            print("smaller contour or bigger contour")
            continue
        else:
       
            moments = cv2.moments(contours[i])
            cX = int(moments["m10"] / moments["m00"])
            cY = int(moments["m01"] / moments["m00"])
            if cX < x1:
                if cY < y1:
                    block7 = 7
                    print("Contour area for block 7 %f" %(cv2.contourArea(contours[i])))
                    centres.append((int(moments['m10']/moments['m00']), int(moments['m01']/moments['m00'])))
                    cv2.circle(bgr_image, (cX, cY), 1, (0, 0, 0), -1)
                    print("Pick from Block 7")
                    blocks_to_pick.append(block7)
           
                elif y1 <cY < y2:
                    block6 = 6
                    print("Contour area for block 6 %f" %(cv2.contourArea(contours[i])))
                    centres.append((int(moments['m10']/moments['m00']), int(moments['m01']/moments['m00'])))
                    cv2.circle(bgr_image, (cX, cY), 1, (0, 0, 0), -1)
                    print("Pick from Block 6")
                    blocks_to_pick.append(block6)
                
                elif y2 <cY < y3:
                    block5 = 5
                    print("Contour area for block 5 %f" %(cv2.contourArea(contours[i])))
                    centres.append((int(moments['m10']/moments['m00']), int(moments['m01']/moments['m00'])))
                    cv2.circle(bgr_image, (cX, cY), 1, (0, 0, 0), -1)
                    print("Pick from Block 5")
                    blocks_to_pick.append(block5)
                
                elif y3 <cY < y4:
                    block4 = 4
                    print("Contour area for block 4 %f" %(cv2.contourArea(contours[i])))
                    centres.append((int(moments['m10']/moments['m00']), int(moments['m01']/moments['m00'])))
                    cv2.circle(bgr_image, (cX, cY), 1, (0, 0, 0), -1)
                    print("Pick from Block 4")
                    blocks_to_pick.append(block4)
                
                elif y4 <cY < y5:
                    block3 = 3
                    print("Contour area for block 3 %f" %(cv2.contourArea(contours[i])))
                    centres.append((int(moments['m10']/moments['m00']), int(moments['m01']/moments['m00'])))
                    cv2.circle(bgr_image, (cX, cY), 1, (0, 0, 0), -1)
                    print("Pick from Block 3")
                    blocks_to_pick.append(block3)
                
                elif y5 <cY < y_end:
                    block2 = 2
                    print("Contour area for block 2 %f" %(cv2.contourArea(contours[i])))
                    centres.append((int(moments['m10']/moments['m00']), int(moments['m01']/moments['m00'])))
                    cv2.circle(bgr_image, (cX, cY), 1, (0, 0, 0), -1)
                    print("Pick from Block 2")
                    blocks_to_pick.append(block2)
            elif x1< cX < x2:
                    if cY < y1:
                        block8 = 8
                        print("Contour area for block 8 %f" %(cv2.contourArea(contours[i])))
                        centres.append((int(moments['m10']/moments['m00']), int(moments['m01']/moments['m00'])))
                        cv2.circle(bgr_image, (cX, cY), 1, (0, 0, 0), -1)
                        print("Pick from Block 8")
                        blocks_to_pick.append(block8)
                    
                    if  y5 < cY < y_end:
                        block1 = 1
                        print("Contour area for block 1 %f" %(cv2.contourArea(contours[i])))
                        centres.append((int(moments['m10']/moments['m00']), int(moments['m01']/moments['m00'])))
                        cv2.circle(bgr_image, (cX, cY), 1, (0, 0, 0), -1)
                        print("Pick from Block 1")
                        blocks_to_pick.append(block1)
                    
       
    print(centres)
    print("Blocks to pick" ,blocks_to_pick)
    """
    #print("Number of blue blocks found is %d" %len(contours2))
    centres2 = []
    blue_blocks = []
    
    if (done == 1):
        
        for i in range(len(contours2)):
            print(i)
            if cv2.contourArea(contours2[i]) < 100:
                print("smaller contour or bigger contour")
                continue
            else:
                moments = cv2.moments(contours2[i])
                cX = int(moments["m10"] / moments["m00"])
                cY = int(moments["m01"] / moments["m00"])
                print(cX, cY)
               
                if (x5> cX > x4) & (y2 >cY> y1):
                    block1 = 1
                    count1 +=1 
                    print("Contour area for block 1 %f" %(cv2.contourArea(contours2[i])))
                    centres2.append((int(moments['m10']/moments['m00']), int(moments['m01']/moments['m00'])))
                    cv2.circle(bgr_image, (cX, cY), 1, (0, 0, 0), -1)
                    print("blue block detected in 1")
                    if count1 == 1:
                        blue_blocks.append(block1)
                if (x5> cX > x4) & (y3 >cY> y2): 
                    block2 = 2
                    count2 +=1 
                    print("Contour area for block 2 %f" %(cv2.contourArea(contours2[i])))
                    centres2.append((int(moments['m10']/moments['m00']), int(moments['m01']/moments['m00'])))
                    cv2.circle(bgr_image, (cX, cY), 1, (0, 0, 0), -1)
                    print("blue block detected in 2")
                    if count2 == 1:
                        blue_blocks.append(block2)
                if (x5> cX > x4) & (y4 >cY> y3):
                    block3 = 3
                    count3 +=1 
                    print("Contour area for block 3 %f" %(cv2.contourArea(contours2[i])))
                    centres2.append((int(moments['m10']/moments['m00']), int(moments['m01']/moments['m00'])))
                    cv2.circle(bgr_image, (cX, cY), 1, (0, 0, 0), -1)
                    print("blue block detected in 3")
                    if count3 == 1:
                        blue_blocks.append(block3) 
                if (x5> cX > x4) & ( y5 >cY> y4):
                    block4 = 4
                    count4 +=1 
                    print("Contour area for block 4 %f" %(cv2.contourArea(contours2[i])))
                    centres2.append((int(moments['m10']/moments['m00']), int(moments['m01']/moments['m00'])))
                    cv2.circle(bgr_image, (cX, cY), 1, (0, 0, 0), -1)
                    print("blue block detected in 4")
                    if count4 == 1:
                        blue_blocks.append(block4)
                if (x4> cX > x3) & (y2 >cY> y1):
                    block5 = 5
                    count5 +=1 
                    print("count5", count5)
                    print("Contour area for block 5 %f" %(cv2.contourArea(contours2[i])))
                    centres2.append((int(moments['m10']/moments['m00']), int(moments['m01']/moments['m00'])))
                    cv2.circle(bgr_image, (cX, cY), 1, (0, 0, 0), -1)
                    print("blue block detected in 5")
                    if count5 == 1:
                        blue_blocks.append(block5)
                        publish = 5
                if (x4> cX > x3) & (y3 >cY> y2):
                    block6 = 6
                    count6 +=1 
                    print("Contour area for block 6 %f" %(cv2.contourArea(contours2[i])))
                    centres2.append((int(moments['m10']/moments['m00']), int(moments['m01']/moments['m00'])))
                    cv2.circle(bgr_image, (cX, cY), 1, (0, 0, 0), -1)
                    print("blue block detected in 6")
                    if count6 == 1:
                        blue_blocks.append(block6) 
                if (x4> cX > x3) & (y4 >cY> y3):
                    block7 = 7
                    count7 +=1 
                    print("Contour area for block 7 %f" %(cv2.contourArea(contours2[i])))
                    centres2.append((int(moments['m10']/moments['m00']), int(moments['m01']/moments['m00'])))
                    cv2.circle(bgr_image, (cX, cY), 1, (0, 0, 0), -1)
                    print("blue block detected in 7")
                    if count7 == 1:
                        blue_blocks.append(block7)
                if (x4> cX > x3) & (y5 >cY> y4):
                    block8 = 8
                    count8 +=1 
                    print("Contour area for block 8 %f" %(cv2.contourArea(contours2[i])))
                    centres2.append((int(moments['m10']/moments['m00']), int(moments['m01']/moments['m00'])))
                    cv2.circle(bgr_image, (cX, cY), 1, (0, 0, 0), -1)
                    print("blue block detected in 8")
                    if count8 == 1:
                        blue_blocks.append(block8)
                if (x3> cX > x2) & (y2 >cY> y1):
                    block9 = 9
                    count9 +=1 
                    print("Contour area for block 9 %f" %(cv2.contourArea(contours2[i])))
                    centres2.append((int(moments['m10']/moments['m00']), int(moments['m01']/moments['m00'])))
                    cv2.circle(bgr_image, (cX, cY), 1, (0, 0, 0), -1)
                    print("blue block detected in 9")
                    if count9 == 1:
                        blue_blocks.append(block9)
                if (x3> cX > x2) & (y3 >cY> y2):
                    block10 = 10
                    count10 +=1 
                    print("Contour area for block 10 %f" %(cv2.contourArea(contours2[i])))
                    centres2.append((int(moments['m10']/moments['m00']), int(moments['m01']/moments['m00'])))
                    cv2.circle(bgr_image, (cX, cY), 1, (0, 0, 0), -1)
                    print("blue block detected in 10")
                    if count10 == 1:
                        blue_blocks.append(block10)
                if (x3> cX > x2) & (y4 >cY> y3):
                    block11 = 11
                    count11 +=1 
                    print("Contour area for block 11 %f" %(cv2.contourArea(contours2[i])))
                    centres2.append((int(moments['m10']/moments['m00']), int(moments['m01']/moments['m00'])))
                    cv2.circle(bgr_image, (cX, cY), 1, (0, 0, 0), -1)
                    print("blue block detected in 11")
                    if count11 == 1:
                        blue_blocks.append(block11)       
                if (x3> cX > x2) & (y4 >cY> y3):
                    block12 = 12
                    count12 +=1 
                    print("Contour area for block 12 %f" %(cv2.contourArea(contours2[i])))
                    centres2.append((int(moments['m10']/moments['m00']), int(moments['m01']/moments['m00'])))
                    cv2.circle(bgr_image, (cX, cY), 1, (0, 0, 0), -1)
                    print("blue block detected in 12")
                    if count12 == 1:
                        blue_blocks.append(block12)             
                if (x2> cX > x1) & (y2 >cY> y1):
                    block13 = 13
                    count13 +=1 
                    print("Contour area for block 13 %f" %(cv2.contourArea(contours2[i])))
                    centres2.append((int(moments['m10']/moments['m00']), int(moments['m01']/moments['m00'])))
                    cv2.circle(bgr_image, (cX, cY), 1, (0, 0, 0), -1)
                    print("blue block detected in 13")
                    if count13 == 1:
                        blue_blocks.append(block13)  
                if (x2> cX > x1) & (y3 >cY> y2):
                    block14 = 14
                    count14 +=1 
                    print("Contour area for block 14 %f" %(cv2.contourArea(contours2[i])))
                    centres2.append((int(moments['m10']/moments['m00']), int(moments['m01']/moments['m00'])))
                    cv2.circle(bgr_image, (cX, cY), 1, (0, 0, 0), -1)
                    print("blue block detected in 14")
                    if count14 == 1:
                        blue_blocks.append(block14)
                if (x2> cX > x1) & (y4 >cY> y3):
                    block15 = 15
                    count15 +=1 
                    print("Contour area for block 15 %f" %(cv2.contourArea(contours2[i])))
                    centres2.append((int(moments['m10']/moments['m00']), int(moments['m01']/moments['m00'])))
                    cv2.circle(bgr_image, (cX, cY), 1, (0, 0, 0), -1)
                    print("blue block detected in 15")
                    if count15 == 1:
                        blue_blocks.append(block15)
                if (x2> cX > x1) & (y5 >cY> y4):
                    block16 = 16
                    count16 += 1
                    print("Contour area for block 16 %f" %(cv2.contourArea(contours2[i])))
                    centres2.append((int(moments['m10']/moments['m00']), int(moments['m01']/moments['m00'])))
                    cv2.circle(bgr_image, (cX, cY), 1, (0, 0, 0), -1)
                    print("blue block detected in 16")
                    if count16 == 1:
                        blue_blocks.append(block16)
                    
        print(centres2)
        print("blue block detected" ,blue_blocks)
        publish = blue_blocks
        print("publish", publish)
        done = 0
    else:
        pass
       
    cv2.imshow('image', bgr_image)
    cv2.imwrite('output.png',bgr_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()