rawdata = readmatrix('results.csv');
xA = rawdata(:,7);
yA = rawdata(:,5);
scatter(xA,yA)
hold on
x = [5 10 15 20 25 30 35 40 100];
% jetzt nur noch die richtige Skala einstellen
yP=2.^x.^(1/3);
plot(x,yP)