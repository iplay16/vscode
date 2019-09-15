clc,clear
cities1=[0.6606,0.9695,0.5906,0.2124,0.0398,0.1367,0.9536,0.6091,0.8767,0.8148,0.3876,0.7041,0.0213,0.3429,0.7471,0.4606,0.7695,0.5006,0.3124,0.0098,0.3637,0.5336,0.2091,0.4767,0.4148,0.5876,0.6041,0.3213,0.6429,0.7471;

0.9500,0.6740,0.5029,0.8274,0.9697,0.5979,0.2184,0.7148,0.2395,0.2867,0.8200,0.3296,0.1649,0.3025,0.8192,0.6500,0.7420,0.0229,0.7274,0.4697,0.0979,0.2684,0.7948,0.4395,0.8867,0.3200,0.5296,0.3649,0.7025,0.9192];
% plot(cities1(1,:),cities1(2,:),'*')%模拟退火算法
%TSP问题

 
T0 =500;%初始温度
Tend = 1e-4; %终止温度
L=200; %各个温度下的链长
q=0.98; %降温速率
cityNum = 30; %城市个数
% City = rand(cityNum',2); %随机生成城市的坐标
 City=cities1'
%%%%%%%%%%%%%%主程序%%%%%%%%%%%%%%%%%%%%
D = Distance(City);
N = cityNum;
S1 = randperm(N); %产生一个随机解
%解方程，计算迭代次数
Time = ceil(double(solve(['1000*(0.9)^x',num2str(Tend)])));
count = 0; %迭代计数器
Obj = zeros(Time,1);    %每代路径和
track = zeros(Time,N);  %每代最优解
%迭代
while T0>Tend
    count = count + 1;
    temp = zeros(L,N+1);
    for k = 1:L
        %产生L组新解
        S2 = newSolution(S1);
        [S1,R] = Metropolis(S1,S2,D,T0);
        temp(k,:)=[S1 R];
    end
    %记录每次迭代过程的最优路线
    [d0,index] = min(temp(:,end));
    if count == 1 || d0 <Obj(count-1)
        Obj(count) = d0;
    else
        Obj(count)=Obj(count - 1);
    end
     
    track(count,:)=temp(index,1:end-1);
    T0 = q*T0;
end
fprintf('迭代次数：%d\n',count);
fprintf('最短路径：%f\n',Obj(end));
%迭代图
figure
plot(1:count,Obj);
xlabel('迭代次数');
ylabel('距离');
title('优化过程');
DrawPath(track(end,:),City);