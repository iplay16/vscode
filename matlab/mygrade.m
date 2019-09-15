syms x1 x2; %�������ű����ͺ����Ŀ�ݷ�ʽ

% 
% f=(x1-2)^2+2*(x2-1)^2;
% x=[1;3];
% step=10^(-20);
% right answer:[2;1]
% 
% f=x1-x2+2*x1^2+2*x1*x2+x2^2;
% x=[0;0];
% e=10^(-20);
% right answer:[-1;1.5]
% 
f=3/2*x1^2+1/2*x2^2-x1*x2-2*x1;
x=[0;0];
e=10^(-2);
% right answer:[0.9959;0.9877]
%
d=[diff(f,x1);diff(f,x2)];     %�ֱ���x1��x2��ƫ���������½��ķ���. d=1-2*x1   8-4*x2
count=1;
err=1;
%diff_temp=[0;0]
while err>0.001&&count<1000
    step=1/count;
    diff_temp=subs(d,x1,x(1)) ;%�����滻��������d���ʽ�����е�x1��ֵ�滻Ϊx(1)��ֵ������d�����ء�
    diff_temp=subs(diff_temp,x2,x(2)); %ƫ������ֵ
    x=x-diff_temp*step;
%     disp('diff_temp');
%     disp(vpa(diff_temp,4));
%     disp('x');
%     disp(vpa(x,4));
    err=norm(diff_temp);
    count=count+1;
   % pause(0.1)
end
disp(vpa(x,4))
disp(count)
