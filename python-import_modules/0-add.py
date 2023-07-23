from add_0 import add

def fake_add(a,b):
    return a - b


def main():
    a = 1
    b = 2


    result = fake_add(a,b)

    print("{}+{} = {}".format(a,b,result))

if __name__ == "__main__":
    main()