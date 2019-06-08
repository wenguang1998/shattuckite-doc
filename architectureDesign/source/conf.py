import sys
sys.path.append('../../')
import re
import requests
from utils.getTexSettings import GetTexMaketitle
from utils.commonSettings import *
import os
from utils.getVersionInfo import GetReleaseInfo, GetVersionInfo

project = '设计文档'
copyright = '2019, CNLHC'
author = 'CNLHC'
docIndexStr = "003"
docAbbr = "SDD"
htmlhelp_basename = 'shattuckitedoc'

version = GetVersionInfo(docAbbr)
release = GetReleaseInfo(docAbbr)

contributors = [
    {
        'id': '16231275',
        'name': '刘瀚骋',
        # 'work': ''
    },
    {
        'id': '16061053',
        'name': '孟巧岚',
    },
    {
        'id': '16061069',
        'name': '许文广',
    }, {
        'id': "16061044",
        'name': '张起铭',
    }, {
        'id': "16061136",
        'name': "邓健",
    }
]

latex_elements['preamble'] = GetTexMaketitle(
    documentTitle=project, docAbbr=docAbbr, contributors=contributors)

latex_documents = [(master_doc, 'shattuckite-{docAbbr}.tex'.format(docAbbr=docAbbr),
                    'shattuckite {title}'.format(title=project), 'SHADOC-{docIndexStr},SDP,第五组'.format(docIndexStr=docIndexStr), 'howto'), ]
