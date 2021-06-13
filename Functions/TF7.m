
function [o] = TF7(x)
nm = [1 2 4 8 16 32 64 128 2^8 2^9 2^10 2^11 2^12 2^13 2^14];
m = nm*(reshape(x,[],15))';
r = 1.28;
l = -1.28;
delta = (r-l)/(2^15);
xx = l + m.*delta; 
dim=size(xx,2);
o=sum([1:dim].*(xx.^4))+rand;
end

