# MLCube Project Template
This repository provides a cookiecutter-based template for [MLCommons](https://mlcommons.org/) MLCubes. A detailed
description of MLCubes can be found [here](https://mlcommons.github.io/mlcube/). 

## Prerequisites
Currently, the MLCube supports docker- and singularity-based cubes. The cookiecutter template comes with docker
configuration files.  

[![asciicast](getting-started.gif)](https://asciinema.org/a/Mnl0Kh9uNZWD9Y6MkgQewheeP)

## Initialize python environment
- Install [cookiecutter](https://pypi.org/project/cookiecutter/) for creating MLCubes from templates.
- Install [mlcube-docker](https://pypi.org/project/mlcube-docker/) for running docker-based cubes.
```
virtualenv -p python3 ./env && source ./env/bin/activate
python -m pip install --upgrade pip && pip install cookiecutter mlcube-docker
```

## Creating MLCubes from cookiecutter template
Run the following commands to create a directory for MLCube projects and create a simple project from cookiecutter
template. The cookiecutter will ask several questions, such as MLCube name and author.
> Do not use `~/mlcube` directory. It is used by the MLCube runtime as a default cache directory and storage location.
> For instance, by default, MLCube stores singularity containers here.
```
$ mkdir -p ~/mlcube_projects && cd ~/mlcube_projects 
$ cookiecutter https://github.com/mlcommons/mlcube_cookiecutter.git

mlcube_name [my_mlcube]:
mlcube_description [my_mlcube_description]:
author_name [mlcube_author_name]:
author_email [mlcube_author_email]:
author_org [mlcube_author_org]:
```
 
## Running MLCubes
The MLCube template project that has just been created provides an example implementation of a task that MLCube runners
can run. Assuming your MLCube name is `my_mlcube`, configure and run it using docker container runtime:
```
$ cd ./my_mlcube && ls ./workspace
parameters_file.yaml

$ mlcube configure --mlcube=. --platform=docker -Prunner.build_strategy=auto
$ mlcube run --mlcube=. --platform=docker --task=my_mlcube

$ ls ./workspace
output.txt           parameters_file.yaml

$ cat ./workspace/output.txt 
Running my_mlcube task with parameters '{'abc': 123}'.
```

## Distributing ML workloads as MLCubes. 
Start updating your MLCube by studying the `mlcube.yaml` file in the root directory of your MLCube. Every configuration
file provides a description and what needs to be updated next. Mode details are available at 
[MLCube wiki](https://mlcommons.github.io/mlcube/).

## Contribution guidelines
Thank you for your interest in contributing to MLCube! The best way to get started is to make sure you signed the 
Google CLA (https://cla.developers.google.com/clas), soon to be replaced by a MLCommons/MLCube CLA.

- If you are making a trivial change (such as a typo fix), please feel free create a PR once you have signed the CLA.
- For larger changes, please join our mailing list https://groups.google.com/g/mlcommons-best-practices and/or 
  slack http://mlperf.slack.com/ to discuss.

## Resources
- [MLCommons](https://mlcommons.org)
- [MLCube](https://github.com/mlcommons/mlcube)
- [MLCube Wiki](https://mlcommons.github.io/mlcube)
- [MLCube Examples](https://github.com/mlcommons/mlcube_examples)

## License
[Apache License 2.0](./LICENSE)
