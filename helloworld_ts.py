
print("this is now working")

import subprocess
#produce reference artifact
subprocess.call(["touch", "testABC.txt"])


def double(x):
    y = x+x
    return y


if __name__ == '__main__':
    a = 2
    b = double(a)
    print(b)
