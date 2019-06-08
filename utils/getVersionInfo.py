import re,os,subprocess

from utils.gitRepo import GetFormattedCommitListByDocAbbr

def GetReleaseInfo(docAbbr,shadigest=None):
    if shadigest is None:
        fmtedCommit = GetFormattedCommitListByDocAbbr(docAbbr)
        shadigest= fmtedCommit[0]['shadigest'] if  len(fmtedCommit)>0  else None

    with subprocess.Popen(['git', 'describe', '--match','v*.*-{0}'.format(docAbbr),shadigest], stdout=subprocess.PIPE) as proc2:
        version = proc2.stdout.read().decode()
        return version

def  GetVersionInfo(docAbbr,shadigest=None):
    return GetReleaseInfo(docAbbr,shadigest).split('-')[0]
