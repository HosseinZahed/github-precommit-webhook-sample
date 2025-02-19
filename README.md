### GitHub Pre-commit Webhooks Sample

### What are Pre-commit webhooks?
Pre-commit webhooks in GitHub are used to ensure code quality and consistency by running scripts before a commit is made. These hooks can perform various checks and validations, such as:

- **Preventing giant files from being committed**: Specify a maximum file size to prevent large files from being added to the repository5.
- **Checking for valid Python syntax**: Ensure that Python files parse correctly5.
- **Checking for merge conflicts**: Detect files that contain merge conflict strings5.
- **Verifying JSON and XML syntax**: Load and verify the syntax of JSON and XML files5.

### Installing Pre-Commit Hooks in Your GitHub Repository

#### Introduction
This guide provides step-by-step instructions for installing pre-commit hooks in your GitHub repository. Pre-commit hooks help ensure code quality by running checks before commits are made.

#### Prerequisites
- Python 3.9 or higher
- Git installed on your machine

#### Installation
1. **Install python libraries**:
<code>pip install -r requirements.txt</code>

2. **Add a pre-commit configuration file**:
   Create a file named .pre-commit-config.yaml in the root of your repository with the following content:

   ```
   repos:
   - repo: https://github.com/pre-commit/pre-commit-hooks
     rev: v5.0.0
     hooks:
      - id: check-merge-conflict
      - id: trailing-whitespace
      - id: end-of-file-fixer

3. **Install pre-commit**:
<code>pre-commit install</code>

#### Configuration
You can customize the hooks by modifying the .pre-commit-config.yaml file. Refer to the An external link was removed to protect your privacy. for more options.

#### Usage
Run hooks on all files:
<code>pre-commit run --all-files</code>

Run hooks on staged files:
<code>pre-commit run</code>

Uninstall pre-commit:
<code>pre-commit uninstall</code>

By following these steps, you can ensure that your code meets quality standards before committing changes to your repository.

References:
- https://pre-commit.com/
- https://github.com/pre-commit/pre-commit-hooks