import logging
import argparse
import sys
import os
from fibonacci import fibonacci

# Setup Module Level Logging for our Running Application

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


# Setup CLI for calling application from Terminal

parser = argparse.ArgumentParser()

# Make argument parameters
parser.add_argument(
    "--upto",
    type=int,
    required=True,
    help="Upto which number should the fibonacci sequence be calculated",
)

parser.add_argument(
    "--first",
    type=int,
    help="Starting Term of your fibonacci Sequence",
)

parser.add_argument(
    "--second",
    type=int,
    help="Next Term of your fibonacci Sequence after Starting Term",
)

args = parser.parse_args()


if __name__ == "__main__":
    log.info(f"Starting Application")

    # Test for successful input of cli args
    try:
        if args.upto:
            log.info(f"{args.upto} given as input for first positional argument")

            end = args.upto
            series = fibonacci(end)

            print(
                f""" Your list of fibonacci numbers upto 
            {end} are:\n {series}"""
            )
        else:
            raise Exception("There is no required positional argument given")
    except Exception as user_e:
        print("Run again with proper arguments. Type -h for help")
        log.error("{user_e} raised")
    except ValueError as ve:
        log.error(
            f"Value error. Check that your argument is the right type\
                  \n{ve}"
        )
    finally:
        pass
