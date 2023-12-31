import setuptools

setuptools.setup(
    name='volcab_finding',
    version='1.0',
    install_requires=['pandas',
                      'numpy'],
    description='利用自由度和凝合度在文本中尋找可能為單詞的字串',
    author='bananaiselite',
    author_email='dashcamp057@gmail.com',
    packages=setuptools.find_packages(exclude=['example']),
)
