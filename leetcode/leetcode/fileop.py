class bit:
    def __init__(self,li):
        self.b=bytes(li)
        self.x=self.b[0:2]
        self.y=self.b[5:6]

        # self.z=[50,60]

    def printall(self):
        print(self.x)
        # print(self.y)
        # print(self.z)

if __name__=='__main__':
    dd=bit([9,4])
    file_obj=open('f:\\temp\\x.dat',mode='wb')
    file_obj.write(bytes([1,*[2,3],4]))
    file_obj.close()

    file_obj=open('f:\\temp\\x.dat','r')
    x=file_obj.read()
    c=bit(x)
    c.printall()