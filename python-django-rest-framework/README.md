# Python Django Rest Framework Implementation

**TL;DR**
```
make
# in a new terminal
open localhost:5123
```

## Pros
* API and Database Schema derived in the same place, from models
* Database migration creator comes out-of-the-box with Django
* Increased developer productivity with generated API plumbing
* Well-documented tool reduces documentation burden
* Industry standard tooling out-of-the-box for, e.g.
[OAuth2 Authentication and Authorization](https://www.django-rest-framework.org/api-guide/authentication/#django-oauth-toolkit)
* Larger developer recruitment pool through tapping into large 
Python developer base in Boston
* Increased developer motivation through professional development
with valueable skillset

## Cons
* Limited Python knowledge here at ButcherBox

This implementation leverages the widely-used
[Django Rest Framework](https://www.django-rest-framework.org/)
to generate API plumbing derived from database models.

Django Rest Framework allows you to take declarative models, 
defined using the Django ORM, and builds an API for interfacing
with those models. Verbs like `PATCH`, `PUT`, and `DELETE` are
included in the framework, which improves site reliability and
decreases unit testing burden.

Additionally, DRF ships with a browsable API to improve API
discoverability for new developers, and reduce documentation burden.

In the effort to centralize ButcherBox backend services around APIs,
it would be wise to leverage widely-used frameworks, built to
simplify API development.
