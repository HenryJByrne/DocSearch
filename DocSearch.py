from nltk.corpus import stopwords
import numpy

def listcreate(file):
    sortedlist = []
    with open(file, "r") as myfile:
        for line in myfile:
            newline = line.replace("\n","")
            removespace = newline.replace("\t"," ")
            split = removespace.split(' ')
            if split[-1] == '':
                split.pop()
            sortedlist.append(split)
    return sortedlist

def dictcreate(docwords):
    dictionary = {}
    for line in docwords:
        for word in line:  
            if word in dictionary:
                dictionary[word] += 1
            else:
                dictionary[word] = 1
    return dictionary


def removewords(wordlist):
    en_stops = set(stopwords.words('english'))
    count = 0
    for line in wordlist[:]:
        for word in line[:]:
            if word in en_stops:
                wordlist[count].remove(word)
        count += 1
    return wordlist

def indexarray(wordslist):
    indexed_array = {}
    for i in range(0,len(wordslist)):
        for word in wordslist[i]:
            if word not in indexed_array:
                indexed_array[word] = [i+1]
            else:
                indexed_array[word].append(i+1)
    return indexed_array

def docsearch(index,queries):
    docs = index.values()
    dictkeys = index.keys()
    reldocs = []
    for line in queries: 
        linecommon = []
        for query in line: 
            queries = []
            for word in dictkeys: 
                if query == word: 
                    queries.extend(index[word]) 
            if len(linecommon) == 0:
                linecommon.extend(queries)
            else:
                linecommon = list(set(queries).intersection(linecommon))
        reldocs.append(linecommon)
    return reldocs

def duplicates(duplicatelist):
    non_duplicate = []
    for line in duplicatelist:
        line = list(dict.fromkeys(line))
        line.sort()
        non_duplicate.append(line)
    return non_duplicate

#def removesimilar(list1,querylist):
#    for i in range(0,len(querylist)):

        

def main():
    three_d_doc = listcreate("C:/Users/henry/OneDrive/Documents/Uni/Year 1/Spring Semester/CM1208 - Maths for Computer Science/Coursework/set2/docs.txt")
    queries = listcreate("C:/Users/henry/OneDrive/Documents/Uni/Year 1/Spring Semester/CM1208 - Maths for Computer Science/Coursework/set2/queries.txt")
    dictionary = dictcreate(three_d_doc)
    nostopwords = removewords(three_d_doc)
    print("Words in dictionary: ",len(dictionary))
    indexed_array = indexarray(nostopwords)
    documents = duplicates(docsearch(indexed_array,queries))
    for i in range(len(queries)):
        reldocs = ""
        for j in range(0,len(documents[i])):
            reldocs += str(documents[i][j])
            reldocs += ' '
        print("Query:",' '.join(queries[i]))
        print("Relevant documents: ",reldocs)
main()

            
    
    
    
