#Returns 1 if version1 is higher than version2, -1 if is lower, and 0 if the versions are equal
#Versions with more decimal places are considered higher than versions with less decimal places,
#provided everything else is equal. eg: 1.12.3 is higher than 1.12
#Returns None if any of the versions are invalid

import itertools

def forceIntCheck(l):
    try:
        for a in l:
            v1,v2 = a
            v1,v2 = int(v1),int(v2)
    except TypeError:
        pass
        

def checkVersion(version1,version2):
    vsplited1 = version1.split(".")
    vsplited2 = version2.split(".")
    dictionary = list(itertools.izip_longest(vsplited1, vsplited2))
    try:
        forceIntCheck(dictionary)
        for instance in dictionary:
            v1,v2 = instance
            v1,v2 = int(v1),int(v2)
            if v2 is None:
                return 1
            if v1 is None:
                return -1
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0
    except ValueError:
        return None

 
assert checkVersion("1.12","1.25.4") == -1
assert checkVersion("1.12.32","1.25") == -1
assert checkVersion("1.19","1.25") == -1
assert checkVersion("1.25","1.25") == 0
assert checkVersion("4.12","1.25") == 1
assert checkVersion("0.12","1.25") == -1
assert checkVersion("0.25","0.25") == 0
assert checkVersion("1.40","1.25") == 1
assert checkVersion("1.a12","1.00") == None
assert checkVersion("0.25","0.25") == 0
assert checkVersion("1.40","1.255") == -1
assert checkVersion("1.12","1.00c") == None
assert checkVersion("0.25","0.25") == 0
assert checkVersion("1.40","1.25") == 1
assert checkVersion("0.25.4.3","0.25.4.3") == 0
assert checkVersion("1.40","1.25.3.4.5.6.7") == 1
assert checkVersion("1.a12","7.43.2.4.5.?") == None
