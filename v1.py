def kamera():

    import numpy as np
    import cv2
    cap = cv2.VideoCapture(0)  
    while (True):

        # Çerçeveler halinde görüntü yakalar
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ##Gürültü Temizleme islemi
        
        noise_removal = cv2.bilateralFilter(gray, 9, 75, 75)
        # Daha iyi sonuç elde etmek için histogram eşitleme yapıldı
        equal_histogram = cv2.equalizeHist(noise_removal)

        # Dikdörtgen yapı elemanı ile morfolojik açılım
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        morph_image = cv2.morphologyEx(equal_histogram, cv2.MORPH_OPEN, kernel, iterations=15)

        # Görüntü çıkarma (Morph görüntüsünü histogram eşitlenmiş görüntüsünden çıkarmak)
        sub_morp_image = cv2.subtract(equal_histogram, morph_image)

        # Görüntüyü eşikleme
        ret, thresh_image = cv2.threshold(sub_morp_image, 0, 255, cv2.THRESH_OTSU)

        # Canny Edge algılama uygulanması
        canny_image = cv2.Canny(thresh_image, 250, 255)
        # Display Image
        canny_image = cv2.convertScaleAbs(canny_image)

        # Kenarları güçlendirmek için genleşme
        kernel = np.ones((3, 3), np.uint8)

        # Genişletme için çekirdek oluşturma
        dilated_image = cv2.dilate(canny_image, kernel, iterations=1)

        #Çember bulma işlemi

        circles = cv2.HoughCircles(dilated_image, cv2.HOUGH_GRADIENT, 1, 20000, param1=40, param2=60, minRadius=0, maxRadius=0)
        
        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0,:]:
                cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 3)  #Çember tanıma
                cv2.imwrite
                x = i[0]
                y = i[1]
                x = str(x)
                y = str(y)
                x_yer = " "
                if ((480/2) - i[0] < 0):
                    x_yer = "sol"
                elif (480 / 2) - i[0] > 0:
                    x_yer ="sag"
                if (630 / 2 - i[1] > 0):
                    y_yer ="ust"
                elif (630/2 -i[1]<0):
                    y_yer = "alt"

                string = "X:",x,"Y:",y," SOLSAG:",x_yer,"ALTUST:",y_yer,"Tarafda"
                
                string = str(string)
                print(string)
                
                cv2.putText(frame,string,(200,320), cv2.FONT_HERSHEY_COMPLEX, 0.30,(255,255,255),1,cv2.LINE_AA)
                
                
                
        cv2.imshow("Edge",dilated_image)
        cv2.imshow("Cember tespit", frame)
              
        if cv2.waitKey(1) & 0xFF == ord('q'):  # q ile çıkış yapabilirsiniz
            break

   

    cap.release()
    cv2.destroyAllWindows()
kamera()