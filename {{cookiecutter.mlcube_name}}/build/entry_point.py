""" Example entry point script compatible with MLCube protocol. """
import argparse
from enum import Enum
from typing import List


class Task(str, Enum):
    EXAMPLE_TASK = 'example_task'


def example_task(task_args: List[str]) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_file', type=str, default=None, help="Name of an output file")
    args = parser.parse_args(args=task_args)

    with open(args.output_file, 'w') as stream:
        stream.write("Hello from MLCube::example_task task.\n")


def main():
    # Every MLCuber runner passes a task name as the first argument. Other arguments are task-specific.
    parser = argparse.ArgumentParser()
    parser.add_argument('mlcube_task', type=str, help="Task for this MLCube.")

    # The `mlcube_args` contains task name (mlcube_args.mlcube_task)
    # The `task_args` list needs to be parsed later when task name is known
    mlcube_args, task_args = parser.parse_known_args()

    if mlcube_args.mlcube_task == Task.EXAMPLE_TASK:
        example_task(task_args)
    else:
        raise ValueError(f"Unknown task: '{mlcube_args.mlcube_task}'")


if __name__ == '__main__':
    main()
