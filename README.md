# README

This repo showcases the process of making a package into a containerized tool, as well as testing that tool before containerization. 

~~~
#You will need to create a python3 environment that contains pytest.
# On BioHPC, this can be done with
module add python/3.10.x-anaconda
~~~

# Basic CI/CD Concepts - Part 1

## What is CI/CD?

Continuous Integration/Continuous Deployment (CI/CD) is a software development practice that enables developers to automate the process of integrating code changes into a shared repository and deploying them to production environments. It aims to streamline the development workflow, improve collaboration among team members, and accelerate the delivery of high-quality software.

At its core, CI/CD involves two key processes: Continuous Integration (CI) and Continuous Deployment (CD). 

* Continuous Integration focuses on automating the integration of code changes into a shared repository, typically triggered by every commit made by developers. This process involves running automated tests to ensure that the new code does not introduce any regressions or errors into the existing codebase.
  * This allows you to ensure that changes to one part of your code doesn't have some unexpected effect on other parts of your code.

* Continuous Deployment, on the other hand, involves automating the deployment of code changes to production or staging environments after they have passed the CI stage. This allows you to standardize the manner in which you roll out your code, to avoid inconsistencies and repeated effort.

CI/CD pipelines form the backbone of this automation process. A pipeline consists of a series of stages, each comprising one or more jobs that execute specific tasks, such as compiling code, running tests, building container images, and deploying applications. By defining these pipelines in configuration files, developers can automate the entire code delivery process, from code changes to deployment.

> # Summary
> * CI is fundamentally based around the idea of <i>testing</i> your code to make sure it's "Still good".
> * CD is based around the idea of <i>getting your code out there</i>, whether that's via a container, a website, or another Git repository. 


MOST IMPORTANTLY: CI and CD both exist on a <i>spectrum</i>. 

At one end of CI, running your code before you push it to a git repo is a very manual and not-very-continuous form of CI. At the other, having every single function, method, class, and program tested for all possible inputs is an extremely labor-intensive and hard-to-maintain form of CI. 

At one end of CD, you might manually generate some figures for a paper, or you might download your code, build it, and push it to the GitLab registry. At the other, you might run further integration tests to make sure that your container works, and then you might push it to several different registries and deploy a website showcasing it. 


The purpose of CI/CD is to <i>simplify your overall process</i>. You shouldn't be pursuing 100% test coverage, but a little bit of testing to make sure that your code works as expected is always good.

If you expect that you'll be doing the same thing several times to check or deploy your code, or you expect that someone else will need to follow in your footsteps and you don't have time to explain the deployment process to them, CI/CD might be a good thing to think about. 

## Testing

As a scientist, it is important to be skeptical of something working "as it's supposed to". As a developer for scientists, it is important to solve that skepticism. It is also important to ensure that your code is as consistent and reliable as it can be, over:
* Time (If I run the same code the same way later, I should get the same results)
* Consistent inputs (Barring configuration, do different datasets get processed in more or less the same way?)
* Versions (If I upgrade to a newer version of a dependency, does my output change?)
* Environments (If I run the same code on the same inputs somewhere else, do I get the same results?)

As testing is just running code and checking expected results, you can also get some outputs for free, like:
* Statistical analyses of your code's performance
* Figures and images
* Test reports  
* Package/binary builds
* Container images

Therefore, it is important to consider what your code does and how you can test it.

A good test has 5 things:
1. Test data
2. Test configurations
3. Test invocations/commands
4. Expected outputs/behavior

By calling your code with known inputs and comparing the results with known outputs, you can verify if your code is functioning as anticipated. 

For example, for a basic pair of Python functions (NB: Might require an _init.py) 
~~~
#!python3

def mul(x, y):
  return x * y

def add(x, y):
  return x + y
~~~

You could have the following (very explicit) tests:
~~~
# Sanity check for addition
Input: a=3;b=3
Config: (None)
Command: add(a,b)
Expect: 6
~~~
~~~
# Sanity check for multiplication
Input: a=3;b=3
Config: (None)
Command: mul(a,b)
Expect: 9
~~~

Shortened to a more sensible form, the tests would be:
~~~
add(3,3)=6
mul(3,3)=9
~~~

However, testing breaks down into basically two regimes: <i>Typical Cases</i> and <i>Edge Cases</i>.
 * Typical Cases: Exactly what it sounds like. Example data and example outputs that showcase how your process works.
 * Edge Cases: Circumstances or combinations of inputs/config which are somehow 'unique' or 'extreme'.
   * Very large inputs
   * Known-bad outputs




It is therefore sensible to create additional cases:
~~~
import sys

