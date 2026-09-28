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

## Bounties

Merged code, documentation and tests in iceroot-network repositories can earn ROOT, IceRoot's token, from the Developer ecosystem pool. Maintainers review each contribution on GitHub. A bot tracks each item and keeps the public bounty record; it never rates work and never pays. The [programs repository](https://github.com/iceroot-network/programs) holds the program list, the bounty record, the monthly statements and the account bindings.

| Contribution | Provisional reward (ROOT) |
| --- | ---: |
| Tier 1: major feature, subsystem, tool or test suite, or a large refactor that keeps every test passing | 2,500 |
| Tier 2: bug fix with a test, measured performance improvement, or new guide or reference page | 1,000 |
| Tier 3: small fix with a test, added tests for existing code, or substantive documentation correction | 250 |
| Posted bounty: a task whose amount a maintainer states before work starts | Up to 12,500 |

The provisional yearly cap is 375,000 ROOT from the Developer ecosystem pool. The final table will be set once ROOT has a value on chain. The table is reviewed each quarter; the table in force when a pull request arrives sets its reward, and a review never reduces a reward already earned. Typos, links, formatting, dependency bumps and generated files receive credit only.

### Who can earn

Anyone with a GitHub account, except the IceRoot team. Validators and related parties can earn under the same rules and rates; payouts to related parties are marked, with the relationship stated. A contribution that was paid a bounty carries a "bounty paid" tag on the validator portal, with a link to its record.

### How rewards are awarded

Open a pull request against the repository's `dev` branch as described above. When it is merged, a maintainer rates it and explains the rating, and the reward is recorded against your numeric GitHub account ID. You may ask for one second review. A contribution split across several pull requests is rated as one.

A reproducible bug with no security effect, reported in an issue with steps to reproduce and confirmed by a maintainer, earns 250 ROOT from the Security and bug bounty pool. Report anything with a possible security effect privately, as the [security policy](SECURITY.md) describes: a private report first is a condition for any bounty for a vulnerability.

### Before mainnet

ROOT does not exist yet, so rewards are earned and recorded now and paid in the mainnet genesis:

1. Each reward is recorded against your numeric GitHub account ID, which stays the same if you rename the account.
2. Once testnet accounts are available, link your GitHub account to one testnet account: from that GitHub account, post a message signed with the testnet account's key. A new or changed link takes effect after 7 days.
3. From the linked testnet account, bind your mainnet address with the same memo transaction that the testnet participation pool uses.
4. Bound rewards are credited in the mainnet genesis as allocations from the relevant pool, usable from the first block. Security rewards follow the advisory timing in the security policy.

Step-by-step instructions and deadlines are not published yet. What happens to a reward that is still unbound at the binding deadline has not been decided.

### After mainnet

Once a month the team pays the approved rewards by hand from each pool's 2-of-3 multisig account, in a batch the bot prepares. An entry must be on the program list before it is paid, and the payment must match it; there is no waiting period after listing. Each payout carries the memo `iceroot:pay:v1 <entry id> <fingerprint>`, where the fingerprint is the 64-character fingerprint of the entry's payment details, and appears on the explorer's Genesis distribution page.
