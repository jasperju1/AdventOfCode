with open('example2.txt', 'r') as f:
    lines = f.readlines()

    for x in lines:
        print(x.split())