function excercice1()
%EXCERCICE1 Summary of this function goes here
%   Detailed explanation goes here

hand = imread('hand.ppm','ppm');
book = imread('book.ppm','ppm');

data1 = normalize_and_label(hand, 0);
data2 = normalize_and_label(book, 1);
test_data = [data1;data2];
figure;
hold on;
plot(data2(:,1),data2(:,2),'.');
plot(data1(:,1),data1(:,2),'.r');
legend('Hand holding book', 'Hand');
xlabel('green');
xlabel('red');

end

