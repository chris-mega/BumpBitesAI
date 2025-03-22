from setuptools import setup

setup(
    name='BumpBitesAI',
    version='0.1',
    description='AI Recipes Recommendations for Pregnancy',
    author='Chris Melendez',
    author_email='chris.melendezg@gmail.com',
    install_requires=[
        'python-dotenv',
        'openai',
        'requests',
        'google-genai',
        'flask',
        'azure-storage-blob',  # Specific Azure SDK for Blob storage
        'azure-identity',  # For authentication
    ],
    py_modules=['ai_recipes', 'models', 'app'],
)
