#include <string>
#include <iostream>
using namespace std;


class Solution
{
public:
    bool isMatch(string s, string p)
    {
        int pindex = 0;
        int sindex = 0;
        //char preceding;
        char pproduction;
        while (sindex < s.length && pindex < p.length)
        {
            if (p[pindex] == '.')
            {
                pindex++;
                sindex++;
                continue;
            }
            if (p[pindex] == '*')
            {
                    if{
                        
                    }
            }
            if (p[pindex] == s[sindex])
            {
                pindex++;
                sindex++;
                continue;
            }
            else
            {
                return false;
            }
        }
        if(pindex==p.length&&sindex==s.length)
        return true;
        else
        return false;
    }

private:
    bool isletter(char c)
    {
        if (c >= 'a' && c <= 'z')
        {
            return true;
        }
        return false;
    }
    bool isstar(char c)
    {
        if (c == '*')
        {
            return true;
        }
        return false;
    }
    bool ispoint(char c)
    {
        if (c == '.')
        {
            return true;
        }
        return false;
    }
};

class TestSolution
{
    /*test case
     
    */
    Solution solution;
    string s;
    string p;

public:
    void runtest()
    {
        while (true)
        {
            cin >> s;
            cin >> p;
            cout << "s=" << s << " p=" << p << endl;
            if (solution.isMatch(s, p))
            {
                cout << "true" << endl
                     << endl;
            }
        }
    }
};
int main()
{
    TestSolution ts;
    ts.runtest();
}