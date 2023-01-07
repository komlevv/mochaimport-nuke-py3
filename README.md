# MochaImport+ for Nuke

This repo is a fork of https://github.com/mamoworld/mochaimport-nuke
rewritten in Python3

### Features:

+ Nuke 13+ support
+ Minor bugfixes
+ Code style fixes

### Notes

* Tested to work with Nuke 14, but no extensive testing was done for the fork. Feel free to submit any bugs you encounter

---------------------------------------------------

## How to install

1) Copy this entire folder somewhere on your hard drive
2) Make sure the folder is included in your NUKE_PATH environment variable

Instead of adding the folder to your NUKE_PATH, you can also add it to the plugin path in
~/.nuke/init.py

---------------------------------------------------

### Example to change init.py on MacOS

Assume you are user JOHN with home directory /Users/JOHN/
and MochaImportPlus is located at /Users/JOHN/myTools/mochaImportPlus
Then

1) Go to the folder /Users/JOHN/.nuke
2) Create the file init.py in this folder if it does not exist yet
3) Add the following line to init.py:
   nuke.pluginAddPath('/Users/JOHN/myTools/mochaImportPlus');

If you now start nuke, MochaImportPlus should be installed.

For more details see
http://docs.thefoundry.co.uk/nuke/63/pythondevguide/installing_plugins.html

