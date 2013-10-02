function [ mu, sigma ] = bayes_weight( data, w )

W = [0,0];
mu = [0,0;0,0];
for i=1:size(data,1)
    class = data(i,3);
    W(class +1) = W(class + 1) + w(i);
    mu(class + 1, 1) = mu(class + 1, 1) + (data(i,1)*w(i));
    mu(class + 1 , 2) = mu(class + 1, 2) + (data(i,2)*w(i));
end

mu(:,1) = mu(:,1)/W(1);
mu(:,2) = mu(:,2)/W(2);

sigma = [0,0;0,0];
for i=1:size(data,1)
    class = data(i,3);
    sigma(class + 1, 1) = sigma(class + 1, 1) + (((data(i,1) - mu(class + 1, 1)).^2)*w(i));
    sigma(class + 1, 2) = sigma(class + 1, 2) + (((data(i,2) - mu(class + 1, 2)).^2)*w(i));
end
sigma(:,1) = sigma(:,1)/W(1);
sigma(:,2) = sigma(:,2)/W(2);
sigma = sqrt(sigma);

end

