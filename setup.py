from setuptools import setup

setup (
    name='sigma2splunkalert',
    version='0.0.1',
    packages=[''],
    url='',
    license='MIT',
    author='',
    author_email='',
    description='sigma2splunkalert',
    data_files=[
        ('bin/config' , [
            'config/config.yml'
        ]),
        ('bin/templates' , [
            'templates/template'
        ]),
        ('bin/sigma_config' , [
            'sigma_config/splunk-all.yml'
        ]),
        ('bin/classes' , [
            'classes/AlertManager.py',
            'classes/DetectionRuleConverter.py',
            'classes/EMail.py',
            'classes/SummaryIndex.py',
            'classes/TriggeredAlert.py',
            'classes/UseCase.py'
        ])
    ],
    install_requires=['pyYaml','jinja2','sigmatools'],
    scripts=[
        'sigma2splunkalert'
    ]
)
