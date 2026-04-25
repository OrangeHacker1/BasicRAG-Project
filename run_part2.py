from src.add_custom import add_custom_functions
from src.evaluator import run_queries

add_custom_functions()

"""
    First 5 are targeted. Second 5 are cross evaluation.
    api: 'How do I retry API calls with backoff?'
    file: 'How do I load JSON from file?'
    math: 'How do I calculate moving average?'
    text: 'How do I count words in text?'
    validation: 'How do I validate an email address?'
"""


queries = [
    'How do I validate an email address?',
    'How do I calculate moving average?',
    'How do I retry API calls with backoff?',
    'How do I count words in text?',
    'How do I load JSON from file?',
    'How do I decode JSON?',
    'How do I sort a list?',
    'How do I make an HTTP request?',
    'How do I parse command line arguments?',
    'How do I read a file line by line?'
]

# Original part1
"""
queries = [
    'How do I decode JSON?',
    'How do I sort a list?',
    'How do I make an HTTP request?',
    'How do I parse command line arguments?',
    'How do I read a file line by line?',
    'How do I remove duplicates from a list?',
    'How do I convert bytes to string?',
    'How do I run a factorial?',
    'How do I retry failed operations?',
    'How do I work with URLs?'
]
"""

run_queries(queries, 'outputs/part2_results.csv')