#from upm import pyupm_urm37 as sensorObj
from konumAyarla import *
from cemberTanila import *

#sensor = sensorObj.URM37(0, 2)

def gorev1():
    ret = [False, False, False]
    try:
        #distance = sensor.getDistance() #sensörden okunacak konumlar dizi yapılacak
        for i in range(3):
            #konumAyarla(distance[i][x], distance[i][y], distance[i][z]) #sırayla okunan konumlara gidilecek
            konumAyarla(5, 7, 10) #örnek konum
            ret[i] = cemberTanila()
        return ret
    except Exception as e:
        print(e)
        return ret
        