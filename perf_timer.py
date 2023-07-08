import logging

# Set Instance of Logging for file
log = logging.getLogger(__name__)

# Set Formatter
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s", "", "%"
)

# Set Stream Handler instance and add formatter
# This outputs text to the terminal
sh = logging.StreamHandler()
sh.setFormatter(formatter)
# sh.setLevel(logging.DEBUG)
log.addHandler(sh)

# Set Filehandler instance and formatter
# This creates a file where the logged data is stored
# By default, mode is a, encoding is None, delay is False
fh = logging.FileHandler(f"{__name__}_data.log", mode="a")
fh.setFormatter(formatter)
# fh.setLevel(logging.DEBUG)
log.addHandler(fh)

# Set Logging Level
log.setLevel(logging.DEBUG)


def run_time(func_to_dec):
    def wrapper(*args, **kwargs):
        import time

        log.debug(f"Function started")
        start = time.perf_counter()
        func_to_dec(*args, **kwargs)
        end = time.perf_counter()
        time_elapsed = end - start
        log.debug(f"Function endded. Time taken is {time_elapsed}")
        return wrapper
