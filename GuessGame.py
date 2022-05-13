#GuessGame assigment
import random

#Methods
#1. generate_number - Will generate number between 1 to difficulty and save it to
#secret_number.
#2. get_guess_from_user - Will prompt the user for a number between 1 to difficulty and
#return the number.
#3. compare_results - Will compare the secret generated number to the one prompted
#by the get_guess_from_user.
#4. play - Will call the functions above and play the game. Will return True / False if the user
#lost or won.


def generate_number(difficulty):
  # generate some integers
    n = random.randint(0,difficulty)
    print(n)
  #save the number into a secret number
    Secret_Number=n
    print("The secret number is", Secret_Number)
    return Secret_Number

def get_guess_from_user(difficulty):
  print("Please choose a number between 1 and", difficulty)
  i = input()
  try:
      User_Choice= int(i)
  except ValueError:
      print("I am afraid %s is not a number" % i)
      return User_Choice, -1
  else:
      print("User_Choice=",User_Choice)
      if User_Choice > difficulty:
        print("\nNumber is out of range")
        return User_Choice,-1
      else:
        return User_Choice,0


def compare_results(Secret_Number,User_Choice):
    if Secret_Number == User_Choice:
      print("\n User_Choice and difficulty are the same")
    else:
      print("2 numbers are not the same")


def play():
  Secret_Number = generate_number(10)
  User_Choice,Error_Code = get_guess_from_user(10)
  if Error_Code==0:
    compare_results(Secret_Number,User_Choice)


play()