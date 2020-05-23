#from upm import pyupm_urm37 as sensorObj
from konumAyarla import *

#sensor = sensorObj.URM37(0, 2)

def gorev2():
    try:
        #distance = sensor.getDistance() #sensörden okunacak konum
        konumAyarla(10, -10, 2) #örnek konum   
        return True
    except Exception as e:
        print(e)
        return False