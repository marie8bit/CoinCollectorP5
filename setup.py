from setuptools import setup

setup(
    name='CoinCollectorP5',
    version='0.1.0',
    author='Marie Erickson',
    author_email='yd7581ku@go.minneapolis.edu',
    packages=['statecoin50', ],

    #50 state quarter progam url='https://www.usmint.gov/learn/coin-and-medal-programs/50-state-quarters',
    #license='LICENSE.txt',
    description='An app that helps you keep track of your 50 state quarters. A coin program by the US Mint',
    long_description=open('README.txt').read(),
    install_requires=['django', 'folium',
    ],
)
