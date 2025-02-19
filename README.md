# neverstopthemadness

# Lukuvinkki
Lukuvinkki is an app for saving books and videos you might want to refer to later on.

# Motivation
This app is a course work for University of Helsinki course on software production.

## Progress
Development progress can be followed at [Product Backlog](https://docs.google.com/spreadsheets/d/1MJSoLpiMTgNUXJ85q7sGDer07GEPHYba24U61Qp2FtE/edit?usp=sharing)

App can be tested at [lukuvinkkisovellus.herokuapp.com](https://lukuvinkkisovellus.herokuapp.com/)

Test coverage report can be found [here](https://codecov.io/gh/Aleksipa/Lukuvinkkisovellus).

Project report can be found [here](https://docs.google.com/document/d/1gl12Ryy5ZCvcsUaMExCYpzN_GXq_JrAC1F4LCsTcJP4/edit?usp=sharing).

## Developing

Definition of Done:
- Code has been peer-reviewed
- Code has unit testing
- Code has user level testing if applicable
- Code passes tests
- Code has been integrated to app, and app still passes all tests
- Code has been pushed to Heroku and is part of the accessible app

The project uses Pipenv for dependency management. Make sure it is installed.
Development dependencies can be installed by running
```
pipenv install --dev
```
A shell to the created virtualenv can be started by running
```
pipenv shell
```
All following commands must be run inside the virtualenv.

### Unit tests
![Python package](https://github.com/Aleksipa/Lukuvinkkisovellus/workflows/Python%20package/badge.svg)

Tests can be run with the script `run-tests.sh`. To also report test coverage
pass `--cov=application` argument to `run-tests.sh`.

### Feature tests

Feature tests can be run with the script `run-feature-tests.sh`.

<!---
# Build status
Build status of continus integration i.e. travis, appveyor etc. Ex. -
Build Status Windows Build Status
# Code style
If you're using any code style like xo, standard etc. That will help others while contributing to your project. Ex. -
js-standard-style
# Screenshots
Include logo/demo screenshot etc.
# Tech/framework used
Ex. -
Built with Electron
# Features
What makes your project stand out?
# Code Example
Show what the library does as concisely as possible, developers should be able to figure out how your project solves their problem by looking at the code example. Make sure the API you are showing off is obvious, and that your code is short and concise.
# Installation
Provide step by step series of examples and explanations about how to get a development env running.
# API Reference
Depending on the size of the project, if it is small and simple enough the reference docs can be added to the README. For medium size to larger projects it is important to at least provide a link to where the API reference docs live.
# Tests
Describe and show how to run the tests with code examples.
# How to use?
If people like your project they’ll want to learn how they can use it. To do so include step by step guide to use your project.
# Contribute
Let people know how they can contribute into your project. A contributing guideline will be a big plus.
# Credits
Give proper credits. This could be a link to any repo which inspired you to build this project, any blogposts or links to people who contrbuted in this project.
# Anything else that seems useful

# License
A short snippet describing the license (MIT, Apache etc)

--->
