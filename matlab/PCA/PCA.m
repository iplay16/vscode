clc;clear;
% A=100*rand(10,2);
% A=[2.5, 0.5, 2.2, 1.9, 3.1, 2.3, 2, 1, 1.5, 1.1;
% 2.4, 0.7, 2.9, 2.2, 3.0, 2.7, 1.6, 1.1, 1.6, 0.9]
A=rand(100,5);
X=zscore(A);
[coeff,score,latent,tsquare]=princomp(X)
%yΪ�������ԵĹ����ʣ���Ҫ���Ƶ�excel��ͳ����Щ�����ʼ��������Գ���85%���������ȡǰ��������
y=(100*latent/sum(latent))';

%ȡǰ�������ԣ���ά����������
B=X*coeff(:,1:3)