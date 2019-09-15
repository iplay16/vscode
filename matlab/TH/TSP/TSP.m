clc,clear
cities1=[0.6606,0.9695,0.5906,0.2124,0.0398,0.1367,0.9536,0.6091,0.8767,0.8148,0.3876,0.7041,0.0213,0.3429,0.7471,0.4606,0.7695,0.5006,0.3124,0.0098,0.3637,0.5336,0.2091,0.4767,0.4148,0.5876,0.6041,0.3213,0.6429,0.7471;

0.9500,0.6740,0.5029,0.8274,0.9697,0.5979,0.2184,0.7148,0.2395,0.2867,0.8200,0.3296,0.1649,0.3025,0.8192,0.6500,0.7420,0.0229,0.7274,0.4697,0.0979,0.2684,0.7948,0.4395,0.8867,0.3200,0.5296,0.3649,0.7025,0.9192];
% plot(cities1(1,:),cities1(2,:),'*')%ģ���˻��㷨
%TSP����

 
T0 =500;%��ʼ�¶�
Tend = 1e-4; %��ֹ�¶�
L=200; %�����¶��µ�����
q=0.98; %��������
cityNum = 30; %���и���
% City = rand(cityNum',2); %������ɳ��е�����
 City=cities1'
%%%%%%%%%%%%%%������%%%%%%%%%%%%%%%%%%%%
D = Distance(City);
N = cityNum;
S1 = randperm(N); %����һ�������
%�ⷽ�̣������������
Time = ceil(double(solve(['1000*(0.9)^x',num2str(Tend)])));
count = 0; %����������
Obj = zeros(Time,1);    %ÿ��·����
track = zeros(Time,N);  %ÿ�����Ž�
%����
while T0>Tend
    count = count + 1;
    temp = zeros(L,N+1);
    for k = 1:L
        %����L���½�
        S2 = newSolution(S1);
        [S1,R] = Metropolis(S1,S2,D,T0);
        temp(k,:)=[S1 R];
    end
    %��¼ÿ�ε������̵�����·��
    [d0,index] = min(temp(:,end));
    if count == 1 || d0 <Obj(count-1)
        Obj(count) = d0;
    else
        Obj(count)=Obj(count - 1);
    end
     
    track(count,:)=temp(index,1:end-1);
    T0 = q*T0;
end
fprintf('����������%d\n',count);
fprintf('���·����%f\n',Obj(end));
%����ͼ
figure
plot(1:count,Obj);
xlabel('��������');
ylabel('����');
title('�Ż�����');
DrawPath(track(end,:),City);