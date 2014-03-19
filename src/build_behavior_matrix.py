from math import exp
from numpy import array

#build the behavior matrix and write into the outfile
def build_behavior_matrix(in_name, out_name):
    #1. get index from existed file
    print "building index lists..."
    user_file = open("../result/user_id.txt", "r")      #!
    brand_file = open("../result/brand_id.txt", "r")    #!

    user_index = []
    brand_index = []
    row = 0
    col = 0

    row = int(user_file.readline())   #number of matrix rows equals to user num.
    col = int(brand_file.readline())  #number of matrix cols equals to brand num. 

    line1 = "init"
    while line1 != "":#note that here the last line is "" and added, but do not affects.
        line1 = user_file.readline()
        line1 = line1.replace("\n","")
        user_index.append(line1) #no need to check repeats
    line2 = "init"
    while line2 != "":
        line2 = brand_file.readline()
        line2 = line2.replace("\n","")
        brand_index.append(line2) #no need to check repeats
    user_file.close()
    brand_file.close()
    print "user_index and brand_index lists have been built!"

    #2. build behavior matrix(expanded)
    #note that each brand holds 4 feats that represent the score of each behavior from 0-3
        #0 - click
        #1 - bought   
        #2 - collect
        #3 - buying
    print "building behavior matrix..."
    behavior = [[0 for j in range(col * 4)] for i in range(row)] #This is very important!
    infile = open(in_name, "r")
    line = "init"
    line = infile.readline() #pass the title line
    while line != "":
        line = infile.readline()
        line = line.replace("\n","")
        lst = line.split(",")
        user = lst[0]
        if user == "": # bad code
            continue
        brand = lst[1]
        act = int(lst[2])
        t_dist = float(transform_time(lst[3]))
        behavior[user_index.index(user)][brand_index.index(brand)*4+act] += exp(-t_dist/T0)
    infile.close()
    print "behavior matrix has been built. rows:%d  cols:%d" % (row,col*4)

    #3. write behavior matrix
    print "writing behavior matrix..."
    outfile = open(out_name, "w")
    outfile.write(str(row)+ " " + str(col * 4) + "\n") #write num of rows and cols in first line
    for i in range(row):
        for j in range(col * 4):
            if behavior[i][j] == 0:
                outfile.write(str(behavior[i][j]))
            else:
                outfile.write('%.6f' % (behavior[i][j]))
            if j != (col*4-1):
                outfile.write(",")
            else:
                outfile.write("\n")        
    outfile.close()
    print "behavior matrix write done!"  


#input the date time like this "5月16日"; output the 'day distance' from input-time to set end-time
def transform_time(time):
    month_lst = [31,28,31,30,31,30,31,31,30,31,30,31]
    time = time.replace('月',',')
    time = time.replace('日','')
    time = time.split(',')
    in_month = int(time[0])
    in_day = int(time[1])
    start_time = 0
    for i in range(in_month-1):
        start_time += month_lst[i]
    start_time += in_day
    return (end_time - start_time)


###                     ###
#       Run and Set       #
###                     ###
in_name = "../data/test.csv"                    #!
out_name = "../result/groundtruth.txt"          #!
in_name = "../data/train.csv"                   #!
#end-time(July 31th)
end_time = 212                                  #!
T0 = 50                                         #!
#store behavior matrix
out_name = "../result/behavior_matrix.txt"      #!
#run building behavior matrix
build_behavior_matrix(in_name, out_name)                 
    
