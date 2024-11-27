# Usage

## Add new code test

To add a new test for any new functionality you have added or you plan to add you should add a test.
The test is imply added to the tests/
directory.

See our examples ....

## Debugging

### Local Debugging

You can run your automation suite locally by typing the following command in your console. This is useful for verifying the outcome of your automation pipeline before pushing your code:

```bash
tox
```

Running this command will generate a comprehensive report, which may require some effort to debug.

### Remote Debugging on GitHub

For remote debugging, you can monitor the status of your automation jobs in two ways:

1. Create a pull request and view the CI status integration there.
2. Visit the [Actions tab of your repository](https://github.com/rl-institut/super-repo/actions) to see all available job executions.

These options allow you to closely monitor the progress and outcomes of your CI workflow, ensuring the reliability and quality of your codebase.
