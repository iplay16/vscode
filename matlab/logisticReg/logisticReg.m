clear
A=importdata('jumpdata.txt');
x=A(:,1)
y=A(:,2)
n=length(A)
plot(x,y)
p = polyfit(x,y,3);
hold on
X=[x.^3,x.^2,x,ones(n,1)];
z=p*X'
plot(x,z)
syms x1
u=[x1.^3,x1.^2,x1,1]*p';
f=diff(u,2)
t=solve(f)