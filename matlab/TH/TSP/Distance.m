function D = Distance(a)
    r = size(a,1);
    D = zeros(r,r);
    for i = 1:r
        for j = i+1:r
            D(i,j)=sqrt((a(i,1)-a(j,1))^2 + (a(i,2)-a(j,2))^2);
            D(j,i) = D(i,j);
        end
    end
end