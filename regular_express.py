# Meta Characters
# [] A set of characters
# \ Signals a special sequence (can also be used to escape special characters)
# . Any character (except newline character)
# ^ Starts with
# $ Ends with
# * Zero or more occurrences
# + One or more occurrences
# {} Exactly the specified number of occurrences
# | Either or
# () Capture and group

# Special Sequences
# \A Returns a match if the specified characters are at the beginning of the string
# \b Returns a match where the specified characters are at the beginning or at the end of a word r” ain\b.”
# \B Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
#
# \d Returns a match where the string contains digits (numbers from 0-9)
# \D Returns a match where the string DOES NOT contain digits
# \s Returns a match where the string contains a white space character
# \S Returns a match where the string DOES NOT contain a white space character
# \w Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
# \W Returns a match where the string DOES NOT contain any word characters
# \Z Returns a match if the specified characters are at the end of the string

import re

mystr='''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiinaiiiiiiiiiiin
parthibdutta02@gmail.com'''
# Functions-->findall,search,split,sub,finditer

print(r'\n')
patt=re.compile(r'fass')
patt=re.compile(r'.')
patt=re.compile(r'.adm')
patt=re.compile(r'^Tata')
patt=re.compile(r'iiiiiiin$')
patt=re.compile(r'ai*')
patt=re.compile(r'ai+')
patt=re.compile(r'ai{2}')
patt=re.compile(r'(ai){2}')
patt=re.compile(r'ai{1} | t')

#Special Sequence
# patt=re.compile(r'\ATata')
#patt=re.compile(r'\bFax')
#patt=re.compile(r'Fax\b')
# patt=re.compile(r'\d{5}-\d{4}')
#
# matches=patt.finditer(mystr)
# for i in matches:
#     print(i)
#     #print(mystr[448:452])


# Regex Email Editer-->
# email=re.findall(r"[0-9a-zA-Z.+_%]+@[0-9a-zA-Z.+_%]+[.][a-zA-Z0-9.]+",mystr)
# email=re.findall(r"\w+@\S+\w",mystr)
# print(email)

# emai=re.findall(r"\W",mystr)
# print(emai)