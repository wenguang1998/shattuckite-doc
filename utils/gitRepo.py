import subprocess
import re
from utils.misc import GetDocIndeStrByDocAbbr


def GetFormattedCommitListByDocAbbr(docAbbr: str):
    SHADOC_INDEX = GetDocIndeStrByDocAbbr(docAbbr)
    SHADOC_REGEX_PATTERN = re.compile(
        r"^commit(.*?)$\nAuthor:(.*?)$\nDate:(.*?)$\s+SHADOC-{0:s}\sDOC\sUPDATE\s+AUTHOR:(.*?)\s+CENSOR:(.*?)\s+NOTE:(.*?)$".format(SHADOC_INDEX), re.S | re.M)
    with subprocess.Popen(['git', 'log', '--grep', 'SHADOC-{0} DOC UPDATE'.format(SHADOC_INDEX)], stdout=subprocess.PIPE) as proc:
        results = (re.findall(SHADOC_REGEX_PATTERN,
                              proc.stdout.read().decode()))
        return [{
            "shadigest": result[0].lstrip(),
            "author":result[1].lstrip(),
            'censor': result[4].lstrip(),
            'note': result[5].lstrip(),
            'dataString': re.sub('\+\d+', '', result[2]).rstrip().lstrip()
        } for result in results]
