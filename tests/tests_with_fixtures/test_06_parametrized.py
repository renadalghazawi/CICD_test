






# @pytest.mark.parametrize("test_name", ["100", "101", "102"])
# def Test_Driver_Unary(test_name,test_function,input):
#   count=0
#   total_cases=len(input)
#   for num in input:
#     test_function(num)
#     count=count+1
#   print("{} verified with {} tests among {} numbers".format(test_name,count,total_cases))

# def Test_Driver_Binary(test_name,test_function,inputA,inputB):
#   count=0
#   total_cases=len(inputA)*len(inputB)
#   for numA in inputA:
#     for numB in inputB:
#       test_function(numA,numB)
#       count=count+1
#   print("{} verified with {} tests among {} numbers".format(test_name,count,total_cases))

# def Test_Driver_Ternary(test_name,test_function,inputA,inputB,inputC):
#   count=0
#   total_cases=len(inputA)*len(inputB)*len(inputC)
#   for numA in inputA:
#     for numB in inputB:
#       for numC in inputC:
#         test_function(numA,numB,numC)
#         count=count+1
#   print("{} verified with {} tests among {} numbers".format(test_name,count,total_cases))