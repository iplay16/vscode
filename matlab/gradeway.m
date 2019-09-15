
syms x y t

f=(x-2)^2+(y-4)^2; %求解函数的极小值点

g=[diff(f,x),diff(f,y)]; %求梯度
x0=0;
y0=0;
eps=1e-6;
v=[x,y];
g0=subs(g,v,[x0,y0]);%求[x0,y0]的梯度值
v1=[x0,y0];
temp0=norm(g0)
n=0;

while temp0>eps && n<=1000
    d=-g0;
    fval=subs(f,v,v1);
    ft=subs(f,v,v1+t*d);
    dft=diff(ft);
    v1=v1+double(solve(dft))*d; %求下一个迭代点
    g0=subs(g,v,v1);
    temp0=norm(g0);
    n=n+1;
end
disp(v1) %最优解
disp(fval) %f在v1处的最优值