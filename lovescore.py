# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
first_name1 = name1.lower()
second_name2 = name2.lower()
couple = first_name1 + " " + second_name2
# print(couple)
t = couple.count('t')
r = couple.count('r')
u = couple.count('u')
e = couple.count('e')

l = couple.count('l')
o = couple.count('o')
v = couple.count('v')
e = couple.count('e')

true = str(t + r + u + e)
love = str(l + o + v + e)
score = true + love
love_score = int(score)

if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}")





