# Introduction

This is the documentation for the Coding Test.

During the last week I took it upon myself to learn web development,
specifically, using Test Driven Methodology using resources available to me: the book "Test Driven Development with Python" by H. J. W. Percival and the official Django Tutorials (https://docs.djangoproject.com/en/1.11/).

Attached is the skeleton of a full implementation for the LIMS website using the language I know best of the ones listed: Python's Django framework.

Two systems design diagrams are included:

* Class Diagram

  This diagram will serve as the basis for the TDD using Django.

* Entity Relationship Diagram

  This is the proposed design of the back-end database of the system.

# Website Development

## Introduction

The Production Software Team write bespoke Laboratory Information Management
Systems (LIMS) that are used in the high-throughput sequencing pipelines at the
Sanger Institute.

### Functionality Specification

Full description of the functionality specification can be found in the file
![CodingTestV3.pdf](/docs/CodingTestV3.pdf) inside the docs directory.

## Development Cycle

Uses TDD approach.

## Requirements

* Python >= 3.6
* Django <= 1.11

## Tools

* Geckodriver
* Selenium
* Git

## Run Tests

1. start server

```
python manage.py runserver
```

2. run functional tests

```
python functional_tests.py
```

## To-Do

A functional LIMS.
