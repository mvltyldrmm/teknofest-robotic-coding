from gorev1 import *
from gorev2 import *

def main():
    count = 0
    ret = gorev1()
    for boolRet in ret:
        if(boolRet == True):
            count = count + 1
    print("Tanilanan cember sayisi: ", count)
    if (count == 3):
        gorev2()
    return True
    
if __name__ == "__main__":
    main()