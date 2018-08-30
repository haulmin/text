################################################### 
###            2018 -2  OOP   Pre-TEST             ### 
################################################### 
import math


def  triple_sum(data, goal):
    ########################### 
    #      IMPLEMENT HERE     #  
    length = len(data)
    for i in range(length-2):
        for j in range(i+1, length-1):
            for k in range(j+1, length):
                sum = data[i] + data[j] + data[k]
                if sum == goal:
                    return True
    
    return False
    ###########################

#print (triple_sum( [5,12,3,8,12,11,2,6] , 16 ))   # True
#print (triple_sum( [5,12,3,8,12,11,2,6] , 26 ))  # True
#print (triple_sum( [5,12,3,8,12,11,2,6] , 9  ))  # False  
 
##############################################

def  threshold(dailyGains, goal):
    ########################### 
    sum = 0
    for i in range(len(dailyGains)):
        sum += dailyGains[i]
        if sum >= goal:
            return i+1
    return 0
    ###########################

#print (threshold( [5,3,8,2,9,1], 17  ))  # 4  
#print (threshold( [5,3,8,2,9,1], 100 ))  # 0 
 
##############################################
def bmi (h,w): #digits
    ########################### 
    #      IMPLEMENT HERE     #  
    return w / (h / 100.0)**2
    ###########################

#print (bmi(165, 48))  # 17.6308539945
#print (bmi(183, 97))  # 28.964734689 
 
 
###################################################


def check_in_range( data , a, b ) :
    ########################### 
    #      IMPLEMENT HERE     #  
    def isInRange(num, min, max) : #closed interval [min, max]
        if num <= max and num >= min:
            return True
        return False

    for i in data:
        if not isInRange(bmi(i[0], i[1]), a, b):
            return False
    return True

    ###########################

#print (check_in_range ( [[165, 48],[176,69],[186,80],[161,64],[183,97]], 15, 22)) # False 
#print (check_in_range ( [[163, 70],[199,67],[156,59],[186,70],[191,73]], 10, 29 )) # True
###################################################


def height_cone(r, side):
    ########################### 
    #      IMPLEMENT HERE     #  
    pass
    ###########################

# print(height_cone(5, 16))    # 15.1986841536
 
 
###################################################


def volume_cone( r, side ) :
    ########################### 
    #      IMPLEMENT HERE     #  
    pass
    ###########################
    
#print( volume_cone(5, 16))   # 397.900620676


###################################################


def largest_volume_cone ( data ):
    ########################### 
    #      IMPLEMENT HERE     #  
    pass
    ###########################

#print largest_volume_cone([[5,16], [12,19], [4,19], [12,14], [6,8]])  # 2221.37038181 
###################################################

def distance( data ):
    ########################### 
    #      IMPLEMENT HERE     #  
    pass
    ###########################

#print (distance ([ [4,7], [18,27] ]))     # 24.4131112315    
#print (distance ([ [0,7], [7,0] ]))       # 9.89949493661
 
  
###################################################


def center_position(data):
    ########################### 
    #      IMPLEMENT HERE     #  
    pass
    ###########################
    
#print (center_position([ [1,2], [9,2], [4,8], [7,4], [1,-2], [-1, 4] ])) 	#[3.5, 3.0]

###################################################


def find_outlier( data ) :
    ########################### 
    #      IMPLEMENT HERE     #  
    pass
    ###########################

#print find_outlier (([ [1,2], [9,2], [4,8], [7,4], [1,-2], [-1, 4] ]))     # [9, 2]

###################################################
def estimate_pi (err_tolerance) :
    ########################### 
    #      IMPLEMENT HERE     #  
    pass
    ###########################

#print (estimate_pi(-1))  #3.04183961893 
###################################################

def draw_histogram ( data ):
    ########################### 
    #      IMPLEMENT HERE     #
    newList = data
    maxData = max(data); minData= min(data)
    if maxData >= 0:
        for i in range(maxData+1, -1, -1):
            if i == 1:
                print("="* len(data) * 3)
            elif i == 0:
                for val in data:
                    print(" " + str(val) + " ", end = " ")
                    
            else:
                for val in data:
                    if val > 0:
                        if val >= i-1:
                            print(" * ", end = " ")
                        else:
                            print("   ", end = " ")
                print()

    print()
    if minData < 0:
        for i in range(-1, minData-1, -1):
            for val in data:
                if val < 0:
                    if -val + i >= 0: 
                        print(" * ", end = " ")
                    else:
                        print("   ", end = " ")
                else:
                    print("   ")
        print()
    pass
    ###########################

draw_histogram( [3,4,0,-2] ) 
#draw_histogram([-3,-4, 0,-2])
###################################################

def sumOfTwoDistinctPrimeSquares(n):
    ########################### 
    #      IMPLEMENT HERE     #  
    pass
    ###########################
         

#print (sumOfTwoDistinctPrimeSquares(18)) # False
#print (sumOfTwoDistinctPrimeSquares(26))  # False
#print (sumOfTwoDistinctPrimeSquares(29))  # True  (29 == 2*2 + 5*5)
#print (sumOfTwoDistinctPrimeSquares(34))  # True  (34 == 3*3 + 5*5)
##############################################
 