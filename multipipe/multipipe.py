import os
from typing import Any, Callable, Generator, Iterable, List, Tuple, Union

from multiprocess import Pool


def execute(input: Tuple[Any, List[Callable]]) -> Any:
    """Internal usage."""
    # Unpack the tuple
    x = input[0]
    callables = input[1]

    # Execute the pipeline
    for func in callables:
        x = func(x)

    return x


def prepare_inputs(iterable: Iterable, callables: List[Callable]) -> Generator:
    """Internal usage."""
    for x in iterable:
        yield (x, callables)


def to_generator(inputs: Iterable, chunksize: int, n_threads: int):
    """Internal usage."""
    with Pool(n_threads) as pool:
        yield from pool.imap(execute, inputs, chunksize)


def to_list(inputs: Iterable, chunksize: int, n_threads: int):
    """Internal usage."""
    return list(to_generator(inputs, chunksize, n_threads))


class Multipipe:
    def __init__(self, callables: List[Callable], n_threads: int = 0) -> None:
        """Multipipe constructor.

        Args:
            callables (List[Callable]): List of callables.

            n_threads (int, optional): Number of threads to use for computations. If zero, it will use all the available threads. Defaults to 0.
        """
        self.callables = callables
        self.n_threads = n_threads if n_threads > 0 else os.cpu_count()

    def __call__(
        self, iterable: Iterable, chunksize: int = 1_000, generator: bool = False
    ) -> Union[Generator, List]:
        """Execute the pipeline on the given iterable.

        Args:
            iterable (Iterable): Any iterable object.

            chunksize (int, optional): Chunksize. Defaults to 1_000.

            generator (bool, optional): If True, it will return a generator. Defaults to False.

        Yields:
            Union[Generator, List]: Transformed inputs.
        """
        inputs = prepare_inputs(iterable, self.callables)

        if generator:
            return to_generator(inputs, chunksize, self.n_threads)
        else:
            return to_list(inputs, chunksize, self.n_threads)
