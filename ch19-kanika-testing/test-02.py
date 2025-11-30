s = "python"

rev = "" # empty string


for ch in s: #p , y , t, h, o, n
  print("Current ch value", ch, "current rev value", rev)
  rev = ch + rev #p, y+p, t+y+p, h+t+y+p, o+h+t+y+p, n+o+h+t+y+p


print("Reverse string is", rev)


for i in range(1,5):
    print("loop", i)

    
