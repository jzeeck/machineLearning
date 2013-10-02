function [ mu, sigma ] = bayes( data )
%BAYES_CLASSIFIER Summary of this function goes here
%   Detailed explanation goes here

M = [0,0];
mu = [0,0;0,0];
temp_my = [0,0];
for i=1:size(data,1)
    class = data(i,3);
    M(class +1) = M(class + 1) + 1;
    mu(class + 1, 1) = mu(class + 1, 1) + data(i,1);
    mu(class + 1 , 2) = mu(class + 1, 2) + data(i,2);
end

mu(:,1) = mu(:,1)/M(1);
mu(:,2) = mu(:,2)/M(2);

sigma = [0,0;0,0];
for i=1:size(data,1)
    class = data(i,3);
    sigma(class + 1, 1) = sigma(class + 1, 1) + (data(i,1) - mu(class + 1, 1)).^2;
    sigma(class + 1, 2) = sigma(class + 1, 2) + (data(i,2) - mu(class + 1, 2)).^2;
end
sigma(:,1) = sigma(:,1)/M(1);
sigma(:,2) = sigma(:,2)/M(2);
sigma = sqrt(sigma);

end

