function fitnessVal = fitness( x )
 
%一元函数优化：
 
fitnessVal = sin(10*pi*x) / x;  %求最小值
 
% fitnessVal = -1 * sin(10*pi*x) / x; 用模拟退火求最大值，可以加个负号或者弄个倒数！
 
%二元函数优化：
 
% fitnessVal = -1 * (x(1)^2 + x(2).^2 - 10*cos(2*pi*x(1)) - 10*cos(2*pi*x(2)) + 20);
 
end