from nltk.corpus import stopwords
from nltk.stem.porter import *
from nltk.stem import WordNetLemmatizer

def isInt(k):
    """
    :param k: k is a char
    :return: return ture if the char is a int, return false if the char is not a int
    """
    try:
        int (k)
        return True
    except ValueError:
        return False


def dropStopWords(content):
    """
    :param content: raw text content
    :return: an array drop the stop words
    """
    stop = set(stopwords.words('english'))

    return [i for i in content.lower().split() if i not in stop]


def stemming(content):
    """
    :param content: raw text content
    :return: a text after the stemming process
    """
    steemer = PorterStemmer()
    stringcontent = ""
    stringcontent = steemer.stem(content)
    return stringcontent


def Lemmatizer(content):
    """
    :param content: raw text content
    :return: a text after the lemmatizer process
    """
    wordnet_lemmatizer = WordNetLemmatizer()
    stringcontent = ""
    stringcontent = wordnet_lemmatizer.lemmatize(content)
    return stringcontent




def getArrays(filename):
    """
    :param filename: give a text file name
    :return: return an array, each entry contain a line of text
    """
    inputStream = readIn(filename)
    return breakByLine(inputStream)

def readIn(filename):
    """
    :param filename:  give a text file name
    :return:  return a buffer with textfile's content in it
    """
    filePath = filename
    buffer = ''
    buffer += open(filePath, 'rU').read()
    return buffer

def breakByLine(stream):
    """
    :param stream: text content store in the buffer
    :return:    an array, each entry contain a line of text
    """
    lineArray = str.splitlines(stream)
    return lineArray



def readIn(filename):
    filePath = filename
    buffer = ''
    buffer += open(filePath, 'rU').read()
    return buffer


# break the string into the tokens
def tokenlize(stream):
    tokenArray = str.split(stream)
    return tokenArray


# give name of the file and return a token array
def getToken(filename):
    tokenArray = readIn(filename)
    return tokenlize(tokenArray)



def write_into_file_newline(array, filename):
    write_into_file(array,filename,'\n')

def write_into_file_tab(array,filename):
    write_into_file(array, filename, '\t')

def write_into_file_space(array,filename):
    write_into_file(array, filename, ' ')

def write_into_file(array, filename, separate):
    f = open(filename,"w")

    for x in array:
        f.write(x)
        f.write(separate)

    f.close()

