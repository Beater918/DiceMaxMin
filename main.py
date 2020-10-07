import random
player = 5;
score = 0;
number = random.randint(1,100)
print("First number = ", number, "\n")

while(player != 0):
  n = random.randint(1,100)
  ans = input("Bigger(+) Smaller(-): ")
  if( ans == "+" and (n-number) >= 0):
    print("You Got This (",n,")\n");
    score=score - max(n,number)
  elif( ans == "-" and (n-number) < 0):
    print("You Got This (",n,")\n");
    score=score - max(n,number)
  else:
    print("You miss it (",n,")\n")
    player-=1
    if (score > 15) :
      score=score - 15
     else:
        score =0


  number = n


print("You Lost (-",score,"-)\n")
