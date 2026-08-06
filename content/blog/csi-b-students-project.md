+++
title = "THIARA: From Spreadsheet Chaos to Production Code"
date = "2026-08-05"
lastmod = "2026-08-05"
authors = ["Julian Blümke", "Claudius Laves"]
summary = "A bachelor class was told to build a TARA tool for ISO/SAE 21434. They shipped an actual open-source app.>"
+++

# A Semester-Long Case Study in Automotive TARA Tooling

Take a room of Bachelor's students with wildly different backgrounds. Give them one semester. Ask them to build a complex, production-ready security application from scratch.

They shipped it.

For our Cybersecurity practical project lecture, we set our students a single, ambitious assignment: spend one semester building a real-world tool that solves a genuine pain point in automotive security. No scaffolding, no prepared codebase, no safety net. They organized themselves, chose their stack, and delivered something that works, which is worth documenting as a small case study in what a semester of focused, self-organized student work can actually produce.

Today, that "student assignment" is a fully functioning, open-source project the students built entirely themselves. You can clone it, launch it, and self-host it right now.

## Excel Is Not a Security Tool

If you work in automotive cybersecurity, you already know the four-letter acronym that gives system architects night terrors: TARA (Threat Analysis and Risk Assessment).

Under regulations like UNECE R-155 [1], performing a rigorous TARA isn't optional. It's a mandatory gatekeeper for vehicle type approval. The governing standard, ISO/SAE 21434:2021 [2], lays out a comprehensive, tightly interconnected process for identifying assets, mapping damage, and quantifying attack feasibility.

So how does the industry typically execute this complex, highly linked security analysis?

_**Excel.**_

Multi-billion-dollar automotive architectures are routinely assessed using fragile spreadsheet webs, sprawling Word documents, and copy-pasted risk matrices. The practical result is predictable: no overview of dependencies, painful refactoring whenever a single component changes, poor usability, and no structured guidance through the ISO pipeline. Compliance turns into an exercise in wrestling with cells rather than actually finding threats.

Put plainly: Excel is not a security tool.

Recognizing this gap, we posed the challenge to our students: design and build a modern, web-based platform that natively implements the ISO/SAE 21434 TARA process from the ground up. Everything from architecture decisions to implementation was left entirely in their hands.

## Meet THIARA

The students named their tool THIARA, a blend of our institution, THI (Technische Hochschule Ingolstadt), and TARA. (Managing cybersecurity risk, they figured, should feel a bit more like wearing a crown than nursing a headache.)

THIARA is an open-source, self-hostable, Docker-first TARA platform, designed and implemented by the students from the ground up. Rather than reaching for a toy tech stack to hit a deadline, they built it on Blazor and .NET, producing a responsive, production-grade web application capable of handling genuinely complex enterprise workflows. No enterprise sales call, no proprietary cloud lock-in. Just infrastructure you control, deployable in minutes.

Access the codebase directly on GitHub: [tara-tool-thi Organization] [3]

## Zooming In: The Domain Model as a Story

The application guides users step by step through a strict, hierarchical domain pipeline:

```text
[ Project ] 
   └── [ Item Definition ] 
          └── [ Asset Identification ] 
                 └── [ Damage Scenarios & Impact ] 
                        └── [ Threat Scenarios ] 
                               └── [ Attack Paths & Feasibility ] 
                                      └── [ Security Requirements ]
```

* **Project & Item Definition:** Define the high-level system boundary (e.g., an ECU, gateway, or telematics unit).
* **Asset Identification:** Pinpoint what needs protection (e.g., cryptographic keys, CAN signals, firmware integrity).
* **Damage Scenarios & Impact:** Evaluate safety, financial, operational, and privacy impacts if an asset is compromised.
* **Threat Scenarios:** Map out what an attacker could realistically achieve.
* **Attack Paths & Feasibility Rating:** Trace the exact steps an adversary must execute to realize the threat, scoring attack feasibility according to ISO guidelines.
* **Security Requirements:** Arrive at the ultimate destination: actionable, traceable security controls tailored directly to the discovered risks.

This wasn't handed to the students as a spec to fill in; the pipeline above is the product of their own analysis of how the standard's individual clauses actually connect in practice.

## Built for Real Security Teams

A static, single-user tool misses how modern engineering teams actually operate. We made that a hard requirement from day one: THIARA had to be engineered as a multi-user framework, and the students built it accordingly.

