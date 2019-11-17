import itertools
def algo(letters, pattern, wordsize,flag):
    with open('sowpods.txt') as f:
        good_words=set(x.strip().lower() for x in f.readlines())
    word_set = set()
    for l in range(3,wordsize+1):
        for word in itertools.permutations(letters,l):
            w="".join(word)
            if w in good_words:
                print('YEEE SYFAKDFJALDKFJLKSFJ')
                if len(pattern)>0 and len(w)==len(pattern):
                    if(compare(w,pattern)==True):
                        word_set.add(w)
                elif len(w)==wordsize and len(pattern)==0 and flag=="-reg":
                    word_set.add(w)
                elif flag=="-all":
                    word_set.add(w)
    #return render_template('wordlist.html',wordlist=sorted(word_set),name="CS4131")
    return word_set
def algo2(letters, pattern, word):
    return "hi"

def compare( word, option):
    i=0
    for char in option:
        if ord(char)==ord("."):
            i=i+1
            continue
        else:
            if ord(char)==ord(word[i]):
                i=i+1
            else:
                return False;
           
       
    return True;