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
import subprocess
import js2py
from js2py import require

def getIpa(word):
  #Get JSON of word input from API
  response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/"+word)
  print(response.status_code)
  #Open file and download it
  with open('data.json','w', encoding="utf-8", errors='ignore') as f:
      f.write(str(response.text))
      f.close()
  # Open the existing JSON file for loading into a variable
  with open('data.json', 'r', encoding="utf-8", errors='ignore') as jsondata:
    data = json.load(jsondata)
  #Print phonetics from JSON
  try:
    return(data[0]["phonetic"]) 
  except:
    try:
      return(data[0]["phonetics"][1]["text"])
    except:
      response = str(requests.get("http://en.wiktionary.org/w/api.php?action=parse&format=json&prop=text|revid|displaytitle&callback=?&page="+word).content)
      with open('data.html','w', encoding="utf-8", errors='ignore') as f:
        f.write(response)
        f.close()
      with open('data.html', 'r', encoding="utf-8", errors='ignore') as htmldata:
        # read all content of a file
        content = htmldata.read()
        # check if string present in a file
        if "<span class=" in content:
          content = content[content.find("General American"):content.find("General American")+1000]
          content = content[content.find("<span class=\\\\\"IPA\\\\\">")+22:content.find("<span class=\\\\\"IPA\\\\\">")+100]
          content = content[:content.find("</span>")]
          eval_res, jsRunnerFile = js2py.run_file("converter.js")
          #EXAMPLE CODE!!!! WORKING!!!!
          convert = content[content.find("\\")+1:content.find("\\")+7]
          jsRunnerFile.run(convert)
          concatenatedString = ""
          backlog = 0
          for x in range(len(content)):
            if backlog > 0:
              backlog = backlog-1
              continue
            if content[x] == '\\':
              convert = content[x+1:x+7]
              concatenatedString = concatenatedString + jsRunnerFile.run(convert)
              backlog = 6
            else:
              concatenatedString = concatenatedString + content[x]
          return(concatenatedString)
              

        else:
          print('error. not found.')

def run():
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

run()