trie={}

def enTrie(query):
    words=query.split('\\')
    curr=trie

    for word in words:
        if word not in curr:
            curr[word]={}
        curr=curr[word]

def travel(depth, subtrie):
    for word in sorted(subtrie.keys()):
        print(' '*depth, end='')
        print(word)
        travel(depth+1,subtrie[word])


N=int(input())

for _ in range(N):
    enTrie(input())

travel(0,trie)