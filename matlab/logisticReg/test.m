clear
A=importdata('jumpdata.txt');

X=A(:,2);
X=X*100;
Y=A(:,1);
res=corrcoef(X,Y)