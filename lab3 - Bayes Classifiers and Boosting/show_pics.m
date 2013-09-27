function show_piics()
%SHOW_PICS Summary of this function goes here
%   Detailed explanation goes here

[hand , book] = load_pics();
imagesc(hand);
figure;
imagesc(book);

end

