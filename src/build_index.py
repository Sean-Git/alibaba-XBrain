def build_index(in_name, out_name1, out_name2):
    infile = open(in_name, "r")
    user_id = [];
    brand_id = [];
    line = "init"
    line = infile.readline() #pass the title line
    print "waiting..."
    while line != "":
        line = infile.readline()
        line = line.replace("\n","")
        lst = line.split(",")
        user = lst[0]
        if user == "": # bad code
            continue
        brand = lst[1]

        if user_id.count(user) == 0:
            user_id.append(user)

        if brand_id.count(brand) == 0:
            brand_id.append(brand)
    infile.close()
    
    print "writing outfiles..."
    outfile1 = open(out_name1, "w")
    outfile2 = open(out_name2, "w")
    #the first line of each outfile writes the total num of index items
    outfile1.write(str(len(user_id)) + "\n")
    outfile2.write(str(len(brand_id)) + "\n")
    #iterate each index list and write into the corresponding outfile
    for item in user_id:
        outfile1.write(item + "\n")
    for item in brand_id:
        outfile2.write(item + "\n")
    outfile1.close()
    outfile2.close()
    print "Done!"


###                     ###
#       Run and Set       #
###                     ###
in_name = "../data/train.csv"               #!
#user_id index
out_name1 = "../result/user_id.txt"         #!
#brand_id index
out_name2 = "../result/brand_id.txt"        #!
#run build_index
build_index(in_name,out_name1,out_name2)
    
