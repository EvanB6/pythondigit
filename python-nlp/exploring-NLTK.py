import nltk
import nltk.corpus
# The next line downloads all the example texts used in the NLTK book at https://www.nltk.org/book !
# You can comment out the download line after the first time you do it.
nltk.download('book')
from nltk.book import *
# The next line lets us do GET requests from remote URLs on the web:
from urllib import request
# The following import lines are for plotting interactive visualizations in Python
import matplotlib
import matplotlib.pyplot as plt

# These imports will let us make a simple tkinter user input / output interface:
import tkinter as tk
from tkinter import scrolledtext
import io
import sys

# Little test for Tkinter from https://realpython.com/ref/stdlib/tkinter/
# So, here's a tiny Python function:
def on_button_click():
    print("Button toggled!")
    number = input("Pick a number!")
    text="*@*\n"
    print(text * int(number))
root = tk.Tk()
root.title("Hello World!") 
label = tk.Label(root, text="Go ahead! Click the button!")
label.pack()
# Make a Tkinter button give it "Click Me" text, and on clicking, trigger the function above.
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()
# The next command generates the little tkinter interface as a little pop-up.
root.mainloop()

plt.plot(range(10))
plt.show()

### See how these words are dispersed in NLTK text 1 (Moby Dick)
words = ["whale", "sea", "ship", "captain"]
nltk.draw.dispersion_plot(text1, words)
plt.show()

# Another dispersion plot written closer to the NLTK example:
# Choose the text first (text 4 is Inaugural Addresses):
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
plt.show()

text6.common_contexts(["find","seek"])

text6.similar('grail')

# Blithedale Romance text file on Project Gutenberg
bookurl= "https://www.gutenberg.org/cache/epub/2081/pg2081.txt"
response = request.urlopen(bookurl)
br = response.read().decode('utf8')
# type(br)
# print(len(br))
# make a variable
# howLong = len(br)
# picture string version! 
# print(f"howLong = {howLong}")
# novelSlice = br[:500]
# print(f"novelSlice = {novelSlice}")

splitEmUp = br.split()
print(f"splitEmUp = {splitEmUp[-100:]}")

for token in splitEmUp:
    if token.endswith('ing'):
        print(token)



# Create an NLTK Text object from the Blithedale Romance file in the previous cell.
# We'll start with splitEmUp (our tokenized version of the text)

blithedaleTextObject = nltk.Text(splitEmUp)
print(f"blithedaleTextObject = {blithedaleTextObject}")

# Now we can run thinks like NLTK's **similar** and **common_context** functions
blithedaleTextObject.similar("veil")


localFile = open("xml-to-text-for-python/casablanca-ck.txt", 'r', encoding='utf-8')
casablanca = localFile.read()
localFile.close()

# print(f"casablanca = {casablanca}")

# We have to split the file into tokens to prepare it for NLTK:
casaTokens = casablanca.split()
# this text has a lot of block cap words, so let's lower-case them:
lowerCaseTokens = [w.lower() for w in casaTokens]
print(f"lowerCaseTokens = {lowerCaseTokens}")

casaTextObject = nltk.Text(lowerCaseTokens)
print(casaTextObject)