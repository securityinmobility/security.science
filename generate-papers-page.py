import sys

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

# generate this using `cat content/_index.md | grep -Eo 'orcid.org/[0-9A-Z-]+'`
orcids = [
    '0000-0002-6930-9271',
    '0009-0001-1594-2119',
    '0000-0002-5597-3913',
    '0000-0003-0439-066X',
    '0000-0003-2441-7962',
    '0009-0006-4383-5683',
    '0009-0005-0529-0996',
    '0009-0009-7414-1360',
    '0009-0006-7088-8684',
]

#orcid_auth = OrcidAuthentication(client_id=client_id, client_secret=client_secret)
#access_token = orcid_auth.get_public_access_token()

known_urls = []
papers = []
for orcid in orcids:
    #orcid = Orcid(orcid_id=orcid, orcid_access_token=access_token, state="public")
    orcid = OrcidScrapper(orcid)
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
            print(f"could not parse date: {date_split}", file=sys.stderr)
            continue

        if "url" not in work:
            # ignore these for now. Without an author and date this is useless
            continue

        if work["url"] in known_urls:
            continue
        known_urls.append(work["url"])

        papers.append({
            "order": year * 100 + month,
            "date": f"{year}-{month:02d}" if month != 0 else str(year),
            "title": work["title"],
            "url": work["url"],
        })

papers.sort(key=lambda x: -x["order"])

with open("content/publications.md", "w+") as fd:
    fd.write(page_head)
    for paper in papers:
        fd.write(f"- {paper['date']}: [{paper['title']}]({paper['url']})\n")
    fd.write("\n")
