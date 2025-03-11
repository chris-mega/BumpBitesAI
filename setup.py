from setuptools import setup

setup(
    name='BumpBitesAI',
    version='0.1',
    description='AI Recipes Recommendations for Pregnancy',
    author='Chris Melendez',
    author_email='chris.melendezg@gmail.com',
    install_requires=[
        'openai',
        'requests',
        'google-genai',
        'flask'
    ],
    py_modules=['ai_recipes', 'models']
)
