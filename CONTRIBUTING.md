# Contributing to IceRoot

Choose a project from the [documentation](https://docs.iceroot.com). Its README describes the prerequisites, local build, and checks.

## Branches

- **`prod` is the default production branch.** Changes enter it only through a pull request from this repository's `dev` branch.
- **`dev` is the development branch.** Make changes and run builds and tests locally here. Fork contributions should target `dev`.
- Production CI runs after a `dev → prod` pull request is merged. Development pushes and open pull requests do not trigger build or signing jobs.

```sh
git fetch origin
git switch dev
git pull --ff-only origin dev
```

Keep a change focused. Include the reason for the change, how to exercise it, and the checks you ran. For interface changes, include screenshots at the affected screen sizes and use the [IceRoot design system](https://github.com/iceroot-network/mediakit).

## Promote a release

1. Finish and test the change on `dev`.
2. Open a pull request with base `prod` and head `dev` in the same repository.
3. Review the diff and merge the pull request. Do not push directly to `prod`.
4. Confirm the production checks and deployment or release jobs complete.
5. Merge `origin/prod` back into `dev` to retain the promotion history.

Keep `dev` after merging; it is a permanent branch. Never force-push production history. Signing credentials belong in GitHub secrets, never in source files or pull request comments.

## Documentation and assets

Use **validator** for a network validator. Write product documentation in clear, concrete language. Preserve license notices and compatibility identifiers when using third-party code.

Use the current logo and shared tokens from the [mediakit](https://github.com/iceroot-network/mediakit). Propose shared visual changes there before updating applications.

For vulnerabilities, follow the [security policy](SECURITY.md).
