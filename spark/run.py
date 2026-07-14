import argparse
import subprocess
import sys


COMMANDS = {

    "bronze": "src.bronze.main",

    "silver": "src.silver.main",

    "gold": "src.gold.main"

}


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(

        "job",

        choices=COMMANDS.keys()

    )

    args = parser.parse_args()

    subprocess.run(

        [

            sys.executable,

            "-m",

            COMMANDS[args.job]

        ],

        check=True

    )


if __name__ == "__main__":

    main()