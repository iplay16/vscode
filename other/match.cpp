char *s;
char *p=s;
bool match(char c){
    if(*p==c){
        p++;
        return true;
    }
    else
    {
        return false;
    }
}

bool simple(){

}
bool isempty(){

}
bool strdot(){
    if(!match('\"')) return false;
    if(isempty()) return false;
    if(simple()) return false;
    if(match('\"')) return false;
}

