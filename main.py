import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
options=[rock,paper,scissors]
input1=int(input("choose 0 for rock,1 for paper and 2 for scissor:"))
print(options[input1])

print("Computer chose:")
input2=random.randint(0,2)
print(options[input2])

if input1 is input2:
    print("Match draw")
elif input1==0 and input2==2 or input1==1 and input2==0 or input1==2 and input2==1:
    print("You won")
else:
    print("You lost")