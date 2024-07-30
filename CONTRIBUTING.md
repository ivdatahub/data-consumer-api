# Contributing to this project

Firstly, thank you very much for your interest in contributing to this project.

This document provides guidelines to help ensure the contribution process is smooth and efficient for everyone involved.

## How to Contribute

### 1. Fork the Repository

1. Go to repository page
2. Click the "Fork" button in the top right corner to create a copy of the repository on your GitHub.

### 2. Clone the Repository

Clone the forked repository to your local machine using the command:

### 3. Create a Branch

Create a branch for your feature or bug fix:

```sh
git checkout -b feature/branchname
```

```sh
git checkout -b fix/branchname
```

## 3.1 Code Standards

- Use Python 3.9.6 or later.
- Follow PEP 8 for code style.
- Include unit tests for any new functionality or bug fixes.
- Make sure all existing and new tests pass before submitting a Pull Request.

### 4. Make Changes

Make the desired changes to the code. Be sure to follow code style and documentation guidelines.

## 4.1 Tests

- Use the `pytest` library for testing.
- Write your tests for each new package or component

### 5. Commit your Changes

Commit your changes with a clear and descriptive message:
```sh
git add .
```
```sh
git commit -m "Detailed description of changes"
```

### 6. Push to Remote Repository

Push your changes to the remote repository:

```sh
git push origin branchname
```

### 7. Create a Pull Request

1. Go to the original repository page on GitHub.
2. Click on "Pull Requests" and then on "New Pull Request".
3. Compare your branch with the `main` branch of the original repository and click "Create Pull Request".
4. Fill in the title and description of the Pull Request with clear information about the changes made.


## Reporting Bugs or improvement suggestions

If you find a bug, please open an issue and provide as much information as possible, including:

- Detailed description of the problem.
- Steps to reproduce the issue.
- Python and package version.
- Relevant error messages.

## Thanks

Thanks for considering contributing to this project. Every contribution is valuable and helps to improve the project.
