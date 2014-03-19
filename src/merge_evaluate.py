def build_dict(file_name, my_dict):
    infile = open(file_name, "r")
    line = "init"
    while line != "":
        line = infile.readline()
        line = line.replace("\t",",")
        line = line.replace("\n","")
        lst = line.split(",")
        key = lst[0]
        if key == "": #I hate this!
            continue;
        value = lst[1:]
        if not my_dict.has_key(key):
            my_dict[key] = value
        else:
            for x in value:
                if my_dict[key].count(x) == 0:
                    my_dict[key].append(x)
    return my_dict


def evaluate(truth_dict, predict_dict):
    precision = 0.0
    recall = 0.0
    f_score = 0.0
    N = 0 #predict total brand number
    M = 0 #truth total brand number
    hit = 0 #total hit brand number

    for key in truth_dict:
        M += len(truth_dict[key])

    for key in predict_dict:
        N += len(predict_dict[key])
        for i in predict_dict[key]:
            if truth_dict.has_key(key) and truth_dict[key].count(i) != 0:
                hit += 1

    precision = float(hit) / N
    recall = float(hit) / M
    f_score = (2 * precision * recall) / (precision + recall)
    print "You have made %d hits among %d predicts, precision: %.3f" % (hit, N, precision)
    print "You have made %d hits among %d truths, recall: %.3f" % (hit, M, recall)
    print "Your algorithm result in F-Score: %.3f" % f_score


###                     ###
#       Run and Set       #
###                     ###

truth_file = "../result/groundtruth.txt"                        #!
#To build dictionary of groundtruth
my_truth_dict = {}
my_truth_dict = build_dict(truth_file, my_truth_dict)
#Set the number of predict files for merge.
T = 2                                                           #! 
my_predict_dict = {}
for t in range(T):
    predict_file = "../result/predict" + str(t+1) + ".txt"      #!
    #To build dictionary of predict
    my_predict_dict = build_dict(predict_file , my_predict_dict)

#run evaluation
evaluate(my_truth_dict, my_predict_dict)

