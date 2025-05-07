import sys
import time


def ft_tqdm(lst: range):
    """
    A simple custom progress bar implementation similar to tqdm.

    Args:
        lst (range): The iterable to iterate over.
    """
    total = len(lst)
    start_time = time.time()  # Record the start time
    length = 25  # Length of the progress bar

    for i, item in enumerate(lst):
        percent = (i + 1) / total
        filled_length = int(length * percent)
        bar = '█' * filled_length + '-' * (length - filled_length)

        # Calculate elapsed time
        elapsed_time = time.time() - start_time
        # Calculate remaining time
        if i + 1 < total:
            remaining_time = (elapsed_time / (i + 1)) * (total - (i + 1))
        else:
            remaining_time = 0

        # Format elapsed and remaining time as [MM:SS]
        elapsed_str = time.strftime("%M:%S", time.gmtime(elapsed_time))
        remaining_str = time.strftime("%M:%S", time.gmtime(remaining_time))

        # Calculate iterations per second
        it_per_sec = (i + 1) / elapsed_time if elapsed_time > 0 else 0

        # Write the progress bar to the console
        sys.stdout.write(
            f'\r{int(percent * 100)}%|{bar}| {i + 1}/{total} '
            f'[{elapsed_str}<{remaining_str}, {it_per_sec:.2f}it/s]'
        )
        yield item  # Yield the current item

    # Ensure the progress bar ends cleanly on the same line
    sys.stdout.write('\n')
