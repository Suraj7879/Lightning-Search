import time

def timing(method):
    """
    A decorator function to measure the execution time of a function or method.
    This decorator records the time before calling the function and after it returns,
    then computes and prints the execution time difference. Due to some overhead,
    the results might not be extremely precise but should be sufficient for most use cases.

    Example usage:

        @timing
        def example_function():
            print('Executing the example function...')
            time.sleep(2)

        example_function()

    Output:

        Executing the example function...
        example_function took 2.000321388244629 seconds
    """
    def timed(*args, **kwargs):
        start = time.time()
        result = method(*args, **kwargs)
        end = time.time()

        execution_time = end - start
        if execution_time < 0.001:
            print(f'{method.__name__} took {execution_time * 1000:.2f} milliseconds')
        else:
            print(f'{method.__name__} took {execution_time:.2f} seconds')

        return result

    return timed
