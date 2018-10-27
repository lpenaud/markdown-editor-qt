#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import pypandoc
import helpers


class Pandoc(object):
    """docstring for Pandoc."""
    def __init__(self, input_format, output_format, **kwargs):
        self.input_format = input_format
        self.output_format = output_format
        self.template = kwargs.get('template')
        self.toc = kwargs.get('toc') == True
        self.toc_title = kwargs.get('toc_title')
        self.lang = kwargs.get('lang')
        self.css = kwargs.get('css')
        self.inline_css = kwargs.get('inline_css')

    @property
    def input_format(self):
        return self.__input_format

    @input_format.setter
    def input_format(self, input_format):
        if not(input_format in pypandoc.get_pandoc_formats()[0]):
            raise ValueError('{} is not supported like input formats'.format(input_format))
        self.__input_format = input_format

    @property
    def output_format(self):
        return self.__output_format

    @output_format.setter
    def output_format(self, output_format):
        if not(output_format in pypandoc.get_pandoc_formats()[1]):
            raise ValueError('{} is not supported like output format'.format(output_format))
        self.__output_format = output_format

    @property
    def template(self):
        return self.__template

    @template.setter
    def template(self, template):
        if template:
            pathname = Path(template).absolute()
            if not(pathname.exists()):
                raise ValueError('{} doesn\'t exist'.format(template))
            self.__template = str(pathname)
        else:
            self.__template = None

    @property
    def css(self):
        return self.__css

    @css.setter
    def css(self, css):
        if css:
            pathname = Path(css).absolute()
            if not(pathname.exists()):
                raise ValueError('{} doesn\'t exists'.format(css))
            self.__css = str(pathname)
        else:
            self.__css = None

    @property
    def toc_title(self):
        return self.__toc_title

    @toc_title.setter
    def toc_title(self, toc_title):
        if toc_title == True:
            self.auto_toc_title()
        elif type(toc_title) is str:
            self.__toc_title = toc_title
        else:
            self.__toc_title = None

    @property
    def lang(self):
        return self.__lang

    @lang.setter
    def lang(self, lang):
        self.__lang = lang
        self.auto_toc_title()

    def auto_toc_title(self):
        if self.toc and self.lang:
            titles = {
                'fr': 'Sommaire',
                'default': 'Table of contents'
            }
            if titles.get(self.lang):
                self.__toc_title = titles.get(self.lang)
            else:
                self.__toc_title = titles.get('default')

    def __add_var_args(self, name, value):
        return ('-V', '{}={}'.format(name, value))

    def __generate_args(self):
        args = []
        if self.template:
            args.extend(('--template', self.template))
        if self.lang:
            args.extend(self.__add_var_args('lang', self.lang))
        if self.toc:
            args.append('--toc')
            if self.toc_title:
                args.extend(self.__add_var_args('toc-title', self.toc_title))
        if self.css:
            args.extend(self.__add_var_args('css', self.css))
        if self.inline_css:
            args.extend(self.__add_var_args('inline-css', self.inline_css))
        return args

    def convert_text(self, text, outputfile=None):
        return pypandoc.convert_text(text, self.output_format, self.input_format, self.__generate_args(), 'utf-8', outputfile)

    def convert_file(self, inputfile, outputfile=None):
        pathname = Path(inputfile).absolute()
        if not(pathname.exists()):
            raise ValueError('{} doesn\'t exists'.format(inputfile))
        pypandoc.convert_file(str(pathname), self.output_format, self.input_format, self.__generate_args(), 'utf-8', outputfile)

    def read_config(self, config):
        self.input_format = config['format']['input']
        self.output_format = config['format']['output']
        self.template = Path(*config['template']).absolute()
        if config['lang'] == 'SYSTEM':
            self.lang = helpers.get_lang()
        else:
            self.lang = config['lang']
        self.inline_css = Path(*config['css']['inline']).read_text(encoding='utf8')
        self.toc = config['toc']['toc']
        self.toc_title = config['toc']['title']



def main():
    extra_args = {
        'template': str(Path.joinpath(Path.cwd(), 'template', 'default.html')),
        'lang': 'en',
        'inline_css': Path.joinpath(Path.cwd(), 'template', 'default.css').read_text()
    }
    src = '# This is a h1'
    pandoc = Pandoc('markdown', 'html5', **extra_args)
    print(pandoc.convert_text(src))

if __name__ == '__main__':
    main()
