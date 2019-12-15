import sys
import os

def main():
    filePath = sys.argv[1]

    if not os.path.isfile(filePath):
        print("File path {} does not exist. Exiting...".format(filePath))
        sys.exit()

    words = []
    with open(filePath) as fp:
        for line in fp:
            words.append(line.strip())
    words.sort()
    for word in words:
        print(word)

if __name__ == '__main__':
    main()
