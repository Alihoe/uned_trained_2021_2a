import argparse
import subprocess


def run():


    #data = "default"
    data = "2020_2"

    subprocess.call(["python", "evaluation/scorer/main.py", data])


if __name__ == "__main__":
    run()