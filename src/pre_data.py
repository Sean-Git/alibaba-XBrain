import re

def pre_data(in_name, out_name, pattern):
    in_file = open(in_name,"r")
    out_file = open(out_name,"w")
    line = "init"
    count = 0
    #title
    out_file.write(in_file.readline())
    #write data
    while line != "":
        line = in_file.readline()
        if re.match(pattern, line):
            count += 1
            out_file.write(line)
            print "Match NO.%d" % count
        else:
            pass
    in_file.close()
    out_file.close()
    print "\nTotally %d lines in %s" % (count, out_name)


#source data
in_name = "../data/t_alibaba_data.csv"

#for train
pattern = r'.*,.*,.*,[4-7]'
out_name = "../data/train.csv"
pre_data(in_name, out_name, pattern)

#for test
pattern = r'.*,.*,.*,8'
out_name = "../data/test.csv"
pre_data(in_name, out_name, pattern)
