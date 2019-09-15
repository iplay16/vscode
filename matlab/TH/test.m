syms x y
z=(20+x*x+y*y-10*(cos(2*pi*x)+cos(2*pi*y)))
zhandle=matlabFunction(z)
[x,xval]= simulannealbnd(zhandle,1.2,1,3)