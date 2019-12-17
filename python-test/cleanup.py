import os
import sys
import time
import logging

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

def remove(path):
    # check if path is a directory
    if os.path.isdir(path):
        try:
            os.rmdir(path)
        except OSError:
            print("Unable to remove folder {}".format(path))
    else:
        try:
            if os.path.exists(path):
                os.remove(path)
        except OSError:
            print("Unable to remove file: {}".format(path))

def main(path=CURRENT_DIR, past_days=14):
    logging.basicConfig(filename="cleanup.log",
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)
    logging.info("======== Start cleaning up script ========")
    logging.info("DESC: Delete all files not accessed in the past {} days and any directories that are left empty".format(past_days))
    time_in_secs = time.time() - (past_days * 24 * 60 * 60)
    for root, dirs, files in os.walk(path, topdown=False):
        for file in files:
            full_path = os.path.join(root, file)
            stat = os.stat(full_path)

            if stat.st_mtime <= time_in_secs:
                remove(full_path)
                logging.info("Removed file - {}".format(full_path))

        # root is empty
        if not os.listdir(root):
            remove(root)
            logging.info("Removed empty directory - {}".format(root))
    logging.info("======== End of cleanup script ========")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    elif len(sys.argv) == 3:
        val=None
        try:
            val = int(sys.argv[2])
        except ValueError:
            print("argument 2 is not a valid int")
        main(sys.argv[1], val)
    else:
        main()
    print("see cleanup.log...")
