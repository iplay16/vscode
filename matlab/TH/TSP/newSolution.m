function S2 = newSolution(S1)
    N = length(S1);
    S2 = S1;
    a = round( rand(1,2)*(N-1)+1);  %产生两个随机位置用来交换
    temp = S2(a(1));
    S2(a(1))=S2(a(2));
    S2(a(2)) = temp;
end