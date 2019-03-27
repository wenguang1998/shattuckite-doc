import os
import re
import subprocess
import datetime
import json
import requests
import m2r
project = 'shattuckite-requirements'
copyright = '2019, CNLHC'
author = 'CNLHC'
version = '0.0'
release = release = re.sub('^v', '', os.popen('git describe').read().strip())
needs_sphinx = '1.8'
extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinxcontrib.plantuml',
    'sphinx.ext.graphviz',
    'sphinx.ext.autosectionlabel',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = 'zh_CN'
exclude_patterns = []
pygments_style = None
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
htmlhelp_basename = 'shattuckite-requirementsdoc'
latex_engine = 'xelatex'
latex_documents = [
    (master_doc, 'shattuckite-requirements.tex', 'shattuckite 需求文档', 
    'SHADOC-002,SDP,第五组', 'howto'),
]
plantuml = 'java -jar /opt/plantuml.jar -charset UTF-8'
plantuml_output_format = 'svg_obj'
plantuml_latex_output_format = 'pdf'
graphviz_output_format = 'svg'

#######版本修订记录自动生成
SHADOC_INDEX = '002'
SHADOC_REGEX_PATTERN = re.compile(
    r"^commit(.*?)$\nAuthor:(.*?)$\nDate:(.*?)$\s+SHADOC-{0:s}\sDOC\sUPDATE\s+AUTHOR:(.*?)\s+CENSOR:(.*?)\s+NOTE:(.*?)$".format(SHADOC_INDEX), re.S | re.M)
SHADCommitList = []

with subprocess.Popen(['git', 'log', '--grep', 'SHADOC-{0:s} DOC UPDATE'.format(SHADOC_INDEX)], stdout=subprocess.PIPE) as proc:
    result = (re.findall(SHADOC_REGEX_PATTERN, proc.stdout.read().decode()))
    for i in result:  # type:str
        res = {}
        dateString  = re.sub('\+\d+', '', i[2]).rstrip().lstrip()
        res['Hash'] = i[0].lstrip()
        res['GithubAuthor'] = i[1].lstrip()
        print(dateString)
        res['Date'] = datetime.datetime.strptime(dateString, '%a %b %d %H:%M:%S %Y').strftime('%Y-%m-%d %H:%M')
        res['Author'] = i[3].lstrip()
        res['Censor'] = i[4].lstrip()
        res['Note'] = i[5].lstrip()
        with subprocess.Popen(['git', 'describe', res['Hash']], stdout=subprocess.PIPE) as proc2:
            res['Version'] = proc2.stdout.read().decode()
        SHADCommitList.append(res)

RevHistoryLatexCell = ''
for commit in SHADCommitList:
    RevHistoryLatexCell += '\n{0:s}&      {1:s}&       {2:s}&     {3:s}&  {4:s}    \\\ \hline\n'.format(
        commit['Version'],
        commit['Date'],
        commit['GithubAuthor'],
        commit['Censor'],
        commit['Note'])

#
# #####任务列表自动生成
# AutoTaskListMDBuf=''
# AutoTaskListTemplate='''### {title}
# 成员:{smember}
# {body}
# '''
# with open('./plan/issue.rst','w',encoding='utf8') as rstfp:
#     issues=json.loads(requests.get('https://api.github.com/repos/buaaembeddedse/shattuckite-META/issues?state=all').text)
#     # issues=json.loads(fp.read())
#     for issue  in issues:
#         memberList=','.join([i['login'] for i in issue['assignees']])
#         AutoTaskListMDBuf+=AutoTaskListTemplate.format(**issue,smember=memberList)
#
#     rstfp.write(m2r.convert(AutoTaskListMDBuf))

latex_elements = {
    'papersize': 'a4paper',
    'fncychap': '',
    'figure_align': 'H',
    'extraclassoptions': 'openany,oneside',
    'maketitle': r'''\shattuckitemaketitle
\newpage
    ''',
    'releasename': "版本",
    'preamble': r'''\usepackage{ctex}
\newcommand{\shattuckitemaketitle}{%
\maketitle
\makeMetaPage
}
\makeatletter
\def\@maketitle{%
  \newpage
  \null
  \vskip 2em%
  \begin{center}%
  \let \footnote \thanks
    {\zihao{-0} Shattuckite \par}%
    \vskip 1.5em%
    {\zihao{-0} 需求文档 \par}
    \vskip 5.5em%
    {\large
      \lineskip .5em%
      \begin{tabular}[t]{c}%
        \zihao{4}\@author
      \end{tabular}\par}%
    \vskip 1em%
      {\heiti\zihao{4}\itshape\py@release \releaseinfo}\par
    %{\large \@date}%
  \end{center}%
  \par
  \vskip 1.5em}
\makeatother
\newcommand{\makeMetaPage}{
\newpage
\begin{table}[]
\caption {\heiti 版本变更历史} \label{tab:title}
\centering
\begin{tabular}{|l|p{2cm}|p{4cm}|l|p{5cm}|}
\hline
版本 & 提交日期 & 主要编制人 & 审核人 & 版本说明 \\ \hline
'''+RevHistoryLatexCell+r'''
\end{tabular}
\end{table}
\clearpage
}'''
}
texinfo_documents = [
    (master_doc, 'shattuckite', 'shattuckite 需求文档',
     author, 'shattuckite', 'shattuckite 物联网开发框架',
     'Miscellaneous'),
]
todo_include_todos = True
