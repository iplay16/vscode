function fitnessVal = fitness( x )
 
%һԪ�����Ż���
 
fitnessVal = sin(10*pi*x) / x;  %����Сֵ
 
% fitnessVal = -1 * sin(10*pi*x) / x; ��ģ���˻������ֵ�����ԼӸ����Ż���Ū��������
 
%��Ԫ�����Ż���
 
% fitnessVal = -1 * (x(1)^2 + x(2).^2 - 10*cos(2*pi*x(1)) - 10*cos(2*pi*x(2)) + 20);
 
end