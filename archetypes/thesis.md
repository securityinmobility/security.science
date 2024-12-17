+++
draft = true
title = "{{ replace .TranslationBaseName "-" " " | title }}"
author = "John Wayne"
keywords = []
date = '{{ .Date | time.Format "2006-01-02" }}'
expiryDate = '{{ (.Date | time.AsTime).AddDate 0 6 0 | time.Format "2006-01-02" }}' # Expire after 6 month
+++

A brief description of the thesis. To add header pills:
```text
<a class="f6 link dim br-pill ph2 pv1 dib white bg-dark-blue">Bachelor</a>
<a class="f6 link dim br-pill ph2 pv1 dib white bg-dark-green">Master</a>
```
