#!/usr/bin/python3

def shell():
    import traceback,readline,termcolor
    #from termcolor import colored
    print(">>> # moonshell")
    print(">>> # by bufferbandit")
    while 1:
        try:
            i = input(termcolor.colored(">>> ","cyan"))
            if i == "quit" or i == "exit":
                print(i)
                return 0
            elif i in dir():
                exec("print({})".format(i))
            elif i == "dir()":
                exec("print(dir())")
            else:
                if i.endswith(":"):
                    while 1:
                        i2 = input("...   ")
                        if i2:
                            i += "\n    {}".format(i2)
                            continue
                        else:
                            print("")
                            break

            exec(i)
        except  Exception as exception:
            print("\n")
            traceback.print_exc()
            continue
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt")
            continue

if __name__ == "__main__":
    shell()
    
