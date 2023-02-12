from setuptools import setup

APP = ['total_money.py']
OPTIONS = {
    'argv_emulation': False,
    'iconfile': 'money.icns'
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    name='Total Money'
)
