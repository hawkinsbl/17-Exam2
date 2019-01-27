"""
Exam 2, problem 1.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Ben Hawkins.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import testing_helper
import time


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem1a()
    run_test_problem1b()
    run_test_problem1c()
    run_test_problem1d()


###############################################################################
# Done: 2.  READ the doc-strings for the  sum_of_digits  and  is_prime
# functions defined below.  They are the same as you have seen before.
# After you UNDERSTAND the doc-string (JUST the doc-string, NOT the code),
# ASKING QUESTIONS AS NEEDED, change the above _TODO_ to DONE.
###############################################################################

def sum_of_digits(number):
    """
    What comes in:  An integer.
    What goes out:  Returns the sum of the digits in the given integer.
    Side effects:   None.
    Example:
      If the integer is 83135,
      this function returns (8 + 3 + 1 + 3 + 5), which is 20.
    """
    # -------------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above  sum_of_digits function - it has no _TODO_.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problems below.
    # -------------------------------------------------------------------------
    if number < 0:
        number = -number

    digit_sum = 0
    while True:
        if number == 0:
            break
        digit_sum = digit_sum + (number % 10)
        number = number // 10

    return digit_sum


def is_prime(n):
    """
    What comes in:  An integer n >= 2.
    What goes out:
      -- Returns True if the given integer is prime,
         else returns False.
    Side effects:   None.
    Examples:
      -- is_prime(11) returns  True
      -- is_prime(12) returns  False
      -- is_prime(2)  returns  True
    Note: The algorithm used here is simple and clear but slow.
    """
    for k in range(2, (n // 2) + 1):
        if n % k == 0:
            return False

    return True
    # -------------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above  is_prime  function - it has no _TODO_.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problems below.
    # -------------------------------------------------------------------------


def run_test_problem1a():
    """ Tests the   problem1a   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1a  function:')
    print('--------------------------------------------------')

    format_string = '    problem1a( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 30 + 5  # which is 35
    print_expected_result_of_test([[30, 1, 22, 8, 5]], expected, test_results,
                                  format_string)
    actual = problem1a([30, 1, 22, 8, 5])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 8 + 8  # which is 16
    print_expected_result_of_test([[8, 30, 40, 50, 1, 3, 66, 8]], expected,
                                  test_results, format_string)
    actual = problem1a([8, 30, 40, 50, 1, 3, 66, 8])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = 0
    print_expected_result_of_test([[20, -20]], expected, test_results,
                                  format_string)
    actual = problem1a([20, -20])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 40
    print_expected_result_of_test([[20, 20]], expected, test_results,
                                  format_string)
    actual = problem1a([20, 20])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = 30 + 5  # which is 35
    print_expected_result_of_test([(30, 1, 22, 8, 5)], expected, test_results,
                                  format_string)
    actual = problem1a((30, 1, 22, 8, 5))
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def problem1a(sequence):
    """
    What comes in:  A sequence of numbers.  You may assume that the sequence
      contains at least 2 numbers.
    What goes out:
      -- Returns the sum of the first and last numbers in the sequence.
    Side effects:   None.
    Examples:
      -- problem1a( [30, 1, 22, 8, 5] ) returns 30 + 5 (which is 35).
      -- problem1a( [8, 30, 40, 50, 1, 3, 66, 8] ) returns 8 + 8 (which is 16).
      -- problem1a( [20, -20] ) returns 0.
      -- problem1a( [20, 20] )  returns 40.
      -- problem1a( (30, 1, 22, 8, 5) )  returns 35.
    """
    # -------------------------------------------------------------------------
    # Done: 3. Implement and test this function.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------
    return sequence[0]+sequence[len(sequence)-1]


