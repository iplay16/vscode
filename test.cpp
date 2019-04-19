#include<stdio.h>
#include<map>
#include<string>
#include<iostream>
#include<ext/hash_map>
#include<assert.h>
using namespace std;
using namespace __gnu_cxx;
int main(){
        int i=9;
    map<int,string> m1;
    
    m1.insert(map<int,string>::value_type(2,"student2"));
    m1.insert(map<int,string>::value_type(1,"student1"));
    //m1.insert(map<int,string>::value_type(2,"student3"));
    //m1.insert(pair<int,string>(2,"student3"));
    assert(i>10);
    m1.insert({1,"c++11"});
    m1[2]="student3";
    hash_map<int,string> hmap;
    hash_map<int,string>::iterator hit=hmap.begin();
    hmap.insert(hash_map<int,string>::value_type(34,"34element"));
    hmap.insert(hash_map<int,string>::value_type(33,"33element"));
    for(hash_map<int,string>::iterator it=hmap.begin();it!=hmap.end();it++){
            std::cout << it->first << " => " << it->second << '\n';
    }
    for(map<int,string>::iterator it=m1.begin();it!=m1.end();it++){
            std::cout << it->first << " => " << it->second << '\n';
    }
        //test 
        //test
    return 0;
}

