import re
import os
import subprocess
import datetime
import json
from jinja2 import Template
from utils.gitRepo import GetFormattedCommitListByDocAbbr
from utils.getVersionInfo import GetReleaseInfo


def GetTexMaketitle(docAbbr,contributors: list = [], documentTitle: str = ''):
    ctx = {
        'revisionLists': [],
        'contributors':contributors,
        'documentTitle': documentTitle}
    formattedCommitList = GetFormattedCommitListByDocAbbr(docAbbr)

    for record in formattedCommitList:  # type:str
        ctx['revisionLists'].append({
            'version': GetReleaseInfo(docAbbr,shadigest=record['shadigest']),
            'date': datetime.datetime.strptime(record['dataString'], '%a %b %d %H:%M:%S %Y').strftime('%Y-%m-%d %H:%M'),
            'author': record['author'],
            'censor': record['censor'],
            'note': record['note']
        })

    print(ctx)
    with open(os.path.dirname(os.path.abspath(__file__))+'/TexPreTemplate.latex.jinja2', 'r') as tfp:
        template = Template(tfp.read())
        return template.render(**ctx)


if __name__ == "__main__":
    print(GetTexMaketitle(docAbbr="SDP"))
