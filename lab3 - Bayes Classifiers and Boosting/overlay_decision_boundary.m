function overlay_decision_boundary()

hand = imread('hand.ppm', 'ppm');
book = imread('book.ppm', 'ppm');
data1 = normalize_and_label(hand, 0);
data2 = normalize_and_label(book, 1);
test_data = [data1; data2];
[mu sigma] = bayes(test_data);
p = prior(test_data);

ax = [0.2 0.5 0.2 0.45];
axis(ax);
x = ax(1):0.01:ax(2);
y = ax(3):0.01:ax(4);
[z1 z2] = meshgrid(x, y);
z1 = reshape(z1, size(z1, 1)*size(z1, 2), 1);
z2 = reshape(z2, size(z2, 1)*size(z2, 2), 1);
g = discriminant([z1 z2], mu, sigma, p);
gg = g(:,1) - g(:,2);
gg = reshape(gg, length(y), length(x));
[c, h] = contour(x, y, gg, [0.0 0.0]);
set(h, 'LineWidth', 3);

end