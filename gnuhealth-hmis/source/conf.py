# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'GNU Health Hospital Management'
copyright = '2023, GNU Solidario'
author = 'GNU Solidario'
release = '4.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
        'sphinx.ext.todo',
        'sphinxcontrib.globalsubs',
        'sphinx_toolbox.wikipedia',
        'sphinxcontrib.images'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

todo_include_todos = True
todo_link_only = True

# -- Global Substitutions working with sphinxcontrib.globalsubs --------------
# https://github.com/missinglinkelectronics/sphinxcontrib-globalsubs
# Global substitutions are processed after default substitutions like |release|, |version| and |today|, 
# but before any other substitutions in source files (i.e. global substitutions can be overriden).

global_substitutions = {
    'stub': '.. warning:: This page or section is an undeveloped draft or outline.',
    'version3.4': '.. important:: This section applies to version **3.4** of **GNU Health**.',
    'version3.6': '.. important:: This section applies to version **3.6** of **GNU Health**.',
    'version3.0': '.. important:: This section applies to version **3.0** of **GNU Health**.',
    'todo': '.. todo:: To be added'
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_sidebars = { '**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html']}
