#Checks if two lines overlap
#Assumes that an overlap excludes cases where the overlap is only in one point



def overlap(linea, lineb):
    x1,x2 = linea
    x3,x4 = lineb
    if x3 < x2 and x4 > x1:
        return True
    else:
        return False



assert overlap((1,4),(3,5)) == True
assert overlap((1,2),(3,5)) == False
assert overlap((1,8),(9,11)) == False
assert overlap((1,5),(3,5)) == True
assert overlap((1,3),(3,5)) == False
