import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ProjectName'
copyright = '2024, CompanyName'
author = 'CompanyName'

# Версия документации
version = '0.1.0'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

language = 'ru'

# Расширения Sphinx
extensions = [
    'myst_parser',
    'sphinxcontrib.mermaid',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',  # или 'sphinx.ext.imgmath'
    'sphinx_simplepdf'
]

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

# Пути к шаблонам
templates_path = ['_templates']

# Исключаемые паттерны
exclude_patterns = []

# Тема HTML
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

source_suffix = {
   '.rst': 'restructuredtext',
   '.md': 'markdown',
}

myst_enable_extensions = [
    "dollarmath",  # Включает поддержку формул в двух долларах
]

mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"


mermaid_params = [
   '--theme', 'forest',  # Устанавливает тему для диаграмм
   '--width', '100%',    # Устанавливает ширину диаграмм
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Настройка для генерации PDF
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'preamble': '',
    'figure_align': 'htbp',
}

# Основной документ (обычно это 'index')
master_doc = 'index'

latex_documents = [
    (master_doc, f'{project}.tex', f'{project} Documentation',
     author, 'manual'),
]