# Creating extreme values as constants
INTMAX = sys.maxsize
print("Max integer value:", INTMAX)

# Test Cases
add(3,3)==6
mul(3,3)==9

add(3,INTMAX)>INTMAX
add(INTMAX,3)>INTMAX

~~~

This split of typical cases and edge cases can help you to quickly create a basic set of tests for your code. 


## Creating additional tests

### Breaking cases
Generally, whenever something breaks, you may consider using that input combination as a test case. 

### Property-based tests
Sometimes you can get lucky and have a problem with well-known properties or special inputs. For addition and multiplication, examples of these are
  * Commutative property: A+B=B+A, A\*B=B\*A
  * Distributive properties: 
    * Left: A\*(B+C)=A\*B+A\*C
    * Right: (B+C)\*A=B\*A+C\*A
  * Properties of 0 and 1:
    * A*0=0
    * A*1=A
    * A+0=A
    * A+1>A

Implementation of these is covered in an exercise.

## GitLab CI
We will be skipping over CI with other services since that's out of scope.

In GitLab, all projects can potentially have CI enabled. 
To define CI, you must create a file `.gitlab-ci.yml`, which will live in the root of your code repository. This must be included in your git repository, and it contains the instructions on how your CI environment should be run by a runner.

Just having a .gitlab-ci.yml file alone is not enough to run your CI. For that, you must also have runners registered and available to your GitLab project.

Runners are long-lived processes which execute CI code. Their behavior is a function of their environment, so you must be aware of the environment in which your runners are running.
  * Your laptop at home?
  * A machine in the cloud
  * On a BioHPC workstation

A runner must first be registered to a group or project - this makes it available for all CI pipelines in that group or project.

The runner must then be started - usually by a command like `gitlab-runner run` .


# EXERCISES

For any of these exercises, feel free to substitute in your own code and modify the existing code to fit. 

You should be able to run your tests using `pytest` in the base directory of this repository. 

~~~
# Explicitly running pytest as a python3 module:
python3 -m pytest

# More verbose output, individual tests:
python3 -m pytest -v

# Same verbosity, outputs a report of test statuses. 
python3 -m pytest -v --junitxml=report.xml
~~~


# Exercise A: Corner and Edge Cases

Write additional test cases to cover further corner cases:

- Providing a string as input
- Providing an array/list of numbers as input
- Providing complex numbers and matrices as input. Note that this may require additional packages like NumPy.

# Exercise B: Property-based tests

Say that you have defined a certain set of properties for your code, such as in the following, also located in `...tests/test_03_propertybased.py`

~~~
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

~~~

As these are known mathematical properties of the thing(s) we want to test, and unrelated to the inputs chosen, we can use them to make an arbitrary number of tests:

~~~
import random

def generate_random_numbers(N, A, B, seed=None):
    """
    Generate N random numbers between A and B (inclusive).
    
    Args:
    N (int): The number of random numbers to generate.
    A (int): The lower bound of the random numbers.
    B (int): The upper bound of the random numbers.
    seed (int): Optional. The random seed to use for reproducibility.
    
    Returns:
    list: A list containing N random numbers.
    """
    if seed is not None:
        random.seed(seed)
    return [random.randint(A, B) for _ in range(N)]
~~~

### Exercise B elements:

1. Using the code skeleton in `test_03_propertybased.py`, write driver code which uses the `generate_random_numbers` function to create two test datasets: One which is truly random (`randseed=None`), and the other which uses a seed you specify to control the randomness of that test array.

2. Write additional assertions and code to test the following properties, without writing explicit test cases:
  - That the sum of a number and its negative is 0
  - That the product of a number and its inverse is 1.
  - The associative properties, that A+(B+C)=(A+B)+C, and A\*(B\*C)=(A\*B)\*C



## Exercise C: Testing code with fixtures

When testing code, it can be very computationally expensive to set up the environment for your tests to run in, and so it is often the case that you would like to re-use objects from one test in another.

Fixtures are the solution to this - they are resources that can be consumed by individual tests in order to execute their code. This might be a model matrix, or pre-downloading a large dataset, or any other resource-intensive prep step. 

In the file `...tests/tests_with_fixtures/test_04_withfixtures.py` you will see code which performs the property-based tests of Exercise B. In `...tests/tests_with_fixtures/conftest.py` you will see code which generates the fixtures for this code. 

Noticing how the code uses `number_list`, and referring to the pytest documentation at https://docs.pytest.org/en/7.1.x/how-to/fixtures.html#fixture-parametrize , modify the fixture so that it uses several different seeds, including `None`.