def run_test_problem1b():
    """ Tests the   problem1b   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1b  function:')
    print('--------------------------------------------------')

    format_string = '    problem1b( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = ['hello', 'the', '1234567', 'six']
    print_expected_result_of_test(
        [['hello', 'four', 'the', '1234567890', '1234567', 'six']],
        expected, test_results, format_string)
    actual = problem1b(
        ['hello', 'four', 'the', '1234567890', '1234567', 'six']
    )
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = ['hi', 'all', 'these', 'byebyebyebye1', 'hi']
    print_expected_result_of_test(
        [['hi', 'all', 'these', 'byebyebyebye1', 'hi']],
        expected, test_results, format_string)
    actual = problem1b(
        ['hi', 'all', 'these', 'byebyebyebye1', 'hi']
    )
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = ['on', 'these', 'bad', '7777777', '444', 'eleventiney']
    print_expected_result_of_test(
        [['nope', 'on', 'these', 'good', 'bad', '7777777', '444',
          'eleventiney']],
        expected, test_results, format_string)
    actual = problem1b(
        ['nope', 'on', 'these', 'good', 'bad', '7777777', '444', 'eleventiney']
    )
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = ['twenty-four', 'on', 'these', 'bad', '444']
    print_expected_result_of_test(
        [['twenty-four', 'on', 'these', 'good', 'bad', '444', 'twenty-three']],
        expected, test_results, format_string)
    actual = problem1b(
        ['twenty-four', 'on', 'these', 'good', 'bad', '444', 'twenty-three']
    )
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = ['yes', 'yes', 'yes']
    print_expected_result_of_test(
        [['yes', 'yes', 'yes']], expected, test_results, format_string)
    actual = problem1b(
        ['yes', 'yes', 'yes']
    )
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = []
    print_expected_result_of_test(
        [['nope', 'nope']], expected, test_results, format_string)
    actual = problem1b(
        ['nope', 'nope']
    )
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = ['yep', 'yes']
    print_expected_result_of_test(
        [['nope', 'none', 'yep', 'yes']], expected, test_results,
        format_string)
    actual = problem1b(
        ['nope', 'none', 'yep', 'yes']
    )
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = ['yep', 'yes']
    print_expected_result_of_test(
        [['none', 'yep', 'nope', 'yes']], expected, test_results,
        format_string)
    actual = problem1b(
        ['none', 'yep', 'nope', 'yes']
    )
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = ['yes', 'yep']
    print_expected_result_of_test(
        [['yes', 'nope', 'none', 'yep']], expected, test_results,
        format_string)
    actual = problem1b(
        ['yes', 'nope', 'none', 'yep']
    )
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    expected = ['yep', 'yes']
    print_expected_result_of_test(
        [['yep', 'yes', 'nope', 'none']], expected, test_results,
        format_string)
    actual = problem1b(
        ['yep', 'yes', 'nope', 'none']
    )
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11:  (Same as #1 but the argument is a tuple)
    expected = ['hello', 'the', '1234567', 'six']
    print_expected_result_of_test(
        [('hello', 'four', 'the', '1234567890', '1234567', 'six')],
        expected, test_results, format_string)
    actual = problem1b(
        ('hello', 'four', 'the', '1234567890', '1234567', 'six')
    )
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def problem1b(strings):
    """
    What comes in:  A sequence of strings.  You may assume that each string
      has length at least 2.
    What goes out:
      -- Returns a list of all the strings in the sequence
           whose length is prime.
    Side effects:   None.
    Examples:
      -- problem1b( ['hello', 'four', 'the', '1234567890', '1234567', 'six'] )
              returns ['hello', 'the', '1234567', 'six']
           since:
             -- the lengths of those strings are prime (5, 3, 7, and 3,
                  respectively)
             -- the lengths of the other two strings are NOT prime
                   (4 and 10, respectively)
      -- See the test cases for more examples, or ASK YOUR INSTRUCTOR
           FOR HELP if this problem's specification is not clear to you.
     """
    ###########################################################################
    # Done: 4. Implement and test this function.
    #          Tests have been written for you (above).
    ###########################################################################
    mylist = []
    for k in range(len(strings)):
        if is_prime(len(strings[k])) is True:
            mylist = mylist + [strings[k]]
    return mylist


def run_test_problem1c():
    """ Tests the   problem1c   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1c  function:')
    print('--------------------------------------------------')

    format_string = '    problem1c( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 1
    print_expected_result_of_test([[30, 2, 2, 9, 1, 0, -10, 4, 1, 40, 2]],
                                  expected, test_results, format_string)
    actual = problem1c([30, 2, 2, 9, 1, 0, -10, 4, 1, 40, 2])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 999
    print_expected_result_of_test([[1, 2, 3]],
                                  expected, test_results, format_string)
    actual = problem1c([1, 2, 3])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = -100
    print_expected_result_of_test([[-100, 2, 2, 9, 1, 0, -10, 4, 1, 40, 2]],
                                  expected, test_results, format_string)
    actual = problem1c([-100, 2, 2, 9, 1, 0, -10, 4, 1, 40, 2])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 2
    print_expected_result_of_test([[30, 2, 2, 9, 10, 90, 10, 40, 19, 40, 2]],
                                  expected, test_results, format_string)
    actual = problem1c([30, 2, 2, 9, 10, 90, 10, 40, 19, 40, 2])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = 999
    print_expected_result_of_test([[]],
                                  expected, test_results, format_string)
    actual = problem1c([])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = 999
    print_expected_result_of_test([[0]],
                                  expected, test_results, format_string)
    actual = problem1c([1])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = -1
    print_expected_result_of_test([[-1]],
                                  expected, test_results, format_string)
    actual = problem1c([-1])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:  Same at Test #1, but a tuple
    expected = 1
    print_expected_result_of_test([(30, 2, 2, 9, 1, 0, -10, 4, 1, 40, 2)],
                                  expected, test_results, format_string)
    actual = problem1c((30, 2, 2, 9, 1, 0, -10, 4, 1, 40, 2))
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def problem1c(integers):
    """
    What comes in:  A sequence of integers.
    What goes out:
      -- Returns the first integer in the sequence that is less than its index,
           or 999 if there is no such integer in the sequence.
    Side effects:   None.
    Examples:
      -- problem1c( [30, 2, 2, 9, 1, 0, -10, 4, 1, 40, 2] )
              returns 1
           since:  It is NOT true that 30 < 0
                   It is NOT true that 2 < 1
                   It is NOT true that 2 < 2
                   It is NOT true that 9 < 3
                   It IS true that 1 < 4  (and so 1 is returned)
      -- problem1c( [1, 2, 3] )
              returns 999
           since none of the three numbers are less than
           their respective indices (0, 1, and 2, respectively).
     """
    ###########################################################################
    # Done: 4. Implement and test this function.
    #          Tests have been written for you (above).
    ###########################################################################
    for k in range(len(integers)):
        if integers[k] < k:
            return integers[k]
    return 999


