score = input("Enter score: ")
usrSrc=0.0
try:
  usrScr = float(score)
except:
    print("Invalid score")
    quit()

if usrScr >= 0.9 and usrScr <= 1.0:
    print("A")
elif usrScr >= 0.8 and usrScr < 0.9: 
    print("B")
elif usrScr >= 0.7 and usrScr < 0.8:
    print("C")
elif usrScr >= 0.6 and usrScr < 0.7:
    print("D")
elif usrScr < 0.6 and usrScr >= 0.0:
    print("F")
elif usrScr < 0.0 or usrScr > 1.0:
    print("Please enter score from 0.0 to 1.0")
