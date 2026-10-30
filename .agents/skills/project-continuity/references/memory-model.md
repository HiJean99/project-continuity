# Project Memory Model

## Purpose

Project memory stores durable knowledge that should survive conversation boundaries. It is not a transcript archive and should not repeat details already maintained in source code, issue trackers, experiment trackers, or domain-specific documentation.

## Default records

### PROJECT.md — stable context

Keep relatively stable:

- project purpose and intended outcomes;
- scope and explicit non-goals;
- users, stakeholders, or consumers;
- constraints and operating assumptions;
- important terminology;
- links to authoritative code, data, documents, services, or repositories.

Do not turn it into a running status report.

### STATE.md — current snapshot

Keep it short and replace stale status rather than appending a diary:

- last verified date;
- current phase and objective;
- active Work Items;
- what is currently working or complete;
- blockers and risks;
- next milestone and immediate next actions.

Use links to detailed records. If a fact has not been checked recently, label it as unverified or give its verification date.

### DECISIONS.md — decision history

Append material decisions. Each record should include:

- stable ID and date;
- status: proposed, accepted, rejected, or superseded;
- context/problem;
- decision;
- concise rationale;
- consequences/trade-offs;
- evidence or references;
- prior decision superseded, if any.

Do not record every idea as a decision. Do not rewrite history when a decision changes; append a superseding record.

### OPEN_QUESTIONS.md — unresolved questions

Track questions whose answers may change project direction or implementation:

- stable ID;
- question;
- why it matters;
- evidence or decision needed to resolve it;
- current status;
- related Work Item, if one exists.

A question is not automatically a task. Create a Work Item only when there is a concrete, actionable piece of work.

## Work Items are separate from project memory

Project memory answers: "What is this project, where does it stand, and what decisions matter?"

A Work Item answers: "What specific outcome is unfinished, what is known, what has been done, and what must happen next?"

Keep the project snapshot concise and link to active Work Items. Do not duplicate their full details in STATE.md.

## Evidence discipline

Use explicit labels where ambiguity matters:

- **Verified**: directly supported by a file, command result, reproducible experiment, or reliable source.
- **Observed**: seen in a particular run or environment, not necessarily universal.
- **Hypothesis**: plausible but unverified.
- **Inference**: reasoned from evidence; not directly observed.
- **Decision**: an accepted choice, with an owner and date where relevant.

Record provenance: relative file path, Git commit, experiment ID, citation, URL, page/section, or command used. Avoid unsupported claims such as "tested" when no test was run.
