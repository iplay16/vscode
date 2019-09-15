
syms x y t

f=(x-2)^2+(y-4)^2; %��⺯���ļ�Сֵ��

g=[diff(f,x),diff(f,y)]; %���ݶ�
x0=0;
y0=0;
eps=1e-6;
v=[x,y];
g0=subs(g,v,[x0,y0]);%��[x0,y0]���ݶ�ֵ
v1=[x0,y0];
temp0=norm(g0)
n=0;

while temp0>eps && n<=1000
    d=-g0;
    fval=subs(f,v,v1);
    ft=subs(f,v,v1+t*d);
    dft=diff(ft);
    v1=v1+double(solve(dft))*d; %����һ��������
    g0=subs(g,v,v1);
    temp0=norm(g0);
    n=n+1;
end
disp(v1) %���Ž�
disp(fval) %f��v1��������ֵ