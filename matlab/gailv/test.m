%参数入=1的指数分布在2.3处的值
Y=pdf('exp',2.3,1)
%正太分布N(3,2)在点4.5处的值
Y2=pdf('norm',4.5,3,2)
Y3=pdf('poiss',2,3)
%
a1=cdf('norm',7,3,4)