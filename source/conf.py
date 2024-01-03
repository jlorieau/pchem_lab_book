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

numfig = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_static_path = ['_static', '_static/logos']
html_css_files = [
    'custom.css',
]

html_title = "Physical Chemistry Lab Book"
# html_logo = "path/to/logo.png"
# html_favicon = "path/to/favicon.ico"

html_theme_options = {
    "extra_footer": '<a href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.en">'
                    '<img src="http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-nc-nd.svg" />'
                    ' CC BY-NC-ND 4.0</a>',
    "logo": {"text": "Physical Chemistry Lab Book",
             "image_light": "_static/logos/CAMP.HRZ.SM.RGB.SVG",
             "image_dark": "_static/logos/CAMP.HRZ.SM.INVT.RBG.SVG",
    }
}

html_sidebars = {
    "**": ["navbar-logo.html", "sbt-sidebar-nav.html", "search-field.html"]
}

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