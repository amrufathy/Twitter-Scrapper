# Twitter Scrapper
A python tool that extracts user data through the [Twitter API](https://dev.twitter.com/overview/documentation) and saves it to excel workbooks.

### TODO
Generate a Source &mdash; Target matrix to model a Social Network

### Dependancies
- Python 2.7 [[link](https://www.python.org/download/releases/2.7.6/)]

- "Python Twitter Tools" was used as a wrapper around the Twitter API:
Source Code: [[link](https://github.com/sixohsix/twitter)]
Installation: [[link](http://mike.verdone.ca/twitter/#install)]

- Openpyxl (v 2.4.0-b1) was used to read/write excel workbooks/sheets:
Documentation: [[link](https://openpyxl.readthedocs.io/en/default/index.html)]
Installation: [[link](https://pypi.python.org/pypi/openpyxl)]

### How to use
1. Enter your Twitter API keys in "settings.py" file
2. Enter the screen names of the users whom you want to extract their data in "usernames.py" file
3. Run "main.py" file to start the program