+++
title = "Intelligent Detection of Decreasing Solve Rates and Adjustment of Password Recovery Strategies"
author = "Claudius Laves"
keywords = ['Password Recovery', 'Password Recovery Strategies']
date = 2026-06-03
+++

# Intelligent Detection of Decreasing Solve Rates and Adjustment of Password Recovery Strategies

<div>
    <span class="db">Published: {{< date.inline >}} {{ .Page.Date | time.Format ":date_medium" }} {{< /date.inline >}}</span>
    <span class="db">
        Thesis: 
        <a class="f6 link dim br-pill ph2 pv1 dib white bg-dark-green">Master</a>
    </span>
</div>

## Topic Overview
Password recovery sessions rely on a sequence of attack strategies such as dictionary attacks, brute-force, and rule-based mutations. In practice, these strategies lose effectiveness over time as the most easily cracked passwords are recovered early and the solve rate drops. Currently, strategy adaptation is largely manual. This thesis aims to automatically detect declining solve rates using machine learning algorithms and time-series analysis, and to dynamically switch or prioritize recovery strategies in response.

## Your Tasks
- Survey existing password recovery frameworks and adaptive search strategies
- Define and implement metrics for real-time solve rate monitoring
- Develop a detection algorithm for identifying significant rate drops
- Design a decision mechanism for dynamic strategy adaptation
- Evaluate the system against realistic password datasets (e.g., RockYou, etc.)

## Requirements
- Machine learning & time-series analysis (anomaly detection, trend analysis)
- Python skills
- Basic knowledge of IT security & password hashing
- Linux / command-line proficiency
- Analytical, independent working style

## Contact
Please send your CV to:
{{< profile-card name="Claudius Laves" img="people/claudi.png" affiliation="Leveraging Fingerprinting for Cybersecurity" >}}
    {{< cloakemail display="E-Mail" address="claudius.laves@carissma.eu" >}}
{{< /profile-card >}}