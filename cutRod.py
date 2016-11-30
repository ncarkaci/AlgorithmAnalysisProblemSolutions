#!/usr/bin/env python
#
# cut-road dynamic programming solution
#
# Author: Necmettin Çarkacı
# E-mail: necmettin [ . ] carkaci [ @ ] gmail [ . ] com
#
#Usage : 



def cutRod(beginPoint,endPoint):
    print "Length in firs time :"+list
    
    table = []
    table.insert(0,0); # non-cutting situation cost zero
    
    for currentLength in range(beginPoint,endPoint):
        
        minCost = 0
        for k in range(beginPoint,endPoint):
            newMinCost = cutRod(beginPoint, k)+cutRod(k, endPoint)
            
            if newMinCost < minCost :
                minCost = newMinCost
        
        minCost = (endPoint - beginPoint)+minCost
        


length = 5;

cutRod(length)

