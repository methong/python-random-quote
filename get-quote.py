import random
def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 14
  rnd1 = random.randint(0, last)
  rnd2 = random.randint(0, last)
  mix = quotes[rnd1] + quotes[rnd2]
  
  print(mix)
 

if __name__== "__main__":
  primary()
