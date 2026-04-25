import time

def exponential_backoff_retry(func, retries=3):
    for i in range(retries):
        try:
            return func()
        except Exception:
            time.sleep(2 ** i)
    raise RuntimeError('Max retries exceeded')