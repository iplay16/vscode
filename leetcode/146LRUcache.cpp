#include <unordered_map>
#include <list>
#include<new>
#include<assert.h>
using namespace std;

class LRUCache
{
    public:
    LRUCache(int capacity)
    {
        n = capacity;
    }

    int get(int key)
    {
        int val;
        auto it = umap.find(key);
        if (it != umap.end())
        {   //找到
            //{
            val = it->second->second;
            l.push_front(pair<int, int>(key, val));
            l.erase(it->second);
            it->second = l.begin();
            //}
            //return  
            return val;

        }
        else
        {
            return -1;
        }
    }
    void put(int key, int value)
    {
        auto it = umap.find(key);
        if (it != umap.end())
        {   
            l.erase(it->second); //it->second为lists的迭代器,该行代码删除了listit那个位置的元素
            l.push_front(pair<int, int>(key, value));
            umap[key] = l.begin();//umap[key]就是it->second
        }else  if (n>(int)l.size())
        { //cache 未满
            l.push_front(pair<int, int>(key, value));
            umap[key] = l.begin();
        }else if (it == umap.end())//未找到,需要置换
        {
            auto it = l.end();
            it--;
            umap.erase(it->first);
            l.erase(it); //删除最后一个元素
            l.push_front(pair<int, int>(key, value));
            umap[key] = l.begin();
        }
    }

private:
    int n;
    unordered_map<int, list<pair<int, int>>::iterator> umap;
    list<pair<int, int>> l;
    // void directinsert(int key,int val){
    //     l.push_front(pair(key,val));
    //     umap[key]=l.begin();
    // }
    // void replace(int key,int val){
    //     umap[key]->second=val;
    //     umap.insert(pair<int,list<pair<int,int>>::iterator>(key,l.begin()));
    // }
    // int adjustlist(int key,int value){
    //     int val;
    //     list<pair<int,int>>::iterator listit=value;
    //     val=listit->second;
    //     l.erase(listit);
    //     l.push_front(pair<int,int>(key,val));
    //     return val;
    // }
    // void removeandInsert(){
    //     l.erase(--(l.end()));
    // }
};

    int main(){
        LRUCache lru=LRUCache(2);
        lru.put(1,1);
        lru.put(2,2);
        lru.get(1);
        lru.put(3,3);
        lru.put(4,4);
        lru.get(4);
        lru.get(3);
        lru.get(2);
        lru.get(1);
        lru.put(5,5);
        lru.get(1);
         lru.get(2);
          lru.get(3);
           lru.get(4);
           lru.get(5);
        return 0;
    }