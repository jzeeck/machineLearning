function [ output_args ] = adaboost_decision_boundary( input_args )

[hand , book] = load_pics();
data1 = normalize_and_label(hand, 0);
data2 = normalize_and_label(book, 1);
T = 6;
data = [data1; data2];
[mu, sigma, p, alpha, classes] = adaboost(data, T);

figure;
hold on;
plot(data2(:,1), data2(:,2), '.');
plot(data1(:,1), data1(:,2), '.r');
legend('Hand holding book', 'Hand');
ax = [0.2 0.5 0.2 0.45];
axis(ax);
x = ax(1):0.01:ax(2);
y = ax(3):0.01:ax(4);
[z1 z2] = meshgrid(x, y);
z1 = reshape(z1, size(z1,1)*size(z1,2), 1);
z2 = reshape(z2, size(z2,1)*size(z2,2), 1);
g = adaboost_discriminant([z1 z2], mu, sigma, p, alpha, classes, T);
gg = reshape(g, length(y), length(x));
[c,h] = contour(x, y, gg, [0.5 0.5]);
set(h, 'LineWidth', 3);


end

