function S2 = newSolution(S1)
    N = length(S1);
    S2 = S1;
    a = round( rand(1,2)*(N-1)+1);  %�����������λ����������
    temp = S2(a(1));
    S2(a(1))=S2(a(2));
    S2(a(2)) = temp;
end