To reflect real-world organizational structures, where engineers, risk managers, and external auditors all need different touchpoints, THIARA enforces granular permission levels per project:

* **Read (Viewer):** Ideal for external auditors or stakeholder reviews.
* **Write (Contributor):** For security engineers actively defining assets and threats.
* **Manage (Lead):** For team leads managing project structures and review states.
* **Owner (Admin):** Complete control over access control and project lifecycle.

The result doesn't read like an academic toy model. It mirrors, with surprising fidelity, how automotive security engineering actually gets done, and the students are the ones who turned that requirement into a working permission system.

## The Part Excel Cannot Do

Laying out the pipeline is the easy half. The hard half is everything a spreadsheet quietly refuses to do for you, and that's where the students spent most of their semester.

Take the risk value. In a spreadsheet, it's a number somebody types into a cell and then forgets to update. In THIARA, it's derived. A threat scenario inherits the feasibility of its most critical attack path and combines it with the impact rating of the damage scenario above it. Add a nastier attack path to an existing threat six weeks into the analysis, and the risk climbs on its own. Nobody has to remember which cells downstream were supposed to change, which is precisely the refactoring nightmare that makes spreadsheet-based TARAs age so badly.

The tool also refuses to let you skip steps. A damage scenario cannot be saved without at least one security goal attached, because a damage scenario without a violated security goal isn't a finding; it's a sentence. Small guardrails like this are the difference between a tool that stores your analysis and a tool that keeps it honest.

A few other things the students built that are easy to overlook and hard to live without:

* **Diagrams where they belong:** item definitions carry the technical sketch, preliminary architecture, item boundary, and operational environment as first-class attachments, not as a screenshot pasted into a Word file that nobody can find later.
* **Tagged assets:** filter and group across a project instead of scrolling a 400-row sheet.
* **Risk treatment on the record:** avoid, reduce, share, or retain, captured next to the risk it belongs to.
* **Full-graph export:** one call serializes an entire project, from item definitions down to individual attack steps, into a single structured JSON file. Reporting, backups, and migration stop being a copy-paste ritual.

## How They Actually Pulled It Off

A project this size doesn't hold together on enthusiasm alone. What carried it was process, and the students set that process up themselves.

Nothing reached the main branch by accident. Work moved through feature branches and pull requests, each one gated by required reviewers and automated CI checks. A merge triggered a deployment pipeline. The most instructive part, at least from where we were sitting, is what happened to the features that weren't good enough the first time: user management and the registration flow were both torn down and rebuilt across two and three iterations as review feedback landed and the requirements sharpened. Voluntarily rewriting code that already works, because the review says it isn't right yet, is a standard plenty of professional teams never reach.

By the end, that added up to 58 merged commits from roughly a dozen contributors, a permission system, and a deployment pipeline that still runs today. The code is the visible output. The habits are the part that will outlast the grade.

## A Note From the Supervisors

The two of us running this lecture were Claudius Laves and Julian Blümke.

Both of us are doctoral researchers in the Security in Mobility research group here at THI, and if you want to know what we work on when we aren't grading pull requests, our very first post introduces the entire group, one member at a time: [Welcome to our Blog](/blog/welcome-post/).

The architecture, the code, and the decisions behind both belong to the students. We mostly got to watch it come together.

## Try It Yourself

THIARA is open source, and the fastest way to judge any of the above is to run it. Point Docker at a volume and start it. On first launch it prints a one-time registration link to the console instead of shipping with a default admin password, which we consider a reasonable standard for a security tool to hold itself to. From there, the first project is yours.

The repository is public [3]. Stars are nice, issues are better, and pull requests are best. If you're a THI student reading this and wondering whether a semester project can outlive the semester: this one did, and the next commit could be yours.

## References & Links

[1]: **UNECE R-155:** UN Regulation No. 155 – Uniform provisions concerning the approval of vehicles with regards to cybersecurity and cybersecurity management system. (https://unece.org/transport/documents/2021/03/standards/un-regulation-no-155-cyber-security-and-cyber-security)

[2]: **ISO/SAE 21434:2021:** Road vehicles — Cybersecurity engineering. (https://www.iso.org/standard/70918.html)

[3]: **THIARA GitHub Repository:** (https://github.com/tara-tool-thi)