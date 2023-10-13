# oblig_3_git_n_int


    This project is configured with automated tests using GitHub Actions. GitHub Actions allows you to run tests automatically every time you push new changes to your GitHub repository.


    GitHub Actions Configuration (.github/workflows/main.yml):

    /project-root
    │
    └── .github
        └── workflows
            └── main.yml

# Created Workflow File:

    - Created `main.yml` inside `.github/workflows` to define GitHub Actions workflow.

    # Defined Workflow:

        - Named workflow: "Run Tests".
        - Configured to trigger on every push event (`on: [push]`).


# Configured Workflow Steps:

    - Checked out code using `actions/checkout@v2`.
    - Set up Python 3.8 using `actions/setup-python@v2`.
    - Installed dependencies from `requirements.txt` using `pip install -r requirements.txt`.
    - Ran tests with `pytest` command.

    #Workflow Execution:

    - Workflow automatically runs on every push, handling code checkout, environment setup, dependency installation, and test execution.

    #Monitoring Workflow:

    - Workflow execution monitored in the "Actions" tab of the repository.
    - Detailed logs available for each run, verifying workflow steps and test results.

# Verification:

    - Changes pushed to repository to verify automatic workflow triggering.
    - Checked "Actions" tab, reviewed logs, and ensured successful test execution.



