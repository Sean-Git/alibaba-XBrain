def build_truth(in_name, out_name):
    infile = open(in_name, "r")
    truth_dict = {} #build a groundtruth_dict first, them write it into outfile
    line = "init"
    line = infile.readline() #pass the title line

    while line != "":
        line = infile.readline()
        line = line.replace("\n","")
        lst = line.split(",")
        user = lst[0] #user_id would be the key
        if user == "": # I hate this! Help!
            continue
        brand = lst[1] #brand_id would be the value
        behavior = lst[2] #if behavior equals to 1, then it means the user buys the brand
        #temporarily neglect the time item
        if behavior == "1":
            if truth_dict.has_key(user) and truth_dict[user].count(brand) == 0:
                truth_dict[user].append(brand)
            elif not truth_dict.has_key(user):
                truth_dict[user] = [brand]

    outfile = open(out_name, "w")
    count = 0
    for key in truth_dict:
        outfile.write(key + "\t" + ",".join(truth_dict[key]) + "\n")
        count += 1
        print "Groundtruth record add NO.%d" % count
    infile.close()
    outfile.close()


###                     ###
#       Run and Set       #
###                     ###
in_name = "../data/test.csv"                #!
out_name = "../result/groundtruth.txt"      #!
#run build_truth
build_truth(in_name,out_name)

    
