
function [o] = TF10(x)
nm = [1 2 4 8 16 32 64 128 2^8 2^9 2^10 2^11 2^12 2^13 2^14];
m = nm*(reshape(x,[],15))';
r = 32;
l = -32;
delta = (r-l)/(2^15);
xx = l + m.*delta; 

dim=size(xx,2);
o=-20*exp(-.2*sqrt(sum(xx.^2)/dim))-exp(sum(cos(2*pi.*xx))/dim)+20+exp(1);
end

