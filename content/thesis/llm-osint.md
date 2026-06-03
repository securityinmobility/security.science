+++
title = "On Using LLMs for enriching Password Recovery Strategies"
author = "Claudius Laves"
keywords = ['Password Recovery', 'Password Recovery Strategies']
date = 2026-06-03
+++

# On Using LLMs for enriching Password Recovery Strategies

<div>
    <span class="db">Published: {{< date.inline >}} {{ .Page.Date | time.Format ":date_medium" }} {{< /date.inline >}}</span>
    <span class="db">
        Thesis: 
        <a class="f6 link dim br-pill ph2 pv1 dib white bg-dark-blue">Bachelor</a>
    </span>
</div>

## Topic Overview
Generic wordlists and rules used in password recovery ignore the personal and regional context in which passwords are typically chosen. People often base their passwords on locally meaningful terms - sports clubs/players, landmarks, regional figures, or place names. This thesis aims to build an OSINT Sleuth system that uses LLMs to automatically gather publicly available information about a target person or region, and derives context-specific wordlists, mutation rules, and attack patterns to dynamically enrich ongoing recovery sessions.

## Your Tasks
- Survey OSINT methodologies, LLM prompt engineering, and password recovery techniques
- Design an automated OSINT pipeline for extracting regional and person-related terms
- Use LLMs to generate targeted wordlists and Hashcat rule sets from collected data
- Integrate generated resources into active recovery sessions
- Evaluate the approach against realistic, regionally contextualized scenarios

## Requirements
- Experience with LLMs & prompt engineering (Ollama, OpenAI API, LangChain or similar)
- Python (web scraping, API integration)
- Basic knowledge of IT security & password hashing
- Interest in OSINT and open-source intelligence methods
- Analytical, independent working style

## Contact
Please send your CV to:
{{< profile-card name="Claudius Laves" img="people/claudi.png" affiliation="Leveraging Fingerprinting for Cybersecurity" >}}
    {{< cloakemail display="E-Mail" address="claudius.laves@carissma.eu" >}}
{{< /profile-card >}}