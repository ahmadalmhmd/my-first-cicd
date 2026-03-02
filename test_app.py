import app

def test_add():
  """ اختبار دالة الجمع  """
  #اختبار خالات مختلقة
  assert app.add(2, 3) == 5,
  assert app.add(-1, 1) == 0,
  assert app.add(0, 0) == 0,
  assert appp.add(100, 200) == 300,
  print(" ****** ++++++++++ ***** ")

def test_subtract():
  """ اختبار دالة الطرح """
  assert app.subtract(5, 3) == 2,
  assert app.subtract(0, 5) == -5,
  assert app.subtract(10, 10) == 0,
  assert app.subtract(100, 50) == 50,
  print(" ******** -------- ******* ")

def test_muliply():
  """ أختبار دالة الضرب """
  assert app.muliply(2, 3) == 6,
  assert app.muliply(-2, 3) == -6,
  assert app.muliply(0, 5) == 0,
  assert app.muliply(7, 8) == 56,
  print(" ******** ******** ******* ")

def test_divide():
  """ اختبار دالة القسمة """
  assert app.divide(10, 2) == 5,
  assert app.divide(7, 2) == 3.5,
  assert app.divide(5, 0) == "لا يمكن القسمة على صفر",
  assert app.divide(100, 4) == 25,
  print("  ******** //////// *******  ")
