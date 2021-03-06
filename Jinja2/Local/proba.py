# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 22:40:58 2017

@author: sonGhenG
"""

import os
from jinja2 import Environment, FileSystemLoader
from configparser import SafeConfigParser

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
        autoescape=False,
        loader=FileSystemLoader(os.path.join(PATH,'templates')),
        trim_blocks=False)
config = SafeConfigParser()
config.read(r'G:\Python\configparser\tomorrow.ini')

def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)
    
def create_index_html():
    fname = "output.html"
    urls = config.get('URL','urls')
    context = {
            'urls': urls
    }
    
    with open(fname, 'w') as f:
        html = render_template('index.html', context)
        f.write(html)
        
def main():
    create_index_html()
    
if __name__ == "__main__":
    main()
    
    