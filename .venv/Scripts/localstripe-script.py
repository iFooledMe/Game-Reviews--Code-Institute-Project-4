#!d:\repos\game_reviews\.venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'localstripe==1.12.7','console_scripts','localstripe'
__requires__ = 'localstripe==1.12.7'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('localstripe==1.12.7', 'console_scripts', 'localstripe')()
    )
