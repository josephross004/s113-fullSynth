'''
engIpa.py

Provides interface for translating words to IPA values, using (XXX: Machine Learning) Dictionary API.


Author: Joey Ross
'''

'''
CLASSES
N/A

METHODS
getIpa (string):
  Parameters: 
    word: Pass in a word to be translated.
  Returns: 
    s: string to be displayed.
'''

import requests
import json
import tkinter as tk
import codecs

def getIpa(word):
  #Get JSON of word input from API
  response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/"+word)
  print(response.status_code)
  #Open file and download it
  with open('eng-ipa/data.json','w', encoding="utf-8", errors='ignore') as f:
      f.write(str(response.text))
      f.close()
  # Open the existing JSON file for loading into a variable
  with open('eng-ipa/data.json', 'r', encoding="utf-8", errors='ignore') as jsondata:
    data = json.load(jsondata)
  #Print phonetics from JSON
  try:
    return(data[0]["phonetic"]) 
  except:
    try:
      return(data[0]["phonetics"][1]["text"])
    except:
      response = str(requests.get("http://en.wiktionary.org/w/api.php?action=parse&format=json&prop=text|revid|displaytitle&callback=?&page="+word).content)
      with open('eng-ipa/data.html','w', encoding="utf-8", errors='ignore') as f:
        f.write(response)
        f.close()
      with open('eng-ipa/data.html', 'r', encoding="utf-8", errors='ignore') as htmldata:
        # read all content of a file
        content = htmldata.read()
        # check if string present in a file
        if "<span class=" in content:
          content = content[content.find("General American"):content.find("General American")+1000]
          content = content[content.find("<span class=\\\\\"IPA\\\\\">")+22:content.find("<span class=\\\\\"IPA\\\\\">")+100]
          content = content[:content.find("</span>")]
          convert = content[content.find("\\")+3:content.find("\\")+7]
        else:
          print('error. not found.')

# Top level window
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('400x200')
# Function for getting Input
# from textbox and printing it 
# at label widget
  
def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text = getIpa(inp))

# Text box creation
inputtxt = tk.Text(frame,
                   height = 5,
                   width = 20)
  
inputtxt.pack()
  
# Button creation
printButton = tk.Button(frame,
                        text = "Print", 
                        command = printInput)
printButton.pack()
  
# Label Creation
lbl = tk.Label(frame, text = "")
lbl.pack()
frame.mainloop()

