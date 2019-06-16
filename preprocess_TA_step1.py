# make timestamps to datetime format
import datetime
import os
import sys
# reload(sys)
# sys.setdefaultencoding("ISO-8859-1")

dataset = sys.argv[1]
path = '../data/' + dataset
# print(path)
os.makedirs(dataset + '_TA', exist_ok=True)
newpath = '../data/' + dataset + '_TA/'
filelist = os.listdir(path)
# print(filelist)
for filename in filelist:   
    if filename.startswith('stat'):
        continue

    # print(filename)
    fp = open(os.path.join(path, filename))
    # print(fp)
    fw = open(os.path.join(newpath, filename), "w")

    start_time_str = "2018-01-01"
    format = "%Y-%m-%d"
    start_time = datetime.datetime.strptime(start_time_str, format)

    time_id = 3
    print(fp)
    for i, line in enumerate(fp):
        print(line)
        info = line.strip().split("\t")
        # print(len(info))
        print("info [time_id]")
        print(info[time_id])

        time = start_time + datetime.timedelta(hours=int(info[time_id]))
        time_str = time.strftime(format)

        fw.write("%-5d\t%-5d\t%-3d\t%-s\t0\n" % (int(info[0]), int(info[1]), int(info[2]), time_str))

    fp.close()
    fw.close()
