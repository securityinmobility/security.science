---
title: "Code"
description: ""
draft: false
---

# Code

The following is a list of selected repositories and corresponding code.


## SELFY VSOC

The SELFY VSOC ([link to the GitHub repository](https://github.com/securityinmobility/selfy-vsoc-api)) is one of the contributions from the research group in the [EU-funded SELFY project](https://selfy-project.eu/). It holds the full Vehicle Security Operations Center (VSOC) stack that consists of the following components:

- ELK stack (elasticsearch, logstash, and kibana)
- VSOC API (HTTP REST)
- Locust test scripts 
- Binary scanning tool


## DC Charging Station

This repository ([link to the GitHub repository](https://github.com/securityinmobility/dc-charging-station)) contains glue code in order to create a fully working DC charging station.

In our case we use [SwitchEV/josev](https://github.com/SwitchEV/josev) for the ISO15118 stack, an [EVAcharge SE](https://chargebyte.com/products/charging-station-communication/evacharge-se) for powerline communication and a [Kratzer Automation battery tester](https://www.ni.com/de/shop/power-electronics-test-systems.html) as a HV power supply.


## AUTOSEC Framework

The AUTOSEC Framework ([link to the GitHub repository](https://github.com/securityinmobility/autosec-framework)) holds various attacker scripts to attack and features to interact with modern vehicle systems. It is continually extended with new attacks and updated to support further technologies.


## Vehicle logs 

This repository ([link to the GitHub repository](https://github.com/securityinmobility/vehiclelogs)) contains various logs that we collected from vehicles. Currently the following directories:

- ESA 5000 
- Renault Twizy 
- Tesla Model 3
- Volkswagen ID 4
- Vehicle to power grid communication


## Exploit to module conversion

This programm ([link to the GitHub repository](https://github.com/securityinmobility/exploit-to-module-conversion)) is for converting exploit code into a module for an automated penetration testing framwork e.g. the [AUTOSEC framework](#autosec-framework).


## Custom monocypher-rs library

This repository ([link to the GitHub repository](https://github.com/securityinmobility/monocypher-rs)) is a minimal, easily expendable rust binding for the [Monocypher](https://monocypher.org/) cryptography library.

It is inspired by [Jan Schreib's monocypher-rs](https://github.com/jan-schreib/monocypher-rs) implementation, but several functions were necessary in our application that are not covered by his version. The binding was also created to get familiar with bindgen.


## Survey data for publications 

This repository ([link to the GitHub repository](https://github.com/securityinmobility/survey-data)) holds the raw survey data from publications of ours.
