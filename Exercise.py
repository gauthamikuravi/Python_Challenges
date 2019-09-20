from sys import argv

scripts,user_name = argv
prompt = '> '
print("Hi {user_name}, I am " ,scripts)
print("Let me ask you few questions")
print("Hi {user_name}, do you like python?")
likes = input(prompt)
print("where did you learn about python?")
learn = str(input(prompt))
print("how comfortable are you in python on scale of 10?")
scale = str(input(prompt))