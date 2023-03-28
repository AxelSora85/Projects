def problem1():
    months={
    "1": "january",
    "2": "febuary",
    "3": "march",
    "4": "april",
    "5": "may",
    "6": "june",
    "7": "july",
    "8": "august",
    "9": "september",
    "10": "october",
    "11": "november",
    "12": "december"
}
    while True:
            try:
                value=int(input("enter a number for a month:  "))
                
                if (value >= 1 and value <= 12):
                    print ("that month is " + months[str (value)])
                
                    break
            except ValueError:
                print("please enter a valid input ")
problem1()


def problem2():
    file1=open("videoGamesSales.txt", "r")

    for line in file1.readlines():
        linetosplit=line.split(",")
        print(linetosplit[1]+ ' ' + linetosplit[10])
    file1.close()
problem2()


def problem3():
    globalsum=0
    file1=open("videoGamesSales.txt", "r")
    print("name and Global sales" + "\n")

    for line in file1.readlines():
        linetosplit=line.split(",")
        print("current sum of global sales "+ str(globalsum)+ "\n")
        print(linetosplit[1]+ "--Global Sales " + linetosplit[10])
        try:

         globalsum= globalsum + float(linetosplit[10])
        except ValueError:
             continue
        
    return globalsum
    file1.close()


def finalglobalsales():
    cactusjack=problem3()
    print("\n" + "Final sum of global sales "+ str(cactusjack))
finalglobalsales()

def problem4():

    while True:
        try:
            userinput=float(input("please enter a number or float to be divided by 16 "))
            calc=16/userinput
            break
        except ZeroDivisionError:
            print("cannot divide by zero")
            continue
        except ValueError:
            print("please enter a valid float or integer ")
            continue
    print("final Value " + str (calc))

problem4()