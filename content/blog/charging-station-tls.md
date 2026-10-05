+++
title = "Who Actually Uses TLS? Measuring Charging Station Security in Germany"
date = "2026-10-05"
lastmod = "2026-10-05"
authors = ["Jakob Löw", "Lukas Eder"]
summary = "ISO 15118 fast-charging communication can be authenticated and encrypted with TLS. We tested a targeted set of German fast chargers and extrapolated the results to over half the market: only 27.4% actually do it."
+++

# The Padlock Nobody Turns On

When you plug your electric car into a fast charger, the car and the charging station start talking long before any energy flows. They negotiate voltage limits, current limits, temperature constraints and, increasingly, who pays for the session. All of this happens over a powerline link inside the charging cable.

The standard behind this conversation in Europe, ISO 15118, includes the same kind of protection your browser uses every day: TLS, which authenticates the charging station and encrypts the session. The catch is that TLS is optional. Both the car and the charger have to support it, and the charger has to be configured with a valid certificate.

So we asked a simple question: **how many fast chargers in Germany actually use it?**

The short answer is fewer than one in three in the part of the market we could measure, and probably even fewer across the whole country.

## Why This Matters

Our group has spent the last few years taking charging communication apart. In our technology review of fast-charging communication [1], we mapped out how ISO 15118 works and where its attack surface lies. In our E-Energy '25 paper [2], we showed how cheap off-the-shelf powerline hardware can reliably sniff and man-in-the-middle a charging session from the first packet onward. And in our work on plug and charge [3], we demonstrated a relay attack in which an attacker charges their own car and bills a victim's contract.

Other research groups have shown similar results: wireless eavesdropping on the powerline signal, wireless denial of service, TLS stripping, and payment relay attacks [4, 5, 6, 7].

A common thread runs through most of these attacks. They work far better, or only work at all, when the charging session runs **without TLS**. Without it, nothing stops an attacker from pretending to be the charging station, reading the session, or altering it.

That leads straight to an empirical question that nobody had answered at national scale: how often is the protection that already exists in the standard actually switched on?

## Testing 40,000 Chargers Without Visiting 40,000 Chargers

Germany has more than 40,000 CCS fast-charging points. Driving to every single one with a test device is not an option. We needed a way to test a few dozen and still say something meaningful about the rest.

The trick lies in the structure of the market. Hundreds of companies operate charging stations, but very few build them. Charge point operators (CPOs) such as EnBW, Aral or IONITY mostly buy off-the-shelf hardware from a small number of manufacturers. That leads to two assumptions:

* **A1:** Charging stations from the same manufacturer support the same set of features, such as TLS. Whether a feature is actually enabled is decided by the operator through configuration and certificate provisioning.
* **A2:** An operator configures all its stations from the same manufacturer the same way.

If both hold, testing one station from a given (operator, manufacturer) pair tells you about every station in that pair. The methodology then works like this:

1. **Collect data.** We combined the official charging station register of the Bundesnetzagentur [8] with the community-curated map of goingelectric.de [9]. The official register has locations and operators but no hardware details; goingelectric users add manufacturer and model information.
2. **Clean it.** Manufacturer labels were normalized (for example "Tesla" and "Supercharger" are the same thing), and charging points without a known manufacturer were dropped. Out of 44,313 German CCS points listed in December 2025, 40,949 remained.
3. **Cluster** the charging points by (operator, manufacturer).
4. **Sample** by starting with the largest clusters and testing stations within reach of our lab in Ingolstadt.
5. **Field test** each station with our own testing device.
6. **Extrapolate** each result to its whole cluster.
7. **Aggregate** everything into a national estimate.

## One Manufacturer to Rule Them All

The market analysis turned out to be quite convenient for us. Nearly **66%** of all German CCS charging points come from a single manufacturer: **Alpitronic**. ABB (10.3%) and Tesla (9.2%) follow far behind, and everyone else shares the remaining 14.5%.

