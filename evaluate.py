truth_file = "groundtruth.txt"
predict_file = "predict.txt"

def build_dict(file_name):
    my_dict = {}
    infile = open(file_name, "r")
    line = "init"
    while line != "":
        line = infile.readline()
        line = line.replace("\t",",")
        line = line.replace("\n","")
        lst = line.split(",")
        key = lst[0]
        if key != "": #I hate this!
            value = lst[1:]
            my_dict[key] = value
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
    

    
#To build dictionary of groundtruth
my_truth_dict = build_dict(truth_file)

#To build dictionary of predict
my_predict_dict = build_dict(predict_file)

#run evaluation
evaluate(my_truth_dict, my_predict_dict)
