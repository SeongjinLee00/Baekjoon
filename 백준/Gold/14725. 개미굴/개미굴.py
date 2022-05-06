trie={}

def enTrie(words):
    curr=trie
    for word in words:
        if word not in curr:
            curr[word]={}
        curr=curr[word]

def travel(level, subtrie):
    for word in sorted(subtrie.keys()):
        print('--'*level, end='')
        print(word)
        travel(level+1, subtrie[word])


N=int(input())

for _ in range(N):
    d,*words=input().split()
    enTrie(words)

travel(0,trie)