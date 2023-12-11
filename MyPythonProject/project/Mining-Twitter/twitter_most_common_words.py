import sys,re,string,json 
from collections import Counter
from nltk.corpus import stopwords

punctuation = list(string.punctuation)
stop=stopwords.words('english') + punctuation + ['rt','via']
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [ 
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]

tokens_re = re.compile(r'('+'|'.join(regex_str)+')',re.VERBOSE | re.IGNORECASE)
emoticons_str = re.compile(r'^'+emoticons_str+'$',re.VERBOSE | re.IGNORECASE)

def tokenize(s):
    return tokens_re.findall(s)

def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticons_str.search(token) else token.lower() for token in tokens]
    return tokens

if __name__=='__main__':
    fname=sys.argv[1]
    with open(fname,'r') as f:
        count_all=Counter()
        for line in f:
            tweet=json.loads(line)
            tokens = preprocess(tweet['text'])
            print(type(tokens))