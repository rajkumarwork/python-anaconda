#!/usr/bin/env conda-execute
"""
A script that uses numpy's random normal distribution to print 3 numbers.

"""

# conda execute
# env:
#  - python >=3
#  - numpy
# run_with: python

import numpy as np

print(np.random.normal(size=3))
