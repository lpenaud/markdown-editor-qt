#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import pypandoc


class Pandoc(object):
    """docstring for Pandoc."""
    def __init__(self, input_format, output_format, **kwargs):
        super(Pandoc, self).__init__()
        self.input_format = input_format
        self.output_format = output_format
        self.template = kwargs.get('template')
        self.lang = kwargs.get('lang')
        self.toc = kwargs.get('toc') == True
        if self.toc:
            self.toc_title = kwargs.get('toc_title')
            if self.toc_title == True and self.lang:
                self._auto_toc_title()
        self.css = kwargs.get('css')
        self.inline_css = kwargs.get('inline_css')

    @property
    def input_format(self):
        return self._input_format

    @input_format.setter
    def input_format(self, input_format):
        if not(input_format in pypandoc.get_pandoc_formats()[0]):
            raise ValueError('{} is not supported like input formats'.format(input_format))
        self._input_format = input_format

    @property
    def output_format(self):
        return self._output_format

    @output_format.setter
    def output_format(self, output_format):
        if not(output_format in pypandoc.get_pandoc_formats()[1]):
            raise ValueError('{} is not supported like output format'.format(output_format))
        self._output_format = output_format

    @property
    def template(self):
        return self._template

    @template.setter
    def template(self, template):
        if template:
            pathname = Path(template).absolute()
            if not(pathname.exists()):
                raise ValueError('{} doesn\'t exists'.format(template))
            self._template = str(pathname)
        else:
            self._template = None

    @property
    def css(self):
        return self._css

    @css.setter
    def css(self, css):
        if css:
            pathname = Path(css).absolute()
            if not(pathname.exists()):
                raise ValueError('{} doesn\'t exists'.format(css))
            self._css = str(pathname)
        else:
            self._css = None

    def _auto_toc_title(self):
        titles = {
            'fr': 'Sommaire',
            'default': 'Table of contents'
        }
        if titles.get(self.lang):
            self.toc_title = titles.get(self.lang)
        else:
            self.toc_title = titles.get('default')

    def _add_var_args(self, name, value):
        return ('-V', '{}={}'.format(name, value))

    def _generate_args(self):
        args = []
        if self.template:
            args.extend(('--template', self.template))
        if self.lang:
            args.extend(self._add_var_args('lang', self.lang))
        if self.toc:
            args.append('--toc')
            if self.toc_title:
                args.extend(self._add_var_args('toc-title', self.toc_title))
        if self.css:
            args.extend(self._add_var_args('css', self.css))
        if self.inline_css:
            args.extend(self._add_var_args('inline-css', self.inline_css))
        return args

    def convert_text(self, text, outputfile = None):
        return pypandoc.convert_text(text, self.output_format, self.input_format, self._generate_args(), 'utf-8', outputfile)

    def convert_file(self, inputfile, outputfile = None):
        pathname = Path(inputfile).absolute()
        if not(pathname.exists()):
            raise ValueError('{} doesn\'t exists'.format(inputfile))
        pypandoc.convert_file(str(pathname), self.output_format, self.input_format, self._generate_args(), 'utf-8', outputfile)


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
