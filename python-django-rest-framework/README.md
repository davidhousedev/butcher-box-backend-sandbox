# Python Django Rest Framework Implementation

**TL;DR**

```
make
# in a new terminal
open localhost:5123
```

## Pros

- API and Database Schema derived in the same place, from models
- Database migration creator comes out-of-the-box with Django
- Increased developer productivity with generated API plumbing
- Well-documented tool reduces documentation burden
- Industry standard tooling out-of-the-box for, e.g.
  [OAuth2 Authentication and Authorization](https://www.django-rest-framework.org/api-guide/authentication/#django-oauth-toolkit)
- Larger developer recruitment pool through tapping into large
  Python developer base in Boston
- Increased developer motivation through professional development
  with valuable skillset

## Cons

- Limited Python knowledge here at ButcherBox

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

# Developer Tips

## VS Code

### Local Interpreter

To enable VS Code Intellisense in this project, you've got a few
tools to install. If you'd like to skip this step and use the advanced
VS Code Remote Development feature, skip to the next section.

1. pyenv: Use this to install a non-system Python interpreter

```
# if you prefer to not pipe to bash, cf: https://github.com/pyenv/pyenv
curl https://pyenv.run | bash
exec $SHELL
pyenv install 3.8.1  # install a local Python interpreter
pyenv global 3.8.1  # set the interpreter as your global default

# Now do a quick sanity check
pip --version && python --version

# If these versions align, you're good to go!
```

2. Install project package requirements on your host interpreter. This is necessary to enable VS Code Intellisense.

```
pip install -r requirements-vscode.txt
```

1. Configure VS Code to use your interpreter
   1. In VS Code, press `cmd-shift-P`
   2. Type `python select interpreter`
   3. In the dropdown, select the `3.8.1` version with `pyenv` in the name

### Remote Interpreter (Alternative)

**For those of you who are adventurous:** You can set up VS Code as a
remote interpreter running inside the container. This allows you to
avoid installing a local python interpreter altogether!
cf: https://code.visualstudio.com/docs/remote/containers

### Essential Settings:

**Important:** Make sure that you have

```JSON
{
  "editor.formatOnSave": true,
  "files.autoSave": "afterDelay",
  "files.trimTrailingWhitespace": true,
  "python.formatting.provider": "black",
  "python.linting.mypyEnabled": true,
  "python.linting.pylintEnabled": true,
  "python.testing.pytestEnabled": true,
  "[python]": {
    "editor.insertSpaces": true,
    "editor.tabSize": 4,
    "editor.defaultFormatter": "ms-python.python",
    "editor.rulers": [88],
  }
}
```

## Python Language Tips

- Importing \*
  - `__init__.py` files should always be blank, until you're very comfortable
    with how Python imports work. Then, they should ~only include `import`
    statements.
