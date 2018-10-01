# -*- mode: python -*-

import site

block_cipher = None

added_files = [
    ('README.rst', '.'),
    ('LICENSE', '.'),
    ('example', 'example'),
    ('template', 'template')
]

a = Analysis(['markdown-editor/__main__.py'],
             pathex=[],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          icon='',
          exclude_binaries=True,
          name='Markdown-Editor',
          debug=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='Mardown-Editor')
