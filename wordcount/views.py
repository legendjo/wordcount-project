from django.http import HttpResponse
from django.shortcuts import render
import operator   # to use operator

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    wordlistdic = {}                      #Initialize wordlistdictionary to an empty dictionary

    for word in wordlist:                 # iterate/loop through the wordlist
        if word in wordlistdic:           # check if a particular word is already in the wordlistdictionary
           wordlistdic[word] += 1         #Increment the wordcount by 1 if it is already in wordlistdictionary

        else:
            # Add to the dictionary if word is not in dictionary
            wordlistdic[word] = 1

    sortedlist = sorted(wordlistdic.items(), key=operator.itemgetter(1), reverse=True)  # covert wordlistdic to list & sort the new wordlist                                                                   # convert the wordlistdic to list using .items()
    return render(request, 'count.html', {'fulltext' : fulltext, 'wordcount': len(wordlist), 'sortedlist':sortedlist})

def about(request):
    return render(request, 'about.html')
