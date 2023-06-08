import cv2
img=cv2.imread("solar_system.jpg")
cv2.imshow("output",img)
text="Sun" 
cv2.putText(img,
            text,
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
text1="Mercury" 
cv2.putText(img,
            text1,
            (30,600),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
text2="Venus" 
cv2.putText(img,
            text2,
            (40,800),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
text3="Earth" 
cv2.putText(img,
            text3,
            (10,400),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
text4="Mars" 
cv2.putText(img,
            text4,
            (50,900),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
text5="Jupiter" 
cv2.putText(img,
            text5,
            (60,1000),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
text6="Saturn" 
cv2.putText(img,
            text6,
            (70,1100),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
text7="Uranus" 
cv2.putText(img,
            text1,
            (80,1200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
text8="Neptune" 
cv2.putText(img,
            text1,
            (90,1300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.imshow("output",img)
cv2.waitKey(0)
