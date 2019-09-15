pos=rand(10,2);
scatter(pos(:,1),pos(:,2))
hold on
for i = 1:(length(pos)-1)
    t1=[pos(i,1);pos(i+1,1)]
    t2=[pos(i,2);pos(i+1,2)]
    plot(t1,t2,'Color','r')
end