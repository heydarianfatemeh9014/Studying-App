# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['D:\\\\New folder (2) - Copy\\\\main.py'],
    pathex=[],
    binaries=[],
    datas=[('D:\\\\New folder (2) - Copy\\\\calendar_proj.py', '.'), ('D:\\\\New folder (2) - Copy\\\\pomo.py', '.'), ('D:\\\\New folder (2) - Copy\\\\planner_proj.py', '.'), ('D:\\\\New folder (2) - Copy\\\\start_proj.py', '.'), ('D:\\\\New folder (2) - Copy\\\\tips_study.py', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['D:\\New folder (2) - Copy\\photos\\22.ico'],
)