On the operator side, the market is broader. It includes energy utilities (EnBW, EWE, E.ON, Vattenfall), carmakers (Tesla, Volkswagen's Elli, and IONITY), supermarkets (Lidl, Aldi, Kaufland, Edeka) and fuel station chains (Aral pulse, Shell). Four of the five largest operators use Alpitronic for more than 90% of their charging points. The fifth is Tesla, which builds its own.

This concentration is the reason a manageable number of field tests can cover a large share of the country.

## Checking the Assumptions

Extrapolation is only as good as the assumptions behind it, so we went looking for counterexamples.

For **A1**, we tested stations from Alpitronic, ABB, Tritium, Compleo, Efacec, EKOenergetyka and ChargePoint across hardware generations from 2018 to 2024. We found no case where two stations from the same manufacturer differed in their ability to do TLS. Public firmware documentation also shows that different models of the leading manufacturer share a common software platform.

For **A2**, we tested multiple stations for the same operator–manufacturer pairs at different locations and with different installation years: eight EnBW stations at five sites, five Aral stations at four sites, and three IONITY stations at three sites. Within each pair, the behavior was identical. We also pulled in 25 stations measured by Szakály et al. in the UK, Switzerland and Hungary [10]. Operators present in both datasets, such as IONITY, Allego and Fastned, were configured the same way across borders.

None of this is a mathematical proof. Configurations change over time, large operators may have regional differences, and small operators are underrepresented. The results should be read as a well-founded approximation, not an exact count.

## The Testing Device

To test a charger, you have to convince it that a car is plugged in. We built a small, portable device that does exactly that and nothing more:

* A **Raspberry Pi Zero 2 W** runs the communication logic and logs everything.
* A **HomePlug Green PHY powerline modem** (Codico RED-BEET evaluation board) is connected to the Pi over SPI.
* A **modified Type 2 charging cable** connects to the station. A few resistors and switches reproduce the control pilot states a real vehicle would signal. The cable has no DC power contacts.
* An ordinary **power bank** supplies power, so the whole thing fits in a backpack.

The software plays the role of the car. It goes through the powerline pairing (SLAC), service discovery, the optional TLS handshake and protocol negotiation for DIN SPEC 70121, ISO 15118-2 and ISO 15118-20. Each station goes through several test cycles: one where the "car" insists on TLS, and others that probe which charging protocols the station supports and which one it prefers.

All the information we need is exchanged before any energy transfer starts. The device stops the session at that point, so the charger never puts voltage on the cable.

## The Results

We tested stations from 14 operators, covering clusters that together represent **51.9% of all German CCS charging points**. Within that scope:

* **100%** support DIN SPEC 70121, the older baseline protocol without any security controls.
* **More than 90%** support ISO 15118-2, the protocol that *can* use TLS.
* Only **27.4%** actually establish a TLS-protected session.

| Operator | Manufacturer | Share of German CCS points | ISO 15118-2 | TLS |
|---|---|---:|:---:|:---:|
| EnBW | Alpitronic | 17.7% | ✓ | ✗ |
| Aral | Alpitronic | 6.6% | ✓ | ✓ |
| EWE | Alpitronic | 4.9% | ✓ | ✗ |
| Allego | Alpitronic | 4.3% | ✓ | ✓ |
| Pfalzwerke | Alpitronic | 3.4% | ✓ | ✗ |
| Elli | Compleo | 2.2% | ✓ | ✗ |
| Aldi | Alpitronic | 2.0% | ✓ | ✗ |
| Lidl | ABB | 1.9% | ✓ | ✗ |
| Mer | Alpitronic | 1.8% | ✓ | ✗ |
| IONITY | Tritium | 1.6% | ✓ | ✓ |
| Kaufland | ABB | 1.6% | ✓ | ✗ |
| IONITY | ABB | 1.1% | ✓ | ✓ |
| Edeka | Compleo | 0.9% | ✗ | ✗ |
| Fastned | Alpitronic | 0.8% | ✓ | ✗ |
| IONITY | Alpitronic | 0.6% | ✓ | ✓ |
| Circle K | ABB | 0.5% | ✗ | ✗ |
| Aral | Compleo | <0.1% | ✗ | ✗ |

The most striking row is the first one. Germany's largest operator runs Alpitronic hardware, the same hardware that does TLS just fine at Aral and Allego, and it does not use TLS.

## It's Not the Hardware

That observation sums up the main finding. **The gap is operational, not technical.** Every major manufacturer we tested can do TLS. Identical or even older models from the same product line do TLS at one operator and not at another.

What is missing is the certificate. For the car to accept a TLS connection, the charging station must present a certificate chain that ends in a root certificate authority the car trusts. On the web, getting such a certificate is free and fully automated, thanks to services like Let's Encrypt. In the charging world, public key infrastructure (PKI) providers typically charge a one-time fee plus a recurring fee **per charging station**.

At least four V2G PKI operators offer root CAs for ISO 15118 today. In our entire dataset, we only ever saw certificates from one of them: the Hubject V2G Root CA.

## Security as a Side Effect of Convenience

Looking at who *does* use TLS reveals a pattern. ISO 15118 requires TLS for **plug and charge**, the feature that lets the car authenticate and pay automatically when plugged in. Every network that offers plug and charge therefore also uses TLS.

IONITY introduced plug and charge in October 2021, and even its stations built before that date now do TLS, so they were updated after installation. Aral introduced plug and charge in early 2022, with the same pattern.

In other words, TLS shows up wherever operators wanted plug and charge, not because anyone set out to secure the charging session. Security is a by-product of a payment feature.

## The Real Number Is Probably Lower

Our 27.4% describes the measured half of the market, which leans towards large operators. We expect the other half to look worse.

A large part of the remaining charging points belongs to small operators that sell through roaming networks such as NewMotion, be.energised, Ladenetz and innogy. None of those networks advertise plug and charge, and the stations we spot-checked confirmed the lack of TLS. For an operator with a handful of chargers, PKI fees and integration effort rarely pay off.

## What Would Help

Regulation is starting to push in the right direction. Under the EU Alternative Fuels Infrastructure Regulation (AFIR) [11], newly deployed public charging points have to support ISO 15118-20 from 2027 onward. ISO 15118-20 makes TLS mandatory, so new installations will have to do it. The tens of thousands of stations already in the ground are not affected.

To close that gap, getting a charging station certificate has to become as boring as getting a certificate for a website. A charging-world equivalent of ACME, the protocol behind Let's Encrypt, could make certificates free, automatic and secure by default, instead of a paid, manual, per-station process. That is one of the directions we want to explore next.

Today, charging communication looks a lot like the web did years ago: the padlock exists, most sites just don't bother.

## Data and Reproducibility

The methodology is not specific to Germany. Anyone with charging station data and a testing device can apply it to another country or region, and we would love to see comparable numbers from elsewhere.

We publish all our raw measurement data, including communication dumps and station model information, on GitHub [12].

This work was carried out in the research project [eSiLa](https://www.esila.bayern/) ("Elektromobiles Sicheres Laden"), funded by the Bavarian Ministry of Economic Affairs, Regional Development and Energy. The paper is co-authored by Jakob Löw, Lukas Eder, Alexander Müller and Hans-Joachim Hof. If you want to know more about the people behind it, our [first blog post](/blog/welcome-post/) introduces the whole group.

## References & Links

[1]: **J. Löw, K. Mayer, H.-J. Hof:** Fast Charging Communication and Cybersecurity: A Technology Review (2024).

[2]: **L. Eder, J. Löw, H.-J. Hof:** Charging Communication Sniffing and Man-in-the-Middle Attacks. E-Energy '25. (https://doi.org/10.1145/3679240.3734648)

[3]: **J. Löw, V. Vasu, T. Hutzelmann, H.-J. Hof:** Charge It to My Neighbor: A Relay Attack on ISO 15118 Plug and Charge Payment.

[4]: **R. Baker, I. Martinovic:** Losing the Car Keys: Wireless PHY-Layer Insecurity in EV Charging. USENIX Security 2019. (https://www.usenix.org/conference/usenixsecurity19/presentation/baker)

[5]: **S. Köhler et al.:** Brokenwire: Wireless Disruption of CCS Electric Vehicle Charging. NDSS 2023. (https://doi.org/10.14722/ndss.2023.23251)

[6]: **M. Szakály et al.:** DCeption: Real-world Wireless Man-in-the-Middle Attacks Against CCS EV Charging (2026). (https://arxiv.org/abs/2601.15515)

[7]: **M. Conti et al.:** EVExchange: A Relay Attack on Electric Vehicle Charging System. ESORICS 2022. (https://doi.org/10.1007/978-3-031-17140-6_24)

[8]: **Bundesnetzagentur:** Ladesäulenkarte. (https://www.bundesnetzagentur.de/DE/Fachthemen/ElektrizitaetundGas/E-Mobilitaet/Ladesaeulenkarte/start.html)

[9]: **GoingElectric:** Stromtankstellen API. (https://www.goingelectric.de/stromtankstellen/api/docs/)

[10]: **M. Szakály, S. Köhler, I. Martinovic:** Current Affairs: A Security Measurement Study of CCS EV Charging Deployments (2025). (https://arxiv.org/abs/2404.06635)

[11]: **Regulation (EU) 2023/1804:** Alternative Fuels Infrastructure Regulation (AFIR). (https://eur-lex.europa.eu/eli/reg/2023/1804/oj)

[12]: **Raw measurement data:** (https://github.com/M4GNV5/charging-station-tests-germany)
