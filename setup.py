import setuptools

setuptools.setup(
    name='volcab_finding',
    version='1.0',
    author='bananaiselite',
    author_email='dashcamp057@gmail.com',
    description='利用自由度和凝合度在文本中尋找可能為單詞的字串',
    packages=setuptools.find_packages(),
    packages=['volcab_finding'],
    entry_points={
        'console_scripts': [
            'volcab_finding = volcab_finding.main:main'
        ]}
)
