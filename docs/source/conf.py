# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
project = 'kiu-test'
copyright = '2025, tomas nardi'
author = 'tomas nardi'
release = '0.1'

# -- Path setup --------------------------------------------------------------
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',     
    'sphinx.ext.napoleon',   
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'furo'
html_static_path = ['_static']
