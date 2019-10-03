import random
import Tkinter
import webbrowser

#
# Probelm
# Google has a restriction to not copy any content to the clipboard which showed in the top most bar
# (i.e photos and names) i call it as list bar. So i Opened the concole and copied the div tag and coliped
# it in empty web page and opend it. Volla i was able to copy all the content in a easy and
# It is going to be every useful for knowledge improvement. For to do all the manual work it is tough
# i created a script which does this i open a web and copy it and runs the scirpt it will
# create a temp directory and using a small template to genreate html and other tage and opens it in the chrome.
# From where i can copy it and save it to evernote. I can clean the code for now i am just keeping as it is
#

# File Properties
FILE_EXTENSION = ".html"
FILE_PREFIX = "temp"
FILE_DESTINATION = "/Users/syakka/Downloads/"

# Web Broswer file prefix
WEBBROWSER_FILE_PREFIX = "file://"



def getRandomFileName():
    return FILE_DESTINATION + FILE_PREFIX + str(random.randint(1, 120)) + FILE_EXTENSION;

def getClipboardContent():
    root = Tkinter.Tk()
    root.withdraw()
    text_in_clipboard = root.clipboard_get()
    return text_in_clipboard

def getFileContent():

    head = """<!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>""""""
    </head>
        <body>
    """

    tail="""
        </body>
            </html>
    """

    body = getClipboardContent()

    return head+body+tail

def createFileAndOpenFileInBrowser():
    randomFileName = getRandomFileName()
    fileContent = getFileContent()

    with open(randomFileName,'w+') as file :
        file.write(fileContent)

    webbrowser.open_new_tab(WEBBROWSER_FILE_PREFIX + randomFileName)

createFileAndOpenFileInBrowser()
