function [S,R] = Metropolis(S1,S2,D,T)
    R1 = pathLength(D,S1);
    R2 = pathLength(D,S2);
    dT = R2 - R1;
    if dT < 0
       S=S2;
       R=R2;
    elseif exp(-dT/T) >= rand
       S=S2;
       R=R2;
    else
       S=S1;
       R=R1;
    end
end