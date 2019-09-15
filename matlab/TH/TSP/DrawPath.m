function DrawPath(BestTrack,City)
    N = size(BestTrack,2);
    cityArray = zeros(N,2);
    for i = 1:N
        cityArray(i,1) = City(BestTrack(i),1);
        cityArray(i,2) = City(BestTrack(i),2);
    end
    figure;
    hold on
    plot(cityArray(:,1),cityArray(:,2),'-o','color',[0.5 0.5 0.5]);
    plot([cityArray(1,1),cityArray(end,1)],[cityArray(1,2),cityArray(end,2)],...
        '-','color',[0.5 0.5 0.5]);
    hold off
    xlabel('ºá×ø±ê');
    ylabel('×Ý×ø±ê');
    title('TSPÍ¼');
    box on
end