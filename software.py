Age=dict()


def switch(i):
    switcher={
                    1: InsertData,
                    2: UpdateData,
                    3: DeleteData,
                    4: ShowData
             }
    return switcher.get(i,'no option found')

    
def App(): 
    while True:
        print("1.Enter the data:")
        print("2.Update the data")
        print("3.Delete the data")
        print("4.Show the data")
        print("Enter 0 to quit")
        opt=int(input("Please choose option from above:"))
        if (opt > 0 and opt <5):
            ans=switch(opt)
            ans()
            
        elif (opt==0):
            break


def InsertData():
    name=input("Enter Name:")
    age=int(input("Enter age:"))
    Age.update({name:age})
    print("new data added\n")
    
def UpdateData():
    name=input("Enter Name:")
    age=int(input("Enter age:"))
    if name in Age.keys():
        Age.update({name:age})
        print("new data updated\n")
    else:
        print("no item in the dictionary\n")
    
def DeleteData():
    print("Enter the key you want to delete:")
    delete=input()
    if delete in Age.keys():
        del Age[delete]
    else:
        print("no item found")
        
def ShowData():
    for i,j in Age.items():
        print(i,'=',j)
        