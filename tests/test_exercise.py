import pytest
from sciware_testing_python import sum_numbers, add_vectors
from numpy import random as r
import numpy as n

# Edit 4/29/21, with notes..
# names must start with test_* to be found by pytest

def test_sum_numbers_123():
    # basic test to see if we get the expected answer for a simple case.
    sum = sum_numbers([1,2,3])
    assert sum == 6

def test_sum_numbers_yours():
    # write another test of the sum_numbers function
    x = r.rand(10000)
    assert sum_numbers(x)==sum(x)

def test_sum_numbers_empty():
    # what's the sum of an empty list?
    assert sum_numbers([])==0

def test_sum_numbers_inf():
    assert sum_numbers([n.Inf])==n.Inf

#@pytest.mark.xfail(strict=True, raises=TypeError)
def test_sum_strings():
    #assert sciware_testing_python.sum_numbers(["1","2","3"]) == "123"
    pass


# ADDING

def test_add_vectors():
    assert add_vectors([1,2],[3,4])==[4,6]

@pytest.mark.xfail(strict=True)    # marks as should fail
def test_add_vectors2():
    assert add_vectors([1,2],[3])==[4,2]    # fails

# Write a test for the add_vectors function
def test_add_big_vectors():
    # write another test of the sum_numbers function
    x = r.rand(10000)
    y = r.rand(10000)
    assert (n.array(add_vectors(x.tolist(),y.tolist()))==x+y).all()


    # @pytest.raises -> can catch a crash

    # Numpy has own numpy.testing
    
#    https://numpy.org/doc/stable/reference/routines.testing.html

# 
#if you have imported numpy.np, you can do things like np.assert_allclose() to compare arrays that are close within some tolerance 
#*import numpy as np 
#*np.testing.assert_allclose(…) (sorry) 
#The way this works is that assert raises a specific kind of exception (AssertionError). If a test function raises AssertionError, it’s marked as a failed test; if it raises any other exception, it’s marked as an error; and if it doesn’t raise anything, it’s marked as pass. The xfail decorator flips this around a bit so that if the required exception isn’t raised, then it raises AssertionError for you; and if it is raised, it’s caught so that the test appears as passed 







# Write a test for sum_numbers on a list of booleans

