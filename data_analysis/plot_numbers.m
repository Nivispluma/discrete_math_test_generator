rawdata = readmatrix('results.csv');
dimensions = length(rawdata);

xA = rawdata(:,1);
yA = rawdata(:,5);
zA = rawdata(:,7);

x = reshape(xA,[],dimensions);
y = reshape(yA,[],dimensions);
z = reshape(zA,[],dimensions);

surf(hrrr)