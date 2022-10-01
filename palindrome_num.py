def palin(n):
  rev = 0
  temp = n
  while(temp>0):
    digit = temp%10
    rev = rev*10+digit
    temp = temp//10
  if(rev == n):
    print("Yes, it is a palindrome number.")
  else:
    print("No, it is not a palindrome number.")
 
num = int(input("Enter a number you want to check if it is a palindrome or not : "))
palin(num)
