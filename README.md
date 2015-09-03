# simpleStatistics
simpleStatistics is a lightweight statistics library written in pure python.

NOTE: This code is still in in active development use at your own risk.

The goal of this project is to provide the python community with a simple statistics library compatible with python 2.7 
and 3.4+. The scope of this project is that the module should handle the statistical formulas and tests typically found 
in a semester long undergraduate research statistics course. simpleStatistics is intended to have a very low learning
curve for people with a rudimentary understanding of statistics so they can solve problems in code more quickly.

Examples:

import simpleStatistics

test_data = [1, 2, 3, 3, 3, 4]

descriptive_statistics = simpleStatistics.DescriptiveStatistics()

summarised_data = descriptive_statistics.summarise_descriptive_statistics(test_data)

print(summarised_data)

'''
 Above command results
 {'min': 1, 'max': 4, 'median': 3.0, 'number': 6, 'range': 3, 'mode': 3, 'standard_deviation': 1.032, 'mean': 2.66}
'''