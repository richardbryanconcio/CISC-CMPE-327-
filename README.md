# Pocket Rentals • A website to manage and create listings (via C2C) for available apartments/housing.
![Pocket Rentals Logo](https://github.com/richardbryanconcio/Pocket-Rentals/assets/101062026/4935be7c-e495-4530-a179-a568a45e32a5)
(Logo created by Richard Bryan Concio)
> Richard Bryan Concio • Anton Gudonis • Anjali Patel • Isaac Schneider

- Consists of a sign in page with email and passwords to an existing account.
- Users are able to create and book listings for housing/apartment rentals through an online application.
- A verified guest can review listings made by other users.
- User payment is directly through their balance on the online application.
- A user can add money to their account through online banking (transfer directly from their own banking account).
- The program is built using Qt Studio and C++.

🚀 This project incorporates the SCRUM method with daily scrum meetings and updates and sprints.

## Project Division Leads
Backend Development Lead - Anton Gudonis, Richard Bryan Concio
Frontend Development Lead - Richard Bryan Concio, Anjali Patel

| Lead | Feature |
| ----------- | ----------- |
| Richard Bryan Concio | Login Function, Integration Testing, Docker, Security/Deployment |
| Anton Gudonis | SCRUM Master | Create Listings, Integration Testing, Security/Deployment |
| Anjali Patel | Register Function, Integration Testing, Security/Deployment |
| Isaac Schneider | Update Listings, Integration Testing |

# 🍱 CI pipeline

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



