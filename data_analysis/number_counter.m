rawdata = readmatrix('D:\Dateien Schnell\Python\Prime_Generator_Test\number_generator.csv');

xA = rawdata(:,2);

c = arrayfun(@(x)length(find(xA == x)), unique(xA), 'Uniform', false);
bar(cell2mat(c))