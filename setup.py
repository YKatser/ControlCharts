from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='ControlCharts',
    url='https://github.com/YKatser/ControlCharts',
    author='Iurii Katser',
    author_email='waico@waico.ru',
    # Needed to actually package something
    packages=['ControlCharts'],
    # Needed for dependencies
    install_requires=['math','os','matplotlib','numpy','sklearn','scipy','pandas'],
    # *strongly* suggested for sharing
    version='1.0.0',
    # The license can be anything you like
    license='MIT',
    description='Control charts for process monitoring and anomaly detection',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.md').read(),
)