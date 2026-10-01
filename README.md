# Week 5 Assignment: Password Generator & Your Own Module

This assignment practices Python modules, built-in modules, functions, default values, and creating and importing a custom module.

## Files

- **`password_generator.py`** — Uses the `random` and `string` modules to generate random passwords with default and custom lengths.
- <img width="1109" height="336" alt="mart py1" src="https://github.com/user-attachments/assets/a3a239ab-0aa9-4870-b736-e047a92101e5" />

- **`helpers.py`** — Contains reusable `tables_needed()` and `welcome()` functions and demonstrates `if __name__ == "__main__"`.
- <img width="1101" height="80" alt="mart py2" src="https://github.com/user-attachments/assets/2ad7fdbf-20ff-4e69-bca7-946a99b0f5d0" />

- **`main.py`** — Imports the custom `helpers` module and uses its functions.
- <img width="1112" height="112" alt="mart py3" src="https://github.com/user-attachments/assets/6e185e63-2dd8-4a31-9e43-08da047a3092" />


## Reflection

The hardest part was understanding how `if __name__ == "__main__":` works. It allows the test code in `helpers.py` to run when the file is executed directly, but prevents that code from running when `helpers` is imported by `main.py`.
