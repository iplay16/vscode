f_xy = @ (x,y)(20+x*x+y*y-10*(cos(2*pi*x)+cos(2*pi*y)));
f = @(x)f_xy(x(1),x(2));
[x,fval] = simulannealbnd(f,rand(1,2))