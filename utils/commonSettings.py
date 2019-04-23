
needs_sphinx = '1.8'
source_suffix = '.rst'
language = 'zh_CN'
html_static_path = ['_static']
templates_path = ['_templates']

latex_engine = 'xelatex'
plantuml = 'java -jar /opt/plantuml.jar -charset UTF-8'
plantuml_output_format = 'svg_obj'
plantuml_latex_output_format = 'pdf'
graphviz_output_format = 'svg'
master_doc = 'index'
pygments_style = None
html_theme = 'sphinx_rtd_theme'
todo_include_todos = True

extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinxcontrib.plantuml',
    'sphinx.ext.graphviz',
    'sphinx.ext.autosectionlabel',
    'sphinxcontrib.bibtex',
]

latex_elements = {
    'papersize': 'a4paper',
    'fncychap': '',
    'extraclassoptions': 'openany,oneside',
    'maketitle': r'''\shattuckitemaketitle
\newpage
    ''',
    'releasename': "版本",
    'fontpkg': r'''
\setmainfont{WenQuanYi Micro Hei Mono}
\setsansfont{WenQuanYi Micro Hei Mono}
\setmonofont{WenQuanYi Micro Hei Mono}
''',
}