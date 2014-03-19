###                     ###
#       Run and Set       #
###                     ###
out_name = "../result/predict.txt"      #!
#set K for kNN
K = 5                                   #!
#set N for top-N recommend
N = 5                                   #!

from kNN import *

#get the user_index / brand_index / behavior_mat and build predict_mat
#1. get index from existed file
print "Getting index lists..."
user_file = open("../result/user_id.txt", "r")
brand_file = open("../result/brand_id.txt", "r")
user_index = []
brand_index = []
row = 0
col = 0
row = int(user_file.readline())  #number of matrix rows equals to user num.
col = int(brand_file.readline()) #number of matrix cols equals to brand num.
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
print "1. user_index and brand_index lists have been achieved!"

#2. get behavior_mat from existed file
print "Getting behavior matirx..."
behavior_file = open("../result/behavior_matrix.txt", "r")
behavior_mat = [[0 for j in range(col * 4)] for i in range(row)]
line3 = "init"
line3 = behavior_file.readline() #pass the first line, the row and col num have been stored
i = 0 #index of row
while line3 != "":
    line3 = behavior_file.readline()
    line3 = line3.replace("\n","")
    lst = line3.split(",")
    if lst == [""]:# bad code, to skip the last line
        continue
    for j in range(col * 4):
        if lst[j] == '0':
            behavior_mat[i][j] = 0
        else:
            behavior_mat[i][j] = float(lst[j])
    i += 1
behavior_file.close()
print "2. behavior matirx has been achieved!"


#make prediction in the below
#3. scan behavior_mat, make prediction using kNN MFP and recommend top N.
print "This takes a little longer time. Please wait..."
predict_dict = {} #build a predict_dict first, them write it into outfile
for i in range(row):
    ori_vec = behavior_mat[i]
    knn_vecs = my_knn(ori_vec, behavior_mat, K)
    recommend = my_vote(knn_vecs, N)
    for j in range(N):
        user = user_index[i]
        brand = brand_index[recommend[j]]
        if predict_dict.has_key(user) and predict_dict[user].count(brand) == 0:
            predict_dict[user].append(brand)
        elif not predict_dict.has_key(user):
            predict_dict[user] = [brand]              
print "3. scan to make prediction. Done!"

#4. write predict_mat into the outfile
print "predict_dict is being written to file..."
outfile = open(out_name, "w")
for key in predict_dict:
    outfile.write(key + "\t" + ",".join(predict_dict[key]) + "\n")
outfile.close()
print "4. predict.txt written. All Done!!!"
