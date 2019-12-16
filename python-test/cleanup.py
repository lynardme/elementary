import os
import sys
import time


def remove(path):
    if os.path.isdir(path):
        try:
            os.rmdir(path)
        except OSError:
            print("Unable to remove folder {}".format(path))
    else:
        try:
            if os.path.exists(path):
                os.remove(path)
                print("removed file {}".format(path))
        except OSError:
            print("Unable to remove file: {}".format(path))

def main(past_days, path):
    time_in_secs = time.time() - (past_days * 24 * 60 * 60)
    for root, dirs, files in os.walk(path, topdown=False):
        # print("root {}".format(root))
        # print(dirs)
        # print(files)
        for file in files:
            full_path = os.path.join(root, file)
            stat = os.stat(full_path)
            print(full_path)
            print("time {}".format(stat.st_mtime))
            print("time {}".format(time_in_secs))

            if stat.st_mtime <= time_in_secs:
                # print("removed")
                remove(full_path)
    # print(time_in_secs)
    # print(path)

if __name__ == "__main__":
    days, path = int(sys.argv[1]), sys.argv[2]
    main(days, path)
