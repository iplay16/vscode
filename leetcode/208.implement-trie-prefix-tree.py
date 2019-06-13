#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
class Trie:

    def __init__(self):
        # self.word='@'
        self.flag=False
        self.nextword=[None]*62
        """
        Initialize your data structure here.
        """
        

    def insert(self, word: str) -> None:
        # length=len(word)
        p=self
        for c in word:
            # for c in w:
            if p.nextword[ord(c)-65]==None:
                p.nextword[ord(c)-65]=Trie()
                p=p.nextword[ord(c)-65]
            else:
                p=p.nextword[ord(c)-65]
        p.flag=True

        """
        Inserts a word into the trie.
        """
        

    def search(self, word: str) -> bool:
        p=self
        for c in word:
            # for c in w:
            if p.nextword[ord(c)-65]==None:
                return False
            else:
                p=p.nextword[ord(c)-65]
        if p.flag==True:
            return True
        else:
            return False    
        """
        Returns if the word is in the trie.
        """
        

    def startsWith(self, prefix: str) -> bool:
        p=self
        for c in prefix:
            if p.nextword[ord(c)-65]==None:
                return False
            else:
                p=p.nextword[ord(c)-65]
        return True        
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """

def run(instance,action,data):
    li=[]
    for i in range(1,len(action)):
        ret=getattr(instance,action[i])
        b=ret(data[i][0])
        li.append(b)
        # print(b)
    return li

if __name__=='__main__':
    t=Trie()
    action=["Trie","insert","startsWith","search","insert","startsWith","search","insert","startsWith","search","insert","startsWith","search","insert","startsWith","search","insert","startsWith","search"]
    data=[[],["p"],["pr"],["p"],["pr"],["pre"],["pr"],["pre"],["pre"],["pre"],["pref"],["pref"],["pref"],["prefi"],["pref"],["prefi"],["prefix"],["prefi"],["prefix"]]
    # data=[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]
    li=run(t,action,data)
    print(li)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

