#!/usr/bin/python3
""" Module for 0-minoperations"""

def minOperations(n):
    """
    minOperations
    This function calculates the minimum number of operations needed to get 'n' number of 'H' characters.
    """

    # all outputs should be at least 2 char
    if (n < 2):
        return 0
    # Initialize operations count and root for division check
    ops, root = 0, 2
    # Loop until root is greater than n  
    while root <= n:
        if n % root == 0:
            # total even-divisions by root = total operations
            ops += root 
            # Add root to operations count
            n = n / root  # Update n to reflect division
            # Decrement root to check for smaller factors
            root -= 1
            # Increment root to find next potential factor
        root += 1 
    return ops
