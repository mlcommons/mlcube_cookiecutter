""" Example entry point script compatible with MLCube. """
import argparse
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
from enum import Enum
from typing import List


class Task(str, Enum):
    EXAMPLE_TASK = '{{cookiecutter.mlcube_name}}'


def {{cookiecutter.mlcube_name}}(task_args: List[str]) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_file', type=str, default=None, help="Name of an output file")
    parser.add_argument('--parameters_file', '--parameters-file', type=str, required=True,
                        help="Name of the parameter file.")
    args = parser.parse_args(args=task_args)

    # Replace below lines with user implementation
    with open(args.parameters_file) as stream:
        config = yaml.load(stream.read(), Loader=Loader)
    with open(args.output_file, 'w') as stream:
        stream.write(f"Running {{cookiecutter.mlcube_name}} task with parameters '{config}'.\n")
    

def main():
    # Every MLCuber runner passes a task name as the first argument. Other arguments are task-specific.
    parser = argparse.ArgumentParser()
    parser.add_argument('mlcube_task', type=str, help="Task for this MLCube.")

    # The `mlcube_args` contains task name (mlcube_args.mlcube_task)
    # The `task_args` list needs to be parsed later when task name is known
    mlcube_args, task_args = parser.parse_known_args()

    if mlcube_args.mlcube_task == Task.EXAMPLE_TASK:
        {{cookiecutter.mlcube_name}}(task_args)
    else:
        raise ValueError(f"Unknown task: '{mlcube_args.mlcube_task}'")


if __name__ == '__main__':
    main()
