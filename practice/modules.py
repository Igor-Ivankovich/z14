# import homework2.homework
# from homework2 import homework
# # from homework2.homework import factorial, count_of_max_numbers
#
# from homework2.homework import custom_range as other_name
# from homework2.homework_hard import custom_range
import sys
from decorators import timer
print(sys.argv)
print(sum(map(int, sys.argv[1:])))