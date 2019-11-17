import time
import multiprocessing
# from multiprocessing import Process
import sys
import argparse


def file_create(fileName):
    size = int(namespace.size)
    start_time = time.time()
    with open(fileName, "w") as out:
        out.seek(size - 1)
        out.write(namespace.pattern)
    print(fileName)
    return time.time() - start_time


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-files', type=int, help='amount files for creating')
    parser.add_argument('-size', type=int, help='file size')
    parser.add_argument('-path', type=str, help='path for creating file')
    parser.add_argument('-P', '--pattern', type=str, help='pattern for writing')
    parser.add_argument('-parallel', type=int, help='amount parallel threads')

    return parser


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    count_files = namespace.files
    path = namespace.path
    count_pools = namespace.parallel
    files = []
    for i in range(int(count_files)):
        files.append(str(path) + "/file" + str(i))
    start_total_time = time.time()
    with multiprocessing.Pool(processes=int(count_pools)) as pool:
        all_time = pool.map(file_create, files)
    total_time = time.time() - start_total_time
    min_time = all_time[0]
    max_time = all_time[0]
    sum = 0
    for one_time in list(all_time):
        sum += one_time
        if min_time > one_time:
            min_time = one_time
        if max_time < one_time:
            max_time = one_time
    print("Creating ", count_files, " files in ", path, " in ", count_pools, " threads\n",
          "Min: ", min_time, " Max: ", max_time, "Avg: ", sum / count_files," Total: ", total_time)