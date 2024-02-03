# Video-Plagiarism-Detection library Governance

This document defines project governance for the Video-Plagiarism-Detection library.

## Project Roles

### Maintainers

Aside me, there are no maintainers yet. However, for future purposes;
* The maintainers will be responsible for the overall development of the whole Video-Plagiarism-Detection library and all its components.
* The maintainers will be identified in the [`MAINTAINERS`][MAINTAINERS] file.

#### Changes in Maintainership

New maintainers will be proposed by an existing maintainer and are elected by a ⅔ majority maintainers vote.
Maintainers will be removed by a ⅔ majority maintainers vote.

#### GitHub Project Administration

Maintainers will be added to the collaborators list of the Video-Plagiarism-Detection repository with "Write" access.
After 6 months a maintainer will be given "Admin" access to the Video-Plagiarism-Detection repository.

### Component owners

The component owners will be responsible for development of a specific subproject or component within Video-Plagiarism-Detection repository.
Such components might be represented by a separate directory within the CMD-Executor repository as a subdirectory in a GitHub repository (e.g. `./documentation/` in `Video-Plagiarism-Detection`).
The components will be identified in the [`COMPONENT-OWNERS`][COMPONENT-OWNERS] file in this repository which also includes the component for which they are responsible.

By definition, every maintainer is also an owner for all components and does not have to be mentioned in the `OWNERS` list.

#### Changes in component ownership

New component owners can be proposed by any maintainer and are elected by a ⅔ majority maintainers vote.
Component owners can be removed by a ⅔ majority maintainers vote.

#### GitHub Project Administration

Owners of components which have their own GitHub repository will get "Write" rights for given GitHub repository and will be able to merge approved PRs.
Owners will not get "Admin" rights on any Video-Plagiarism-Detection GitHub repositories.

## Voting

The Video-Plagiarism-Detection project will employ voting to ensure no single member can dominate the project.

For formal votes, a specific statement of what is being voted on should be added to the relevant GitHub issue or PR.
Voters will indicate their yes/no vote on that issue or PR, and after a suitable period of time, the votes will be tallied and the outcome noted.

### Approving PRs

PRs may be merged after receiving at least two positive maintainer votes.
Voting for PRs can be done using a comment in the PR or by approving (or requesting changes) the PR.
If the PR author is a maintainer, this counts as a vote.

PRs which affect only a single component can be approved by at least one positive maintainer vote and one positive vote from an owner of given component.
If the PR author is a maintainer or an owner of given component, this counts as a vote.

### Proposals

Proposals can be opened against the [repository issues][issues].
Proposals should cover any changes to the Video-Plagiarism-Detection project which might significantly impact its users or the project direction.

Voting about proposals is using +1, 0, -1 votes and their fractions, where:
* +1 means "yes"
* -1 means "no"
* The numbers between +1 and -1 indicate how strongly you feel about the proposal

_(Inspired by [Apache Software Foundation voting](https://www.apache.org/foundation/voting.html#expressing-votes-1-0-1-and-fractions))_

Votes from maintainers are binding and count towards the approval of the proposal.
Non-maintainers are allowed and encouraged to vote as well.
But their votes are non-binding and do not count towards approval of the proposal.

+1 votes can be expressed by approving the proposal PR or in the comments.
Other votes should be expressed in the comments.
For example "+1 (binding)", or for a non-maintainer "+1 (non-binding)".

Proposals are approved when they receive at least three +1 binding votes and no -1 binding votes.
The proposal PR should be opened for at least 3 days to give everyone enough time to vote.

### Changes in Governance

All changes in Governance will require a ⅔ majority maintainers vote.

### Other Changes

Unless specified above, all other changes to the project require a ⅔ majority maintainers vote.
Additionally, any maintainer may request that any change require a ⅔ majority maintainers vote.

[MAINTAINERS]: MAINTAINERS.md
[COMPONENT-OWNERS]: COMPONENT-OWNERS.md
[issues]: https://github.com/smilingprogrammer/Video-Plagiarism-Detection/issues
