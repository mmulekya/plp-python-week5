# Week 5 Assignment: Password Generator & Your Own Module

This assignment practices Python modules, built-in modules, functions, default values, and creating and importing a custom module.

## Files

- **`password_generator.py`** — Uses the `random` and `string` modules to generate random passwords with default and custom lengths.
- **`helpers.py`** — Contains reusable `tables_needed()` and `welcome()` functions and demonstrates `if __name__ == "__main__"`.
- **`main.py`** — Imports the custom `helpers` module and uses its functions.

## Reflection

The hardest part was understanding how `if __name__ == "__main__":` works. It allows the test code in `helpers.py` to run when the file is executed directly, but prevents that code from running when `helpers` is imported by `main.py`.