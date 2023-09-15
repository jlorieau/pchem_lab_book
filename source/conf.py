# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Physical Chemistry Labbook'
copyright = '2023, Chem 343 Instructors'
author = 'Chem 343 Instructors'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.mathjax",
    "sphinx_design",
    "matplotlib.sphinxext.plot_directive",
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]

html_title = "Physical Chemistry Labbook"
# html_logo = "path/to/logo.png"
# html_favicon = "path/to/favicon.ico"

# -- Options for LaTeX output ------------------------------------------------
# https://www.sphinx-doc.org/en/master/latex.html

latex_elements = {
    'preamble': r'''
\usepackage{mhchem}
'''}

# -- Options for plot extension ----------------------------------------------
plot_formats = ['png', 'pdf']
plot_html_show_source_link = False
plot_html_show_formats = False