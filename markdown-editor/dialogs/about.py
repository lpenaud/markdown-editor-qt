#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.Qt import QDialog, QVBoxLayout, QLabel, QPixmap, QTextEdit, QDialogButtonBox
from PyQt5.QtCore import Qt
from pathlib import Path
import helpers

class About(object):
    """docstring for About."""
    def __init__(self, parent = None, **kwargs):
        super(About, self).__init__()
        self.parent = parent

        self.__labelsKeys = ('logo','programName','version','comments','website','copyright','license',)
        self.__labels = {
            'website': {},
            'license': {}
        }
        self.copyright = kwargs.get('copyright', '')
        self.programName = kwargs.get('programName', '')
        self.version = kwargs.get('version', '')
        self.website = kwargs.get('website', '')
        self.websiteLabel = kwargs.get('websiteLabel', '')
        self.comments = kwargs.get('comments', '')
        self.logo = kwargs.get('logo', '')
        self.licenseUrl = kwargs.get('licenseUrl', '')
        self.licenseName = kwargs.get('licenseName', '')

        self.__creditsKeys = ('authors','documenters','artists','dependencies',)
        self.__credits = {
            'authors': {
                'label': 'Created by'
            },
            'artists': {
                'label': 'Graphics by'
            },
            'documenters': {
                'label': 'Documented by'
            },
            'dependencies': {
                'label': 'This projet use'
            }
        }
        self.authors = kwargs.get('authors', [])
        self.artists = kwargs.get('artists', [])
        self.documenters = kwargs.get('documenters', [])
        self.dependencies = kwargs.get('dependencies', [])

    def exec_(self):
        dialog = QDialog(self.parent)
        textEdit = QTextEdit(dialog)
        buttonBox = QDialogButtonBox(dialog)
        layout = QVBoxLayout(dialog)
        labels = []
        html = ''
        width = 400
        height = 25

        def triggeredCredit():
            if textEdit.isVisible():
                for i in range(2 if self.logo else 1, len(labels)):
                    labels[i].show()
                textEdit.hide()
            else:
                for i in range(2 if self.logo else 1, len(labels)):
                    labels[i].hide()
                textEdit.show()

        def triggeredClose(arg):
            dialog.close()

        dialog.setWindowTitle('About {}'.format(self.programName))

        for key in self.__labelsKeys:
            value = self.__labels.get(key)
            if value:
                label = QLabel(dialog)
                label.setAlignment(Qt.AlignCenter)
                if key == 'website' or key == 'license':
                    label.setText('<a href="{}">{}</a>'.format(
                        value['url'],
                        value['label'] if value['label'] else value['url']
                    ))
                    label.setTextFormat(Qt.RichText)
                    label.setTextInteractionFlags(Qt.TextBrowserInteraction)
                    label.setOpenExternalLinks(True)
                elif key == 'logo':
                    image = QPixmap(self.logo)
                    label.setPixmap(image.scaled(128,128))
                else:
                    label.setText(value)
                labels.append(label)
                layout.addWidget(labels[len(labels) - 1])

        for key in self.__creditsKeys:
            value = self.__credits.get(key)
            if len(value.get('contributors')) > 0:
                html += '<p><strong>{}</strong><br />{}</p>'.format(
                    value.get('label'),
                    '<br />'.join(value.get('contributors'))
                )
        if html:
            textEdit.setHtml('<center>{}</center>'.format(html))
            layout.addWidget(textEdit)
            buttonBox.addButton('Credits', QDialogButtonBox.YesRole).clicked.connect(triggeredCredit)
        textEdit.close()
        textEdit.setReadOnly(True)

        buttonBox.addButton('Close', QDialogButtonBox.NoRole).clicked.connect(triggeredClose)
        layout.addWidget(buttonBox)

        dialog.setLayout(layout)
        height *= len(dialog.children())
        if self.logo:
            height += 128
        dialog.setFixedSize(width, height)
        return dialog.exec_()

    @property
    def artists(self):
        return self.__credits['artists']['contributors']

    @artists.setter
    def artists(self, artists):
        typeArtists = type(artists)
        if typeArtists is tuple:
            self.__credits['artists']['contributors'] = list(artists)
        elif typeArtists is list:
            self.__credits['artists']['contributors'] = artists
        else:
            helpers.raise_type_error('artists', ('tuple','list',), typeArtists)

    @property
    def authors(self):
        return self.__credits['authors']['contributors']

    @authors.setter
    def authors(self, authors):
        typeAuthors = type(authors)
        if typeAuthors is tuple:
            self.__credits['authors']['contributors'] = list(authors)
        elif typeAuthors is list:
            self.__credits['authors']['contributors'] = authors
        else:
            helpers.raise_type_error('authors', ('tuple','list',), typeAuthors)

    @property
    def documenters(self):
        return self.__credits['documenters']['contributors']

    @documenters.setter
    def documenters(self, documenters):
        typeDocumenters = type(documenters)
        if typeDocumenters is tuple:
            self.__credits['documenters']['contributors'] = list(documenters)
        elif typeDocumenters is list:
            self.__credits['documenters']['contributors'] = documenters
        else:
            helpers.raise_type_error('documenters', ('tuple','list',), typeDocumenters)

    @property
    def dependencies(self):
        return self.__credits['dependencies']['contributors']

    @dependencies.setter
    def dependencies(self, dependencies):
        typeDependencies = type(dependencies)
        if typeDependencies is tuple:
            self.__credits['dependencies']['contributors'] = list(dependencies)
        elif typeDependencies is list:
            self.__credits['dependencies']['contributors'] = dependencies
        else:
            helpers.raise_type_error('dependencies', ('tuple','list',), typeDocumenters)

    @property
    def comments(self):
        return self.__labels['comments']

    @comments.setter
    def comments(self, comments):
        typeComments = type(comments)
        if not(typeComments is str):
            helpers.raise_type_error('comments', 'str', typeComments)
        self.__labels['comments'] = comments

    @property
    def copyright(self):
        return self.__labels['copyright']

    @copyright.setter
    def copyright(self, copyright):
        typeCopyright = type(copyright)
        if not(typeCopyright is str):
            helpers.raise_type_error('copyright', 'str', typeCopyright)
        self.__labels['copyright'] = copyright

    @property
    def licenseName(self):
        return self.__labels['license']['label']

    @licenseName.setter
    def licenseName(self, licenseName):
        typeLicenseName = type(licenseName)
        if not(typeLicenseName is str):
            helpers.raise_type_error('copyright', 'str', typeCopyright)
        self.__labels['license']['label'] = licenseName

    @property
    def licenseUrl(self):
        return self.__labels['license']['url']

    @licenseUrl.setter
    def licenseUrl(self, licenseUrl):
        typeLicenseUrl = type(licenseUrl)
        if not(typeLicenseUrl is str):
            helpers.raise_type_error('licenseUrl', 'str', typeCopyright)
        self.__labels['license']['url'] = licenseUrl

    @property
    def logo(self):
        return self.__labels['logo']

    @logo.setter
    def logo(self, logo):
        if type(logo) is str and len(logo) > 0:
            logop = Path(logo).absolute()
            if not(logop.exists()):
                raise ValueError('{} not exists'.format(str(logop)))
            self.__labels['logo'] = str(logop)
        else:
            self.__labels['logo'] = logo

    @property
    def programName(self):
        return self.__labels['programName']

    @programName.setter
    def programName(self, programName):
        typeProgramName = type(programName)
        if not(typeProgramName is str):
            helpers.raise_type_error('programName', 'str', typeProgramName)
        self.__labels['programName'] = programName

    @property
    def version(self):
        return self.__labels['version']

    @version.setter
    def version(self, version):
        typeVersion = type(version)
        if not(typeVersion is str):
            helpers.raise_type_error('version', 'str', typeVersion)
        self.__labels['version'] = version

    @property
    def website(self):
        return self.__labels['website']['url']

    @website.setter
    def website(self, website):
        typeWebsite = type(website)
        if not(typeWebsite is str):
            helpers.raise_type_error('website', 'str', typeWebsite)
        self.__labels['website']['url'] = website

    @property
    def websiteLabel(self):
        return self.__labels['website']['label']

    @websiteLabel.setter
    def websiteLabel(self, websiteLabel):
        typeWebsiteLabel = type(websiteLabel)
        if not(typeWebsiteLabel is str):
            helpers.raise_type_error('websiteLabel', 'str', typeWebsiteLabel)
        self.__labels['website']['label'] = websiteLabel
