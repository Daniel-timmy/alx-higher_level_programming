#!/usr/bin/python3

if __name__ == "__main__":

    import sys
    n = len(sys.argv)

    sumn = 0
    for i in range(1, n):
        sumn += int(sys.argv[i])
    print("{}".format(sumn))
