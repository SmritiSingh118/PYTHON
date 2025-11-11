height= float(input("enter your height"))
credits=int(input("enter your credits"))
if height>5 and credits>5:
  print("You are not tall enough to ride.")
elif height<5 and credits>5:
  print("You are not tall enough to ride.")
elif height>5 and credits<5:
  print("You don't have enough credits.")
else:
  print("no")
