clear
syms a u;
c=[a,u]';%���ɾ���
% A=[15 16.1 17.3 18.4 18.7 19.6 19.9 21.3 22.5];%�������ݣ������޸�
A=100*rand(10,1)'
Ago=cumsum(A);%ԭʼ����һ���ۼ�,�õ�1-AGO����xi(1)��
n=length(A);%ԭʼ���ݸ���
for k=1:(n-1)
    Z(k)=(Ago(k)+Ago(k+1))/2; %Z(i)Ϊxi(1)�Ľ��ھ�ֵ��������
end
Yn =A;%YnΪ����������
Yn(1)=[]; %�ӵڶ�������ʼ����x(2),x(3)...
Yn=Yn';
E=[-Z;ones(1,n-1)]';%�ۼ�������������ֵ
c=(E'*E)\(E'*Yn);%���ù�ʽ���a��u
c= c';
a=c(1);%�õ�a��ֵ
u=c(2);%�õ�u��ֵ
F=[];
F(1)=A(1);
for k=2:(n)
    F(k)=(A(1)-u/a)/exp(a*(k-1))+u/a;%���GM(1,1)ģ�͹�ʽ
end
G=[];
G(1)=A(1);
for k=2:(n)
    G(k)=F(k)-F(k-1);%�������ԭԭ���У��õ�Ԥ������
end
t1=1:n;
t2=1:n;
plot(t1,A,'bo--');
hold on;
plot(t2,G,'r*-'); 
title('Ԥ����');
legend('��ʵֵ','Ԥ��ֵ');
%��������
e=A-G;
q=e/A;%������
s1=var(A);
s2=var(e);
c=s2/s1;%�����
len=length(e);
p=0;  %С������
for i=1:len
    if(abs(e(i))<0.6745*s1)
        p=p+1;
    end
end
p=p/len;