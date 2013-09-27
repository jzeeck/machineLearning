function [ mu, sigma ] = bayes( data )
%BAYES_CLASSIFIER Summary of this function goes here
%   Detailed explanation goes here

%N = size(data, 2) - 1
%M = [0,0];

%c = [];
%for i=1:size(data,1)
%   class = data(i,3);
%   if (not(ismember(class, c)))
%       c = [c class]; 
%   end

M = [0,0];
mu = [0,0;0,0];
for i=1:size(data,1)
    class = data(i,3);
    M(class +1) = M(class + 1) + 1;
    mu(1,class +1) = mu(1,class +1) + data(i,1);
    mu(2,class +1) = mu(2,class +1) + data(i,2);
end
mu(:,1) = mu(:,1)/M(1);
mu(:,2) = mu(:,2)/M(2);

sigma = [0,0;0,0];

for i=1:size(data,1)
    class = data(i,3);
    xi = data(i,1);
    yi = data(i,2);
    sigma(1, class +1) = sigma(1, class +1) + (data(1,1) - mu(1, class +1)).^2;
    sigma(2, class +1) = sigma(2, class +1) + (data(2,2) - mu(2, class +1)).^2;
end
sigma(:,1) = sigma(:,1)/M(1);
sigma(:,2) = sigma(:,2)/M(2);
sigma = sqrt(sigma);

end

