syms x
% z=sin(10*pi*x) ./ x
z=cos(x)
zhandle=matlabFunction(z)
[r,zval]= simulannealbnd(zhandle,1.6,1,5)
scatter(r,zval,20,'r')
hold on
x=1:0.01:10
plot(x,zhandle(x),'b')

