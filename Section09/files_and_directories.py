import os


def list_directories(s):
    def dir_list(d):
        #! Nonlocal keyword is used to declare that the variable is not local to the function
        #! Global keyword does not work in this case because the variable is not global
        nonlocal tab_stop
        files = os.listdir(d)
        for f in files:
            current_dir = os.path.join(d, f)
            if os.path.isdir(current_dir):
                print(f"{'\t'*tab_stop}Directory {f}")
                tab_stop += 1
                dir_list(current_dir)
                tab_stop -= 1
            else:
                print(f"{'\t'*tab_stop}{f}")

    tab_stop = 0
    if os.path.exists(s):
        print(f"Directory listing of {s}")
        dir_list(s)
    else:
        print(f"The directory {s} does not exist")


def main():
    # listing = os.walk(".")
    # for root, dirs, files in listing:
    #     print(f"root: {root}")
    #     for d in dirs:
    #         print(f"dir: {d}")
    #     for f in files:
    #         print(f"file: {f}")
    #     print()

    list_directories(".")


if __name__ == "__main__":
    main()
