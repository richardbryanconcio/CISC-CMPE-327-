# CI pipeline

[![Pytest-All](https://github.com/richardbryanconcio/CISC-CMPE-327-/actions/workflows/pytest.yml/badge.svg)](https://github.com/richardbryanconcio/CISC-CMPE-327-/actions/workflows/pytest.yml)
[![Python PEP8](https://github.com/richardbryanconcio/CISC-CMPE-327-/actions/workflows/PythonPEP8.yml/badge.svg)](https://github.com/richardbryanconcio/CISC-CMPE-327-/actions/workflows/PythonPEP8.yml)

A2 (backend dev) Folder structure:

```
├── LICENSE
├── README.md
├── .github
│   └── workflows
│       ├── pytest.yml       ======> CI settings for running test automatically (trigger test for commits/pull-requests)
│       └── style_check.yml  ======> CI settings for checking PEP8 automatically (trigger test for commits/pull-requests)
├── qbay                 ======> Application source code
│   ├── __init__.py      ======> Required for a python module (can be empty)
│   ├── __main__.py      ======> Program entry point
│   └── models.py        ======> Data models
├── qbay_test            ======> Testing code
│   ├── __init__.py      ======> Required for a python module (can be empty)
│   ├── conftest.py      ======> Code to run before/after all the testing
│   └── test_models.py   ======> Testing code for models.py
└── requirements.txt     ======> Dependencies
```

To run the application module (make sure you have a python environment of 3.5+)

```
$ pip install -r requirements.txt
$ python -m qbay
```

To run testing:

```
# style check (only show errors)
flake8 --select=E .  

# run all testing code 
pytest -s qbay_test

```


