rawdata = readmatrix('results.csv');
xA = rawdata(:,7);
yA = rawdata(:,5);
scatter(xA,yA)

counter = 0;
limit = 20; %change height of horizontal line here
for i = 1:size(xA)
    if xA(i,1) > limit
        counter = counter +1;
    end
end

counter
yline(limit)