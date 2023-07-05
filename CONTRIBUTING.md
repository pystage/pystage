# Contributing to PyStage


## Making a Pull Request

- You can read here about how to usually [contribute to Open Source Projects](https://docs.github.com/en/get-started/quickstart/contributing-to-projects)
- We follow the [GitHub Flow](https://docs.github.com/en/get-started/quickstart/github-flow)

### Outline of the process
- Make sure you have checked out the development branch and that you are on the most recent commit (do a `git pull` first).
- Then create a branch for your new feature or bug fix. If you work on several features, create a branch for each feature, all branching from development.
- Name your feature branch as meaningful as possible.
- While you work on your feature (until it finally gets merged into the official development branch), always keep your [feature branch in sync with the development branch](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/keeping-your-pull-request-in-sync-with-the-base-branch)

### How to get your own working copy
- Fork the pystage repository to your own account
- Clone a working copy from your fork, as usual
- Add pystage as additional remote, usually called upstream: `git remote add upstream https://github.com/pystage/pystage.git`
- Switch to the development branch: `git checkout development`
- Create your new feature branch: `git checkout -b my-new-feature`
- Do your work...
- Push the feature branch to your forked repository
- Create a pull request via the GitHub website.
- If the development branch changes in upstream, fetch all changes from upstream and merge them into your feature branch:
    - `git fetch upstream`
    - `git merge upstream/development`
