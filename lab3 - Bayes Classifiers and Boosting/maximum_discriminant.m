function maximum_discriminant()

hand = imread('hand.ppm', 'ppm');
book = imread('book.ppm', 'ppm');
data1 = normalize_and_label(hand, 0);
data2 = normalize_and_label(book, 1);
test_data = [data1; data2];
[mu sigma] = bayes(test_data);

[M N] = size(test_data);
p = prior(test_data);
g = discriminant(test_data(:,1:2), mu, sigma, p);
[dummy class] = max(g, [], 2);
class = class - 1;
error_test = 1.0 - sum(class == test_data(:,end))/M


T = 6;
[mu, sigma, p, alpha, classes] = adaboost(test_data, T);
class = adaboost_discriminant(test_data(:,1:N-1), mu, sigma, p, alpha, classes, T);
boost_error_test = 1.0-sum(class == test_data(:,end))/M

end