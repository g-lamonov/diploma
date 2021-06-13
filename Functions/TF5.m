
function [o] = TF5(x)
nm = [1 2 4 8 16 32 64 128 2^8 2^9 2^10 2^11 2^12 2^13 2^14];
m = nm*(reshape(x,[],15))';
r = 30;
l = -30;
delta = (r-l)/(2^15);
xx = l + m.*delta; 

dim=size(xx,2);
o=sum(100*(xx(2:dim)-(xx(1:dim-1).^2)).^2+(xx(1:dim-1)-1).^2);
end

