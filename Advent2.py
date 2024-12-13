with open('example2.txt', 'r') as f:
    lines = f.readlines()
    counter = 0
    for line in lines:
        num = line.split()
        print(num)

        is_safe = True
        direction = ""
        for i in range(len(num) - 1):
            a = int(num[i])
            b = int(num[i+1])
            if i == 0 and a > b:
                direction = "down"
            elif i == 0 and a < b:
                direction = "up"

            pairdirection = ""
            if a > b:
                pairdirection = "down"
            elif a < b:
                pairdirection = "up"
            
            if not (abs(a-b) in [1,2,3] and pairdirection == direction and direction != ""):
            
                is_safe = False

        print(is_safe)
        if is_safe:
            counter +=1
    print(counter)