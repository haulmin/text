def draw_histogram ( data ):
    ########################### 
    #      IMPLEMENT HERE     #
    maxData = max(data); minData= min(data)
    if maxData >= 0: #positive part
      for index in range(maxData+1, -1, -1):
        if index == 1:
          print("=" * len(data) * 3)

        elif index == 0:
          for val in data:
            if val < 0:
              print(str(val) + " ", end = " ")
            else:
              print(" " + str(val) + " ", end = " ")
          print()

        else:
          for val in data:
            if val > 0 and 1 + val - index >= 0:
              print(" * ", end = " ")
            else:
              print("   ", end = " ")
          print()

      if minData < 0: #negative part
        for index in range(-1, minData-1, -1):
          for val in data:
            if val < 0 and -index + val <= 0:
              print(" * ", end = " ")
            else:
              print("   ", end = " ")
          print()
    pass
    ###########################

#draw_histogram( [3,4,0,-2] ) 
#draw_histogram([-3,-4, 0,-2])
#draw_histogram([1,2,3,4,5,0,-2,-4])