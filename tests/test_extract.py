from datetime import datetime, timezone
import logging

from datetime import datetime, timezone

def logger(function):
    """
    Decorator function that logs the execution time and result of a given function.

    Args:
        function: The function to be logged.

    Returns:
        The inner function that logs the execution time and result.
    """
    def inner_function(*args, **kwargs):
        print(f"A função {function.__name__} foi chamada ás {datetime.now(timezone.utc)}")
        result = function(*args, **kwargs)
        print(f"A função {function.__name__} foi concluída ás {datetime.now(timezone.utc)}")
        print(f"O resultado é: {result}")
    return inner_function

@logger
def soma(x,y):
    logging.info("teste")
    return x + y
    
soma(1,2)
        