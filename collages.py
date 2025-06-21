rank = int(input("Enter you rank here: "))

if(rank<=0):
    print("Please Enter a valid rank")

elif(rank>=2001):
    print("Study harder friend....")


branch = input("Enter your branch here: ")
spcific_branch = ["computer science", "information technology", "ai ml"]

category = input("Enter your cast category: ")
spcific_category = ["open", "ews", "sebc", "sc", "st"]

collage1 = "LD"
collage2 = "VGEC"
collage3 = "Nirma"

if(rank>=1 and rank<=50 and category=="open" or category=="ews" or category=="sebc" or category=="sc" or category=="st"):
    print("Congratulations!!! You can get all the top colleges including: ", collage1, collage2, collage3)

elif(rank<=51 and rank<=100 and category=="open" or category=="EWS"):
    print("Congratulations!!! You can get these colleges: ", collage2, collage3)
  
elif(rank>=101 and rank<=200 and category=="open" or category=="EWS"):
    print("You can get these collage: ", collage3)

elif(rank>=201 and category=="open" or category=="ews"):
    print("Sorry you cannot get any of the top three colleges.")

elif(rank>=201 and rank<=300 and category=="sebc" or category=="sc" or category=="st" and branch=="computer science" or branch=="information technology"):
    print("Congratulations!!! You can get these colleges: ", collage2, collage3)

elif(rank>=301 and rank<=400 and category=="sebc" or category=="sc" or category=="st" and branch=="ai ml"):
    print("Congratulations!!! You can get these colleges: ", collage1, collage3)

elif(rank>=401 and rank<= 450 and category=="sebc" or category=="sc" or category=="st" and branch=="ai ml"):
    print("Congratulations!!! You can get these colleges: ", collage1, collage3)

elif(rank>=451 and category=="sebc"):
    print("Sorry you cannot get any of the top three top colleges.")

elif(rank>=451 and category=="sc" or category=="st"):
    print("Congratulations!!! You can get all the top colleges including: ", collage1, collage2, collage3)

print("This colleges are given on the last year cutoff. Thank you")