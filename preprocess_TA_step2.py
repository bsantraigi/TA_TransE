import numpy as np
import sys
import os

# tem_dict
tem_dict = {
    '0y': 0, '1y': 1, '2y': 2, '3y': 3, '4y': 4, '5y': 5, '6y': 6, '7y': 7, '8y': 8, '9y': 9,
    '0m': 10, '1m': 11, '2m': 12, '3m': 13, '4m': 14, '5m': 15, '6m': 16, '7m': 17, '8m': 18, '9m': 19,
    '0d': 20, '1d': 21, '2d': 22, '3d': 23, '4d': 24, '5d': 25, '6d': 26, '7d': 27, '8d': 28, '9d': 29
}

count = 0
dataset = sys.argv[1]
# print(dataset)
path = '../data/' + dataset
# print(path)
# exit()
os.makedirs(dataset + '_TA', exist_ok=True)
write_path = '../data/' + dataset + '_TA'
# print(write_path)

def preprocess(data_part):
    data_path = path + data_part + '.txt'
    tem_write_path = write_path + data_part + '_tem.npy'
    tem = []
    with open(data_path) as fp:
        for i,line in enumerate(fp):
            # print(line)
            # exit()
            global count
            count += 1
            info = line.strip().split("\t")
            # print(info)
            # exit()

            year, month, day = info[3].split("-")
            # print(year,month,day)
            # exit()
            tem_id_list = []
            for j in range(len(year)):
                token = year[j:j+1]+'y'
                tem_id_list.append(tem_dict[token])
            # print(tem_id_list)
            # exit()

            for j in range(1):
                # print(month[1])
                # exit()
                token1 = month[0]+'m'
                tem_id_list.append(tem_dict[token1])
                token2 = month[0]+'m'
                tem_id_list.append(tem_dict[token2])


            for j in range(len(day)):
                token = day[j:j+1]+'d'
                tem_id_list.append(tem_dict[token])
            

            tem.append(tem_id_list)
    np_tem = np.array(tem)
    np.save(tem_write_path, np_tem)


preprocess('train')
preprocess('valid')
preprocess('test')
