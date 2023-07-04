"""Console script for pyrobotlab."""

import fire


def help():
    print("pyrobotlab")
    print("=" * len("pyrobotlab"))
    print("This is a Python interface to MyRobotLab")


def main():
    fire.Fire({"help": help})


if __name__ == "__main__":
    main()  # pragma: no cover