def run_test_problem1d():
    """ Tests the   problem1d   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1d  function:')
    print('--------------------------------------------------')

    format_string = '    problem1d( {}, {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 813 * 56  # which is 45528
    print_expected_result_of_test(
        [10, [12349, 10000, 477, 56, 813, 55, 324, 56]],
        expected, test_results, format_string)
    actual = problem1d(10, [12349, 10000, 477, 56, 813, 55, 324, 56])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 813 * 55 * 56  # which is 45528
    print_expected_result_of_test(
        [9, [12349, 10000, 477, 56, 813, 55, 324, 56]],
        expected, test_results, format_string)
    actual = problem1d(9, [12349, 10000, 477, 56, 813, 55, 324, 56])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = 813 * 55 * 324 * 56  # which is 45528
    print_expected_result_of_test(
        [3, [12349, 10000, 477, 56, 813, 55, 324, 56]],
        expected, test_results, format_string)
    actual = problem1d(3, [12349, 10000, 477, 56, 813, 55, 324, 56])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 813
    print_expected_result_of_test(
        [11, [12349, 10000, 477, 56, 813, 55, 324, 56]],
        expected, test_results, format_string)
    actual = problem1d(11, [12349, 10000, 477, 56, 813, 55, 324, 56])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = 1
    print_expected_result_of_test(
        [12, [12349, 10000, 477, 56, 813, 55, 324, 56]],
        expected, test_results, format_string)
    actual = problem1d(12, [12349, 10000, 477, 56, 813, 55, 324, 56])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = 55 * 324 * 56 * 11 * 12  # which is 131725440
    print_expected_result_of_test(
        [1, [12349, 10000, 477, 56, 813, 55, 324, 56, 11, 12]],
        expected, test_results, format_string)
    actual = problem1d(1, [12349, 10000, 477, 56, 813, 55, 324, 56, 11, 12])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = 12349
    print_expected_result_of_test(
        [18, [813, 802, 324, 55, 12349, 10000, 477, 56]],
        expected, test_results, format_string)
    actual = problem1d(18, [813, 802, 324, 55, 12349, 10000, 477, 56])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = 12349 * 477  # which is 5890473
    print_expected_result_of_test(
        [17, [813, 802, 324, 55, 12349, 10000, 477, 56]],
        expected, test_results, format_string)
    actual = problem1d(17, [813, 802, 324, 55, 12349, 10000, 477, 56])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = 802
    print_expected_result_of_test(
        [9, [813, 802]],
        expected, test_results, format_string)
    actual = problem1d(9, [813, 802])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    expected = 813
    print_expected_result_of_test(
        [9, [802, 813]],
        expected, test_results, format_string)
    actual = problem1d(9, [802, 813])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = 1
    print_expected_result_of_test(
        [11, [813, 802]],
        expected, test_results, format_string)
    actual = problem1d(11, [813, 802])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    expected = 813
    print_expected_result_of_test(
        [11, [802, 813]],
        expected, test_results, format_string)
    actual = problem1d(11, [802, 813])
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def problem1d(t, sequence):
    """
    What comes in:  An integer t and a sequence of positive integers.
      You may assume that the length of the sequence is even.
    What goes out:
      -- Returns the product of the integers in the second half of the sequence
           whose sum of digits is greater than t.
           Returns 1 if there are no such integers.
    Side effects:   None.
    Examples:
      -- problem1d( 10, [12349, 10000, 477, 56, 813, 55, 324, 56 ] )
            returns (813 * 56)  [which is 45528]
            because 813, 55, 324 and 56 are the integers in the second half
            of the sequence, and of those, only 813 and 56 have sum-of-digits
            greater than 10.
      -- See the test cases for more examples, or ASK YOUR INSTRUCTOR
           FOR HELP if this problem's specification is not clear to you.
     """
    ###########################################################################
    # Done: 4. Implement and test this function.
    #          Tests have been written for you (above).
    ###########################################################################
    total = 1
    for k in range(len(sequence)//2,len(sequence)):
        if sum_of_digits(sequence[k]) > t:
            total = total*sequence[k]
    return total


###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################

def print_expected_result_of_test(arguments, expected,
                                  test_results, format_string, suffix=''):
    testing_helper.print_expected_result_of_test(arguments, expected,
                                                 test_results, format_string,
                                                 suffix)


def print_actual_result_of_test(expected, actual, test_results,
                                precision=None):
    testing_helper.print_actual_result_of_test(expected, actual,
                                               test_results, precision)


def print_summary_of_test_results(test_results):
    testing_helper.print_summary_of_test_results(test_results)


# To allow color-coding the output to the console:
USE_COLORING = True  # Change to False to revert to OLD style coloring

testing_helper.USE_COLORING = USE_COLORING
if USE_COLORING:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_colored
else:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_uncolored

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# The   try .. except   prevents error messages on the console from being
# intermingled with ordinary output to the console.
# -----------------------------------------------------------------------------
try:
    main()
except Exception:
    print('ERROR - While running this test,', color='red')
    print('your code raised the following exception:', color='red')
    print()
    time.sleep(1)
    raise
