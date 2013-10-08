function [mu, sigma, p, alpha, classes] = adaboost(data, T)
%ADABOOST Summary of this function goes here
%   Detailed explanation goes here

[M, N] = size(data);

w(1:M) = 1/M;
p = zeros(2,T);
alpha = zeros(T,1);
classes = [0,1];
global global_hyp
global_hyp = zeros(M,T);

for t = 1:T
    p(:,t) = prior(data, w);
    [mu(:,:,t), sigma(:,:,t)] =  bayes_weight(data, w);

    h = discriminant(data(:,1:2), mu(:,:,t), sigma(:,:,t), p(:,t));
    [~, class] = max(h, [], 2);
    class = class - 1;
    global_hyp(:,t) = class;

    sum = 0;
    for m = 1:M
        sum = sum + w(m)*delta_func(class(m), data(m,3));
    end
    error = 1 - sum;
    
    alpha(t) = log((1-error)/error)/2;
    
    Z = 0;
    for m = 1:M
        if delta_func(class(m),data(m,3)) == 1
            w(m) = w(m)*exp(-alpha(t));
        else
            w(m) = w(m)*exp(alpha(t));
        end
        Z = Z + w(m);
    end
    w = w/Z;
end

end

