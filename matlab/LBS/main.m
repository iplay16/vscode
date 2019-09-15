bt=importdata('basetower.txt')
TOA=importdata('TOAdata.txt')
td=importdata('terminaldata.txt')
A=bt(1,:)
line=length(A);
for i=1:line;
    td(i,:)=td(i,:)-A
end
d=sum(td.^2,2).^(1/2)
sj=d/(3e8)
h=scatter(TOA(:,1)',sj')