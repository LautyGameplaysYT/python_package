import setuptools


with open("readme.md","r",encoding="utf-8") as f:
    more_description = f.read()
setuptools.setup(
    name = 'Lauty_utilities',
    version = '0.0.1',
    author = 'LautyGameplaysYT',
    author_email= 'private',
    more_description = more_description,
    more_description_content_type = "text/markdown",
    url='https://github.com/LautyGameplaysYT/python_package',
    project_urls = {
        "Bug Tracker": "https://github.com/LautyGameplaysYT/python_package/issues"
    },
    license= "GNU-3.0",
    packages= ['Lauty_utilities'],
    install_requires = []
)