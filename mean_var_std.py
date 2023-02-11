import numpy as np

def calculator():

    ip = [x for x in range(9)]

    ip = np.reshape(np.array(ip),(3,3))

    answer = dict()

    answer['mean'] = [list(np.mean(ip,axis=0)),list(np.mean(ip,axis = 1)),np.mean(ip)]

    answer['variance'] = [list(np.var(ip,axis=0)),list(np.var(ip,axis=1)),np.var(ip)]

    answer['standard deviation'] = [list(np.std(ip,axis=0)),list(np.std(ip,axis=1)),np.std(ip)]

    answer['max'] = [list(np.max(ip,axis=0)),list(np.max(ip,axis=1)),np.max(ip)]

    answer['min'] = [list(np.min(ip,axis=0)),list(np.min(ip,axis=1)),np.min(ip)]

    answer['sum'] = [list(np.sum(ip,axis=0)),list(np.sum(ip,axis=1)),np.sum(ip)]


    return(answer)