
function [o] = TF13(x)
nm = [1 2 4 8 16 32 64 128 2^8 2^9 2^10 2^11 2^12 2^13 2^14];
m = nm*(reshape(x,[],15))';
r = 50;
l = -50;
delta = (r-l)/(2^15);
xx = l + m.*delta; 

dim=size(xx,2);
o=.1*((sin(3*pi*xx(1)))^2+sum((xx(1:dim-1)-1).^2.*(1+(sin(3.*pi.*xx(2:dim))).^2))+((xx(dim)-1)^2)*(1+(sin(2*pi*xx(dim)))^2))+sum(Ufun(xx,5,100,4));
end

function o=Ufun(x,a,k,m)
o=k.*((x-a).^m).*(x>a)+k.*((-x-a).^m).*(x<(-a));
end