#libraries
import random

#essensial lists and dictionaries
essensials={
"caps" :[chr(x) for x in range(65,91)],
"lows" :[chr(x) for x in range(97,123)],
"chars" :["!","@","#","$","%","&","*","^","-","_"],
"nums" :[str(x) for x in list(range(0,10))]
}
listForChosing=["caps", "lows", "nums", "chars"]
dictForChosing= {"caps": 1, "lows": 1, "nums": 1, "chars":1}
myPasswordList=[]


#this one line function take a list and gives you a random item of that list.
giveMeRandom = lambda mylist: random.choice(mylist)

#this function decides randomly how many of each kind of charecters should your password have.
def howManyOfWhat(length):
    for item in range(length-4):
        tempChoice=giveMeRandom(listForChosing)
        dictForChosing[tempChoice]=dictForChosing[tempChoice]+1

#this function checks the length of your password and make your password.
def makePassword():
    length=int(input("what is your password length?: "))

    if length < 6:

        print("sorry! I can't make good short passwords.please try a bigger number(at least 6).")
        return makePassword()

    else:

        howManyOfWhat(length)
        for item in dictForChosing:
            for count in range(dictForChosing[item]):
                myPasswordList.append(giveMeRandom(essensials[item]))


        finalPassword = ""
        for item in range(length):
            tempElement=giveMeRandom(myPasswordList)
            finalPassword += tempElement
            myPasswordList.remove(tempElement)
        print("here is your password: ")
        print(finalPassword)


#action!
makePassword()