## Exercise D: Using test drivers

You may have noticed a great deal of similar code in the property-based tests, mainly related to error printing and looping.

Using the commented-out code in `test_05_drivers.py`, write a modified form of the property-based tests which uses the driver code to iterate over a list of different tests and their arguments to provide the same test functionality.

The case for the multiplicative identity (A*1=A) is included for you. 


# CI/CD exercises

When you have completed the test exercises to your satisfaction, you should explore automating the tests. You can skip to this step directly, and the code should work as expected.

## Exercise E: Testing your code and container with Bash.

If you are writing code that is meant to function as an application, you will often want to test it 'externally' by calling it. Internal package tests like pytest can be very helpful, but the packaging process can cause some interesting side effects that are hard to detect.

Test this code by issuing the command `python3 main.py 2 4`. It should output the correct sum and product of the two numbers entered:

~~~
#> python3 main.py 2 4
The sum of 2 and 4 is: 6
The mul of 2 and 4 is: 8
~~~

* Write a short Bash script to test some inputs and outputs for the code. 
* Build the container for this package by running `podman build . -t local_newmath`
* Test that the resulting container provides the same outputs for the same inputs as the Bash script.

~~~
#> podman run local_newmath 2 4
The sum of 2 and 4 is: 6
The mul of 2 and 4 is: 8
~~~

By testing your code and container externally, you can re-use the same tests.

## Exercise F: 

By this point, you should have already tested with pytest, with Bash calling Python, and with Bash calling the container.

You can now automate your tests using the `.gitlab-ci.yml` file provided herein. 


~~~
Set up the container
~~~

##


 Set our parameters for this test.

lowbound=0
hibound=10
N=10
randseed=69105

num_list = generate_random_numbers(N, lowbound, hibound, seed=randseed)

test_mul_unit(num_list)
test_mul_zero(num_list)
test_add_unit(num_list)
test_add_zero(num_list)

test_add_comm(num_list)
test_mul_comm(num_list)
test_left_dist(num_list)
test_right_dist(num_list)

~~~

In this case, the `randseed` variable is set to control how the random number generation process takes place. This helps to remove randomness from your testing process, but it can be a good idea to have a truly random test as well. For simplicity, we'll create a function to wrap all of those individual tests:

~~~
def run_test_battery(number_list):
  test_mul_unit(num_list)
  test_mul_zero(num_list)
  test_add_unit(num_list)
  test_add_zero(num_list)
  test_add_comm(num_list)
  test_mul_comm(num_list)
  test_left_dist(num_list)
  test_right_dist(num_list)

num_list_truerandom = generate_random_numbers(N, lowbound, hibound, seed=None)
num_list = generate_random_numbers(N, lowbound, hibound, seed=randseed)

run_test_battery(num_list_truerandom)
run_test_battery(num_list)

~~~

You may have noticed quite a bit of repeated code in the previous section - this is usually to be avoided. To get around this, we will create a test driver:

~~~ 

def Test_Driver_Unary(test_name,test_function,input):
  count=0
  total_cases=len(input)
  for num in input:
    test_function(num)
    count=count+1
  print("{} verified with {} tests among {} numbers".format(test_name,count,total_cases))

def Test_Driver_Binary(test_name,test_function,inputA,inputB):
  count=0
  total_cases=len(inputA)*len(inputB)
  for numA in inputA:
    for numB in inputB:
      test_function(numA,numB)
      count=count+1
  print("{} verified with {} tests among {} numbers".format(test_name,count,total_cases))

def Test_Driver_Ternary(test_name,test_function,inputA,inputB,inputC):
  count=0
  total_cases=len(inputA)*len(inputB)*len(inputC)
  for numA in inputA:
    for numB in inputB:
      for numC in inputC:
        test_function(numA,numB,numC)
        count=count+1
  print("{} verified with {} tests among {} numbers".format(test_name,count,total_cases))

Test_Driver_Unary("MultiplyOne",assert_mul_unit,num_list)
Test_Driver_Unary("MultiplyZero",assert_mul_zero,num_list)
Test_Driver_Unary("AddOneBigger",assert_add_unit,num_list)
Test_Driver_Unary("AddZeroSame",assert_add_zero,num_list)

Test_Driver_Binary("CommAdd",is_add_comm,num_list,num_list)
Test_Driver_Binary("CommMul",is_mul_comm,num_list,num_list)

Test_Driver_Ternary("IsLeftDist",is_left_dist,num_list,num_list,num_list)
Test_Driver_Ternary("IsRightDist",is_right_dist,num_list,num_list,num_list)

~~~