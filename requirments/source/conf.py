
import sys
sys.path.append('../../')
import re
import requests
from utils.getTexSettings import GetTexMaketitle
from utils.commonSettings import *
import os
from utils.getVersionInfo import GetReleaseInfo, GetVersionInfo

project = '需求文档'
copyright = '2019, CNLHC'
author = 'CNLHC'
docIndexStr = "002"
docAbbr = "SRS"
htmlhelp_basename = 'shattuckitedoc'

version = GetVersionInfo(docAbbr)
release = GetReleaseInfo(docAbbr)

contributors = [
    {
        'id': '16231275',
        'name': '刘瀚骋',
        'work': '1, 2, 3.1, 3.2, 4, 5, 6节内容编写/自动化工具编写/文档校对与评审'
    },
    {
        'id': '16061053',
        'name': '孟巧岚',
        'work': '3.3节内容编写(不包括UML绘制)',
    },
    {
        'id': '16061069',
        'name': '许文广',
        'work': '2,3.3 节UML绘制'
    }, {
        'id': "16061044",
        'name': '张起铭',
        'work': '可持续部署实现'

    }, {
        'id': "16061136",
        'name': "邓健",
        "work": "文档校对与评审 ",
    }
]

latex_elements['preamble'] = GetTexMaketitle(
    documentTitle=project, docAbbr=docAbbr, contributors=contributors)

latex_documents = [(master_doc, 'shattuckite-{docAbbr}.tex'.format(docAbbr=docAbbr),
                    'shattuckite {title}'.format(title=project), 'SHADOC-{docIndexStr},SRS,第五组'.format(docIndexStr=docIndexStr), 'howto'), ]
