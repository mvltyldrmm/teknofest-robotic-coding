from konumAyarla import *
from cemberTanila import *

def gorev1():
    ret = [False]
    try:
        for i in range(3):
            konumAyarla(5, 7, 10) #konuma gidildikten sonra cember tanila kullanilip cember aranacak varsa icinde gecilecek.
            ret[i] = cemberTanila()
        return ret
    except Exception as e:
        print(e)
        return ret
        