function g = discriminant(data, mu, sigma, p)

C = 2;
[M, N] = size(data);

g = zeros(M,C);

for index = 1:M
    for i = 1:2
        sum = 0;
        for n = 1:N
            sum = sum + (log(sigma(i,n)) + ((data(index,n) - mu(i,n)).^2)/(2*((sigma(i,n)).^2)));
        end
        g(index, i) = log(p(i)) - sum;
    end
end