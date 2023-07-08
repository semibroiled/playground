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

# Create Parser Instance
parser = argparse.ArgumentParser()

# Create Subparsers for future functionality
subparser = parser.add_subparsers(dest="command")

# Subparser for fibonacci
fibonacci_series = subparser.add_parser("fib")

# Subparser Greetings
salve_greet = subparser.add_parser("salve")


# Make argument parameters
# Greetings!
salve_greet.add_argument(
    "--echo", type=str, help="Type your name for a customized greeting"
)

# For Fibonacci
fibonacci_series.add_argument(
    "--upto",
    type=int,
    required=True,
    help="Upto which number should the fibonacci sequence be calculated",
)

fibonacci_series.add_argument(
    "--first",
    type=int,
    help="Starting Term of your fibonacci Sequence",
)

fibonacci_series.add_argument(
    "--second",
    type=int,
    help="Next Term of your fibonacci Sequence after Starting Term",
)

args = parser.parse_args()


if __name__ == "__main__":
    # Starting run of application
    log.info(f"Starting Application")

    # Test for successful input of cli args and run app
    try:
        if args.command == "salve":
            if args.echo:
                greetings = f"Moin {args.echo}!"
                print(greetings)
                log.info(greetings)
            else:
                print("moin...")

        if args.command == "fib":
            log.info("Calculating Fibonacci Series...")

            if args.upto:
                log.info(f"{args.upto} given as input for first positional argument")

                end = args.upto
                series = fibonacci(end)

                print(
                    f""" Your list of fibonacci numbers upto 
                {end} are:\n {series}"""
                )
    except ValueError as ve:
        log.error(
            f"Value error. Check that your argument is the right type\
                  \n{ve}"
        )
    except TypeError as te:
        log.error(f"{te}")
    finally:
        pass
