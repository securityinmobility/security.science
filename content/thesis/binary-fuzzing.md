+++
title = "Binary Fuzzing Harness Generation"
author = "Dominik Bayerl"
keywords = ['Software Analysis', 'Binary Analysis']
date = 2024-12-16
expiryDate = 2025-04-01
+++

<div>
    <span class="db">Published: {{< date.inline >}} {{ .Page.Date | time.Format ":date_medium" }} {{< /date.inline >}}</span>
    <span class="db">
        Thesis: 
        <a class="f6 link dim br-pill ph2 pv1 dib white bg-dark-blue">Bachelor</a>
        <a class="f6 link dim br-pill ph2 pv1 dib white bg-dark-green">Master</a>
    </span>
</div>

## Topic Overview
State-of-the-art fuzzers like AFL++ rely on fuzzing harnesses for in-memory fuzzing. While automated harness generation using LLMs on source code is an emerging field (see [Google OSS-Fuzz](https://google.github.io/oss-fuzz/research/llms/target_generation/)), our research focuses on extending this capability to binary code. The goal is to develop a trained LLM capable of understanding binaries to automatically generate fuzz harnesses. Key challenges include identifying input parameters, call signatures, handling global state mutations, and inspecting XREF calls.

## Your Tasks
- Conduct a literature review to assess the current state-of-the-art in automated fuzzing harness generation.
- Select appropriate binary fuzz targets for experimentation.
- Develop a prototype tool to automate binary fuzzing harness generation.
- Evaluate the feasibility and effectiveness of your approach.

## Requirements
- Strong interest in computer security and binary analysis.
- Experience in programming and a keen curiosity about AI-driven techniques.

## Contact
Please send your CV to:
{{< profile-card name="Dominik Bayerl" img="people/no-photo.svg" affiliation="Automotive Firmware Security Testing" >}}
    {{< cloakemail display="E-Mail" address="dominik.bayerl@carissma.eu" >}}
{{< /profile-card >}}
