+++
title = "Fake Footage, Real People"
date = "2026-11-18"
lastmod = "2026-11-18"
authors = ["Julienne Eder", "Vishwa Vimukthi Vasu Ashoka"]
summary = "AI-enhanced dash cam footage and AI fake detectors can misrepresent or wrongly flag the people in a clip. What should a reviewer ask before such footage becomes evidence?"
+++

Imagine getting a dash cam clip with a message. *Is this you?* You hit play. There’s your bike on the roadside. There’s the jacket you wore the night you crashed. You pause on the cyclist’s face. **A stranger looks back.**

Someone has used AI to make the cyclist’s face clearer. If the enhanced frame ends up in a crash report, the face the software generated could pass for yours.

{{< full-image img="blog/fake-footage-real-people/dashcam-cyclist-illustration.png" >}}

*AI-generated illustration of the article’s hypothetical cyclist.*

## The face AI fills in

In 2024, a Washington state judge barred AI-enhanced video from a murder trial after finding it showed what the model expected to see. The prosecution’s own forensic video analyst said **every pixel in the enhanced version was new**. [7] [8]

An enhancer can supply details the camera missed. As one developer put it, the tool is guessing how a person should look. [6]

A tool built on the PULSE algorithm showed how far that guess can go. Given a pixelated photo of Barack Obama, it produced an image of a white man. PULSE’s authors acknowledged that it generated white faces far more often and cautioned against using it to identify people in blurred images. [6]

Researchers call it *representational harm* when a tool stereotypes, demeans, or erases a group of people. Here, the person in the frame disappears behind a face shaped by the model’s training data. That’s a form of *erasure*. [5] Once those guessed features are on screen, they can mislead the person reviewing the clip. [7]

## When real footage gets flagged

A reviewer might also check the original clip for tampering. If an AI detector flags it as fake, the footage of your crash could be set aside.

Insurers already use technical, forensic and AI-based checks to look for manipulated images. [3] In one study, deepfake detectors incorrectly flagged real faces of Asian and African women as fake at **1.5 to 3 times the rate for white men**. Error rates differed by up to **10.7%** between groups. [9]

Deepfake detectors can be less accurate for groups that appear less often in their training data. Genuine footage of some people may get flagged more often, while fakes involving other people can slip through. [4] Researchers call those unequal outcomes *quality-of-service harms*. [5]

{{< full-image img="blog/fake-footage-real-people/dashcam-review-illustration.png" >}}

*From left, the blurry clip, a model’s guess at the cyclist’s face, and an authenticity check. AI-generated illustration.*

### Would the same thing happen on the road?

The detector research used datasets of face videos such as FaceForensics++. [9] A dash cam typically takes in a wide, 120- to 170-degree view from behind the windscreen. [10] **Neither study tested footage like the cyclist’s clip.** Whether the same gaps show up when a face is a blur in a wide shot on a dark road is an open question.

## When the clip becomes evidence

Dash cam footage can help establish who caused a crash. In Germany, lower courts once disagreed about whether they could use it at all. In 2018, the Federal Court of Justice ruled that courts could admit it after weighing the interests in each case, even when continuous recording violated data protection rules. [1]

Some dash cams, including ones used in commercial fleets, already run AI. [2] Insurers use AI too, to spot anomalies in images and documents. With AI able to alter or generate both, the German Insurance Association says their value as evidence is harder to take for granted. [3]

## What should a reviewer ask for?

Insurers already look at image files, metadata, and whether what they see adds up. [3] For surveillance cameras, the standards body ONVIF has a specification for signing video as it’s captured so reviewers can detect later changes. [11] With AI in the process, reviewers also need ways to check how accurately the footage shows everyone in it.

- **Keep the original in view.** Save it alongside the enhanced version. Use the original to establish what the camera captured and treat the added details as guesses. [6]
- **Make each step reproducible.** Record how the clip was processed so another reviewer can repeat it. The Washington court rejected the enhancement partly because the tool lacked peer review and general acceptance among forensic video analysts. [7]
- **Test across groups and conditions.** Check how well the tool works at night, at low resolution, and for different groups of people. The detector study’s authors warn that a single overall accuracy figure gives too little information to justify widespread commercial use. [9]

## If it were your footage

German courts already weigh the value of dash cam evidence against the personality rights of the people filmed, case by case. [1] They could also consider how the clip was processed and whether the tools represent the people in it equally well.

Before the clip goes into a report, what would you want the reviewer to ask?

1. **Is the footage authentic?**
2. **Does it show everyone in it accurately?**
3. **Whose footage would we doubt, and why?**

## References & Links

[1]: **Bundesgerichtshof:** Urteil vom 15. Mai 2018, VI ZR 233/17 (full text, German). (https://mi.uni-wuppertal.de/fileadmin/Abteilung/MT/news/BGH-Dashcamurteil_15.5.2018.pdf)

[2]: **Ambarella, Inc.:** Fleet management technology leader KeepTruckin partners with Ambarella on next-generation AI device for front ADAS, driver monitoring and telematics. Press release, 12 August 2021. (https://www.ambarella.com/news/fleet-management-technology-leader-keeptruckin-partners-with-ambarella-on-next-generation-ai-device-for-front-adas-driver-monitoring-and-telematics/)

[3]: **Gesamtverband der Deutschen Versicherungswirtschaft (GDV):** When images lie: insurance fraud with AI. Last updated 9 June 2026. (https://www.gdv.de/gdv-en/topics/digitalisation/when-images-lie-insurance-fraud-with-ai-201160)

[4]: **Y. Ju, S. Hu, S. Jia, G. H. Chen, S. Lyu:** Improving fairness in deepfake detection. WACV 2024. (https://arxiv.org/pdf/2306.16635)

[5]: **R. Shelby et al.:** Sociotechnical harms of algorithmic systems: Scoping a taxonomy for harm reduction. AIES 2023, pp. 723–741. (https://arxiv.org/abs/2210.05791v3)

[6]: **K. Truong:** This image of a white Barack Obama is AI's racial bias problem in a nutshell. VICE, 23 June 2020. (https://www.vice.com/en/article/this-image-of-a-white-barack-obama-is-ais-racial-bias-problem-in-a-nutshell)

[7]: **M. D. Fan:** AI-enhanced evidence. Boston University Law Review, 105:2149, 2025. (https://www.bu.edu/bulawreview/files/2026/05/FAN.pdf)

[8]: **T. Stelloh:** Washington state judge blocks use of AI-enhanced video as evidence in possible first-of-its-kind ruling. NBC News, April 2024. (https://www.nbcnews.com/news/us-news/washington-state-judge-blocks-use-ai-enhanced-video-evidence-rcna141932)

[9]: **L. Trinh, Y. Liu:** An examination of fairness of AI models for deepfake detection. IJCAI 2021. (https://arxiv.org/pdf/2105.00558)

[10]: **The Forensic Experts Group:** Do you see what I see? Pitfalls of video analysis in traffic collision cases. The Singapore Law Gazette, October 2018. (https://lawgazette.com.sg/practice/practice-support/do-you-see-what-i-see/)

[11]: **ONVIF:** Partnering to protect global video authenticity standards. ONVIF Blog, 18 June 2025. (https://www.onvif.org/blog/2025/06/18/partnering-to-protect-global-video-authenticity-standards/)
