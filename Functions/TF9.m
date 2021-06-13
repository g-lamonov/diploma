
function [o] = TF9(x)
nm = [1 2 4 8 16 32 64 128 2^8 2^9 2^10 2^11 2^12 2^13 2^14];
m = nm*(reshape(x,[],15))';
r = 5.12;
l = -5.12;
delta = (r-l)/(2^15);
xx = l + m.*delta; 

dim=size(xx,2);
o=sum(xx.^2-10*cos(2*pi.*xx))+10*dim;
end

