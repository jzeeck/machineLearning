function c = adaboost_discriminant(data, mu, sigma, p, alpha, classes, T)
[M, N] = size(data);

for t = 1:T
    C = size(classes)
    h = discriminant(data(:,1:2), mu(:,:,t), sigma(:,:,t), p(t,:));
    
    [~, h] = max(h, [], 2);
    h = h - 1;
end
    
for m = 1:M
	best_score = -1;
    class = -1;    
    for i = 1:C
        score = 0;
        for t = 1:T
        	score = score + alpha(t)*delta_func(h(m), data(m,3));
        end
    
        if score > best_score
            best_score = score;
            class = i - 1;
        end
    end    
	c(m) = class;
end


end

