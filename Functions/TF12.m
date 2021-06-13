
function [o] = TF12(x)
nm = [1 2 4 8 16 32 64 128 2^8 2^9 2^10 2^11 2^12 2^13 2^14];
m = nm*(reshape(x,[],15))';
r = 50;
l = -50;
delta = (r-l)/(2^15);
xx = l + m.*delta; 


dim=size(xx,2);
o=(pi/dim)*(10*((sin(pi*(1+(xx(1)+1)/4)))^2)+sum((((xx(1:dim-1)+1)./4).^2).*...
(1+10.*((sin(pi.*(1+(xx(2:dim)+1)./4)))).^2))+((xx(dim)+1)/4)^2)+sum(Ufun(xx,10,100,4));
end

function o=Ufun(x,a,k,m)
o=k.*((x-a).^m).*(x>a)+k.*((-x-a).^m).*(x<(-a));
end