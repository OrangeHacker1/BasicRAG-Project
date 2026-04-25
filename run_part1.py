from src.ingest import build_starter_collection
from src.evaluator import run_queries

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

build_starter_collection(reset=True)
run_queries(queries, 'outputs/part1_results.csv')