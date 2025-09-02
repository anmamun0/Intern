## 1️⃣ Virtual Environment Setup

A virtual environment is a self-contained Python environment for your project. It helps avoid conflicts between dependencies of different projects.


```
# Step 1: Navigate to your project folder
cd my_project_folder

# Step 2: Create a virtual environment
# For Python 3.x
python -m venv venv

# Step 3: Activate the virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Step 4: Install dependencies
pip install django  # example

```
 
Tip: Always have a requirements.txt to save dependencies:
```
pip freeze > requirements.txt
```

And install later via:
```
pip install -r requirements.txt
```

Here’s a typical structure for Windows:
```
venv/
├── Include/           # C headers for compiling Python packages
├── Lib/               # Installed Python packages live here
│   └── site-packages/ # Third-party packages installed via pip
├── Scripts/           # Activation scripts & executables
│   ├── activate       # Bash/Zsh activation script
│   ├── activate.bat   # CMD activation script
│   ├── Activate.ps1   # PowerShell activation script
│   ├── python.exe     # Python interpreter
│   └── pip.exe        # Pip executable
├── pyvenv.cfg         # Configuration file for the virtual environment
```

For macOS/Linux, the main difference is the Scripts/ folder is called bin/:
```
venv/
├── bin/               # Activation scripts & executables
│   ├── activate       # Bash/Zsh activation script
│   ├── activate.csh
│   ├── activate.fish
│   ├── python         # Python interpreter
│   └── pip            # Pip executable
├── include/           # C headers
├── lib/               # Installed Python packages
│   └── pythonX.X/
│       └── site-packages/
└── pyvenv.cfg         # Configuration file
```

--- 
<br>
<br>


## 2️⃣ Commenting

Comments make your code readable for you and others. Follow these rules:
Types of comments:

Inline comments:
```
x = x + 1  # Increment x by 1
```

Block comments:
```
# This function calculates
# the factorial of a number
def factorial(n):
    ...

```
Docstrings (for functions, classes, modules):
```
def add(a, b):
    """
    Add two numbers and return the result.
    Args:
        a (int): First number
        b (int): Second number
    Returns:
        int: Sum of a and b
    """
    return a + b
```
## 3️⃣ Naming Conventions

Python follows PEP8 naming rules: Coding Standards (PEP8)

- `Indentation:` Use 4 spaces per indentation level, never tabs.
- `Maximum Line Length:` Limit code lines to 79 characters, comments/docstrings to 72.
- `Blank Lines:` Use 2 blank lines before top-level functions/classes, 1 inside classes.
- `Imports:` Standard library → Third-party → Local application imports. one per line.
- `Whitespace:` Avoid extra spaces around operators, brackets, commas, and colons.
- `Naming Conventions:` Use snake_case for variables/functions, PascalCase for classes, UPPER_CASE for constants.
- `Programming Recommendations:` Avoid multiple statements on one line, use is/is not for None, use in for membership.
- `Comments:` Use inline comments sparingly, block comments above code, and docstrings for modules, classes, and functions.
- `String Quotes:` Be consistent with single ' or double " quotes.
- `Other Guidelines:` Avoid trailing spaces, maintain readable logical structure, use UTF-8 encoding, and virtual environments for dependencies.


Perfect! Here’s a full, easy-to-follow summary of all main PEP8 rules with examples. I’ve organized them by category so you can use it as a coding checklist.

### 1️⃣ Indentation

Use 4 spaces per indentation level. Never use tabs.
```
# Good
def my_function():
    if True:
        print("Hello")

# Bad
def my_function():
	if True:
		print("Hello")
```

### 2️⃣ Maximum Line Length

Limit lines to 79 characters for code, 72 characters for comments/docstrings.
```
# Good
total = (a + b + c + d +
         e + f + g + h)

# Bad
total = a + b + c + d + e + f + g + h + i + j + k + l + m
```

### 3️⃣ Blank Lines

Top-level functions/classes: 2 blank lines before.

Methods inside a class: 1 blank line.
```
class MyClass:
    def method_one(self):
        pass

    def method_two(self):
        pass
```

4️⃣ Imports

Order of imports: Standard library → Third-party → Local application imports.

One import per line.
```
# Good
import os
import sys

import requests

from myapp import utils

# Bad
import sys, os, requests
```

5️⃣ Whitespace in Expressions

Avoid extra spaces in these situations:
```
# Good
x = 1
y = (2 + 3) * 4

# Bad
x =  1
y = ( 2 + 3 ) * 4
```

After commas, colons, semicolons: Always one space:
```
my_list = [1, 2, 3]
```
6️⃣ Naming Conventions

<h6>
  
