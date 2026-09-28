# Security

This policy covers the repositories of the [iceroot-network](https://github.com/iceroot-network) organization and the software built from them.

## Report a vulnerability

Report vulnerabilities privately through [IceRoot's security reporting page](https://github.com/iceroot-network/.github/security/advisories/new), which uses GitHub private vulnerability reporting. Sign in to GitHub, fill in the form and submit it. Only you and the maintainers can see the report. The form accepts reports about any IceRoot repository, including one that is not public yet.

Include the affected repository, the version or commit, the potential impact, and a working reproduction on your own local network or private devnet: a test, a script or exact steps. Do not include private keys, recovery phrases, signing credentials, or personal information. Keep exploit details out of public issues and pull requests.

An email address for reports will be added here once its inbox is watched every working day. Until then, the GitHub form is the way to report.

For ordinary bugs with no security effect and for feature requests, use the affected repository's issue tracker. If you are unsure whether a bug has a security effect, report it privately first.

## Research rules and safe harbour

- Test with test accounts on your own local network or a private devnet, and test site code on a local copy.
- Do not test against mainnet, the public testnet, nodes run by other people, or live websites.
- Do not access, change or take other people's data, keys or funds. Do not use social engineering, physical attacks, or denial of service against shared services.
- Stop testing and report once you have a working reproduction.

Good-faith research that follows these rules is authorized, and the IceRoot team will not pursue legal action for it. Breaking these rules, or publishing details before the advisory, forfeits any reward.

## Response and disclosure

For every private vulnerability report, we will:

- acknowledge it within 3 working days;
- give a severity rating within 14 days of the report;
- send a progress update at least every 14 days until it is resolved.

Our fix targets are 30 days for Critical and High findings and 90 days for Medium and Low findings. These are targets, not promises. Maintainers explain each rating in writing, and you may ask for one second review.

Each fixed report gets a GitHub security advisory, published once the fix is live and no later than 90 days after the report. A consensus flaw is published only after its fix has passed its activation height; until then the fix ships as a security release with its activation height and no details. If that height cannot be reached within 90 days, we may extend the deadline once, by up to 30 days, and state the reason publicly, so the latest publication date is 120 days after the report.

Keep the details private until the advisory is published; after that you may publish your own write-up. You choose whether the advisory credits you by your GitHub name or not at all.

These promises cover privately reported vulnerabilities. Public disclosure of incidents on a live network is decided case by case.

## Bounties

Security reports and confirmed bug reports can earn ROOT from the Security and bug bounty pool. A private report first is a condition for any bounty for a vulnerability. The [programs repository](https://github.com/iceroot-network/programs) holds the program list, the bounty record, the monthly statements and the account bindings.

| Finding | Provisional reward (ROOT) |
| --- | ---: |
| Critical | 50,000 |
| High | 12,500 |
| Medium | 2,500 |
| Low | 500 |
| Confirmed bug with no security effect | 250 |

The provisional yearly cap for these bounties is 750,000 ROOT. The final table will be set once ROOT has a value on chain. The table is reviewed each quarter; the table in force when a report arrives sets its reward, and a review never reduces a reward already earned.

**Who can earn.** Anyone with a GitHub account, except the IceRoot team. Validators and related parties can earn under the same rules and rates; payouts to related parties are marked, with the relationship stated.

**Rules.**

- The first complete report with a working reproduction qualifies. Duplicates, and findings the team had already recorded, earn nothing.
- One root cause earns one reward, however many symptoms it has. A reporter who also writes the fix gets the security reward only, with no contribution reward on top.
- Reports without a working reproduction earn no reward. Repeated low-quality reports can lead to exclusion from the program.

**Scope.** Bounties cover the public iceroot-network repositories, both the default branch and the latest release. A repository joins when it becomes public; the websites and the validator portal join once their code is public, so that research can run on a local copy. These do not qualify:

- flaws in the `solar-core-ref` reference repository that do not also affect Heartwood;
- flaws in third-party libraries, unless exploitable through IceRoot's use of them (report those upstream first);
- volumetric denial of service, social engineering and physical attacks;
- attacks that need a stolen key, a compromised computer or a malicious browser extension;
- limits that the whitepaper states;
- scanner output and best-practice suggestions without a demonstrated effect;
- forks of IceRoot code run by others.

**Payment.** A security reward enters the public record, and becomes payable, only after its advisory is published. Rewards earned before mainnet are recorded against your numeric GitHub account ID and credited in the mainnet genesis once you bind an address; a security reward whose advisory is still unpublished at the genesis cut-off is paid in a monthly run after mainnet instead. See [how rewards are recorded, bound and paid](CONTRIBUTING.md#bounties).
