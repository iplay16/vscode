function len = pathLength(D,S)
    [r,c] = size(D);
    NIND = size(S,1);
    for i = 1:NIND
        p = [S(i,:) S(i,1)];
        i1 = p(1:end-1);
        i2 = p(2:end);
        len(i,1) = sum(D((i1-1)*c + i2));
    end
end