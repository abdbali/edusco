from setuptools import setup, find_packages

setup(
    name='edusco',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'ipywidgets',
        'spellchecker',  # Eğer yazım düzeltme eklersen
    ],
    python_requires='>=3.8',
)
