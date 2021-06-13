
function [o] = TF11(x)

nm = [1 2 4 8 16 32 64 128 2^8 2^9 2^10 2^11 2^12 2^13 2^14];
m = nm*(reshape(x,[],15))';
r = 600;
l = -600;
delta = (r-l)/(2^15);
xx = l + m.*delta; 

dim=size(xx,2);
o=sum(xx.^2)/4000-prod(cos(xx./sqrt([1:dim])))+1;
end

