from gorev1 import *
from gorev2 import *

def main():
    count = 0
    ret = gorev1()
    for boolRet in ret:
        if boolRet == True:
            print "cember Tanimlandi ve gorev1 Basarili."
            count = 1
    if (count == 1):
        gorev2()
    return True
    
if __name__ == "__main__":
    main()