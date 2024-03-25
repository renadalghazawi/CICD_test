# We are testing this package, so import that code.
from newmath.add import add
from newmath.mul import mul

# First define the property you are trying to test.
def assert_mul_unit(A):
  assert mul(A,1) == A, "MultiplyUnit failed for number: {}".format(A)

def test_mul_unit(number_list):
  for num in number_list:
    assert_mul_unit(num)
  
def assert_mul_zero(A):
  assert mul(A,0) == 0, "MultiplyZero failed for number: {}".format(A)

def test_mul_zero(number_list):
  for num in number_list:
    assert_mul_zero(num)

def assert_add_zero(A):
  assert add(A,0) == A, "Addition identity failed for number: {}".format(A)

def test_add_zero(number_list):
  for num in number_list:
    assert_add_zero(num)
        
def assert_add_unit(A):
  assert add(A,1) > A, "Succession property failed for number: {}".format(A)

def test_add_unit(number_list):
  for num in number_list:
    assert_add_unit(num)

# Commutative properties

def is_add_comm(A,B):
  assert add(A,B) == add(B,A), "Commutative add. property failed for numbers: A={},B={}".format(A,B)

def test_add_comm(number_list):
  count=0
  for num1 in number_list:
    for num2 in number_list:
      assert add(num1,num2) == add(num2,num1), "Commutative add. property failed for number: {}".format(num)
      count=count+1
  print("Commutative addition property verified with {} tests among {} numbers".format(count,len(number_list)))

def is_mul_comm(A,B):
  assert mul(A,B) == mul(B,A), "Commutative mult. property failed for numbers: A={},B={}".format(A,B)
  
def test_mul_comm(number_list):
  count=0
  for num1 in number_list:
    for num2 in number_list:
      assert mul(num1,num2) == mul(num2,num1), "Commutative mult. property failed for number: {}".format(num)
      count=count+1
  print("Commutative multiplication property verified with {} tests among {} numbers".format(count,len(number_list)))

# Left: A*(B+C)=A*B+A*C
def is_left_dist(A,B,C):
  assert mul(A,add(B,C)) == add(mul(A,B),mul(A,C)), "Left Distributive property A*(B+C)=A*B+A*C failed for numbers: A={},B={},C={}".format(A,B,C)

def test_left_dist(number_list):
  count=0
  for A in number_list:
    for B in number_list:
      for C in number_list:
        is_right_dist(A,B,C)
        count=count+1
  print("Left distributive property verified with {} tests among {} numbers".format(count,len(number_list)))


def is_right_dist(A,B,C):
  assert mul(add(B,C),A) == add(mul(B,A),mul(C,A)), "Right Distributive property (B+C)*A=B*A+C*A failed for numbers: A={},B={},C={}".format(A,B,C)

def test_right_dist(number_list):
  count=0
  for A in number_list:
    for B in number_list:
      for C in number_list:
        is_right_dist(A,B,C)
        count=count+1
  print("Right distributive property verified with {} tests among {} numbers".format(count,len(number_list)))




