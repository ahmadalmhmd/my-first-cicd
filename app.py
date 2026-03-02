def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  if b == 0:
    return "لا يمكن القسمة على ضقر"
return a / b 

if  __name__ == "__main__":
  print("الالة الحاسبة اليسيطة")
  print("=" * 30)
  print(f"5 + 3 = {add(5, 3)}")
  print(f"10 - 4 = {subtract(10, 4)}")
  print(f"6 * 7 = {multiply(6, 7)}")
  print(f"15 / 3 = {divids(15, 3)}")
  print(f"10 / 0 = {divide(10, 0)}")
