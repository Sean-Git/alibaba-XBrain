from numpy import array,tile

#This function accumulate the K nearest neighbor's descriptor to a single one
#Return the top N recommendation.
def my_vote(data, N):
    sum_vec = array(data).sum(axis = 0)#accumulate
    sum_vec = list(sum_vec.argsort()/4)
    recommend = sum_vec[-N:]
    return recommend    


#This function gives the top K nearest vectors in matrix
def my_knn(vec, data, K):
    if len(vec) != len(data[0]):
        raise Exception("vectors' length do not match!")
    data = array(data) #change data format
    result = [] #the result matrix , each row represent a vector among the top k nearest.
    row = data.shape[0]
    col = data.shape[1]
    #compute Manhattan distances
    diffMat = tile(vec, (row,1)) - data
    sqDiffMat = diffMat**2
    distances = (sqDiffMat.sum(axis = 1))**0.5
    sortedDistIndices = distances.argsort()
    for i in range(1,K+1): #remember the first is the vec itself here
        result.append(list(data[sortedDistIndices[i]]))
    return result



    
    
    
