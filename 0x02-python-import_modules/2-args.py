#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv) - 1

    if i == 0:
        print(f"{i} arguments.")
    elif i == 1:
        print(f"{i} argument:")
    else:
        print(f"{i} arguments:")

    if i >= 1:
        i = 0
        for arg in sys.argv:
            if i != 0:
                print("{}: {}".format(i, arg))
            i += 1
