import sys
from datetime import date

#from pyorcid import OrcidAuthentication, Orcid
from pyorcid import OrcidScrapper

page_head = """
+++
menu = "main"
weight = 50
title = "Publications"
+++

# Publications

The following is a list of peer reviewed papers written by members of our
research group, ordered by date descending.

"""

conference_head = """
## Posters, Talks and more

The following is a list of conference talks, posters and other research
oriented contributions by members of our research group.

"""

# generate this using `cat content/_index.md | grep -Eo 'orcid.org/[0-9A-Z-]+'`
# start and end dates added manually allowing to exclude publications before someone
# joined or after someone left the research group
orcids = [
    ('0000-0002-6930-9271', '1970-01-01', '9999-12-01'),
    ('0009-0001-1594-2119', '1970-01-01', '9999-12-01'),
    ('0000-0003-0439-066X', '1970-01-01', '9999-12-01'),
    ('0000-0003-2441-7962', '1970-01-01', '9999-12-01'),
    ('0009-0005-0529-0996', '1970-01-01', '9999-12-01'),
    ('0009-0006-7088-8684', '1970-01-01', '9999-12-01'),
    ('0009-0009-7414-1360', '1970-01-01', '9999-12-01'),
    ('0009-0003-6679-3672', '1970-01-01', '9999-12-01'),
    ('0009-0000-8446-7641', '1970-01-01', '9999-12-01'),
    ('0000-0002-5597-3913', '1970-01-01', '2024-12-31'), # Kevin Mayer
    ('0009-0006-4383-5683', '1970-01-01', '2024-12-31'), # Marco Michl
]

#orcid_auth = OrcidAuthentication(client_id=client_id, client_secret=client_secret)
#access_token = orcid_auth.get_public_access_token()

known_works = []
papers = []
for orcid, start_date, end_date in orcids:
    #orcid = Orcid(orcid_id=orcid, orcid_access_token=access_token, state="public")
    orcid = OrcidScrapper(orcid)
    start_date = date.fromisoformat(start_date)
    end_date = date.fromisoformat(end_date)
    for work in orcid.works()[0]:
        date_split = work['publication-date'].split('/')
        try:
            if len(date_split) == 1:
                year = int(date_split[0])
                month = 0
            elif len(date_split) == 2:
                year = int(date_split[1])
                month = int(date_split[0])
            else:
                raise ValueError("unknown date format!")
        except ValueError:
            print(f"could not parse date: {date_split} for {work['title']}", file=sys.stderr)
            continue

        publication_date = date.fromisoformat(f"{year}-{month or 6:02d}-15")
        if publication_date > end_date or publication_date < start_date:
            continue

        if work['url'] in known_works or work['title'] in known_works:
            continue

        if work['url'] is None:
            known_works.append(work['title'])
        else:
            known_works.append(work['url'])

        papers.append({
            "order": year * 100 + month,
            "date": f"{year}-{month:02d}" if month != 0 else str(year),
            "title": work["title"],
            "url": work["url"],
        })

papers.sort(key=lambda x: -x["order"])

with open("content/publications.md", "w+", encoding="utf8") as fd:
    fd.write(page_head)
    for paper in papers:
        if paper['url']:
            fd.write(f"- {paper['date']}: [{paper['title']}]({paper['url']})\n")

    fd.write("\n")
    fd.write(conference_head)

    for paper in papers:
        if not paper['url']:
            fd.write(f"- {paper['date']}: {paper['title']}\n")

    fd.write("\n")