| Item          | Convention  | Example          |
| ------------- | ----------- | ---------------- |
| Variables     | snake\_case | user\_name       |
| Functions     | snake\_case | calculate\_sum() |
| Classes       | PascalCase  | BankAccount      |
| Constants     | UPPER\_CASE | PI = 3.14        |
| Modules/files | snake\_case | utils.py         |
| Packages      | lowercase   | myapp            |
</h6>

### 7️⃣ Programming Recommendations

Avoid multiple statements on one line.
```
# Good
if x == 4:
    print(x)

# Bad
if x == 4: print(x)
```

Use is / is not for comparisons to None.
```
if variable is None:
    pass
```

Use in for checking membership instead of multiple ors.
```
if x in [1, 2, 3]:
    pass
```

8️⃣ Comments

Use inline comments sparingly: after code, separated by two spaces.
```
x = x + 1  # Increment x

```
Use block comments for descriptions above code blocks:
```
# This function calculates factorial
def factorial(n):
    ...
```

Use docstrings for modules, classes, and functions:
```
def add(a, b):
    """
    Add two numbers and return the result.
    Args:
        a (int)
        b (int)
    Returns:
        int
    """
    return a + b
```
### 9️⃣ String Quotes

Pick single ' or double " consistently in a project.
```
# Good
name = "Alice"
greeting = 'Hello'

# Bad
name = "Alice'
```
## 🔟 Other Guidelines

Avoid trailing spaces.
- Use consistent encoding (UTF-8).
- Keep logical structure of the code readable.
- Use virtual environments for dependencies.


### 💡 Tools to enforce PEP8:

#### flake8 → pip install flake8 → flake8 yourfile.py
#### pylint → pip install pylint → pylint yourfile.py
#### Most IDEs like VS Code, PyCharm highlight PEP8 violations automatically.


You can check automatically with flake8 or pylint:
```
pip install flake8
flake8 myfile.py
```
 

---
<br>
<br>

## 5️⃣ File / Project Design

A clean project structure is key to maintainability.
```
Example: Django Project Structure
myproject/
│
├── manage.py
├── requirements.txt
├── venv/
│
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── apps/
│   ├── users/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── serializers.py
│   └── blog/
│       ├── models.py
│       ├── views.py
│       ├── urls.py
│       └── serializers.py
│
└── static/
    └── ...
```

Tips:
- Modular apps: Each feature in its own app (users, blog, payments…)
- Separation of concerns: Models → Data, Views → Logic, Templates → UI
- Naming files: Clear and short (e.g., serializers.py, views.py, forms.py)
- Keep reusable code in utils.py or helpers.py


## 4️⃣ File Naming Guidelines
 
`Project Folder:` lowercase, no spaces, use underscores if needed → `myproject/`, `blog_project/`, `vts_backend/` <br>
`App Folder:` lowercase, singular if possible, short and descriptive → `users/`, `blog/`, `products/`, `orders/` <br>
`Python Files:` snake_case (lowercase + underscores) → `user_profile.py`, `utils.py`, `models.py`, `views.py`, `urls.py`, `forms.py`, `serializers.py`, `permissions.py`, `signals.py`, `tests.py` <br>
`Templates:` lowercase, underscores, descriptive → `login.html`, `register.html`, `profile_detail.html` (folder: `app_name/templates/app_name/`) <br>
`Classes:` PascalCase → `UserProfile`, `BlogPost` <br>
`View Names:` function-based → snake_case (`user_login`), class-based → PascalCase + `View` (`UserLoginView`) <br>
`URL Patterns:` lowercase, hyphens, descriptive → `'login/'`, `'profile-detail/'` <br>
`Forms / Serializers:` PascalCase → `UserRegisterForm`, `UserSerializer` <br>
`Constants:` UPPER_CASE → `MAX_USERS = 100` <br>
`Tests:` file names start with `test_`, function names start with `test_` → `test_views.py`, `test_models.py`


## Code Style Checkers in Python

```
pip install pycodestyle
pip install pylint
pip install flake8

```

### Pylint
`pip install pylint`
Pylint is a Python code linter that checks your code for errors, coding standards (PEP8), code smells, and refactoring suggestions. It also gives a score (0–10) for your code quality.

Features:
- Detects syntax errors and undefined variables
- Enforces PEP8 naming and style conventions
- Suggests improvements for maintainability
- Provides code metrics
 

How to use:
```
# Check a Python file
pylint your_file.py

# Example: check all Python files in a folder
pylint myproject/
```


###  Flake8
`pip install flake8`
Flake8 is another Python linter focusing on PEP8 compliance, linting errors, and basic code complexity checks.

Features:
- Checks PEP8 style violations
- Detects syntax errors and undefined names
- Optionally checks code complexity (mccabe)
- Can integrate with editors like VS Code for real-time feedback


How to use:
```
# Check a Python file
flake8 your_file.py

# Example: check all Python files in a project folder
flake8 myproject/
```






























