import sys
sys.path.append('../../')
from utils.getVersionInfo import GetReleaseInfo, GetVersionInfo
import os
from utils.commonSettings import *
from utils.getTexSettings import GetTexMaketitle
import requests
import re

project = '项目计划书'
copyright = '2019, CNLHC'
author = 'CNLHC'
docIndexStr = "001"
docAbbr = "SDP"
htmlhelp_basename = 'shattuckitedoc'

version = GetVersionInfo(docAbbr)
release = GetReleaseInfo(docAbbr)

contributors = [
    {
        'id': '16231275',
        'name': '刘瀚骋',
        'work': '内容编写/内容审核/绘图/自动化工具编写'
    }
]

latex_elements['preamble'] = GetTexMaketitle(
    documentTitle=project, docAbbr=docAbbr, contributors=contributors)

latex_documents = [(master_doc, 'shattuckite-{docAbbr}.tex'.format(docAbbr=docAbbr),
                    'shattuckite {title}'.format(title=project), 'SHADOC-{docIndexStr},SDP,第五组'.format(docIndexStr=docIndexStr), 'howto'), ]