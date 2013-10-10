function [ output_args ] = final_adaboost( input_args )

[hand , book] = load_pics();
data1 = normalize_and_label(hand, 0);
data2 = normalize_and_label(book, 1);
data = [data1; data2];
T = 6;
[mu, sigma, p, alpha, classes] = adaboost(data, T);

book_rg = zeros(size(book,1), size(book,2), 2);
for y=1:size(book,1)
    for x=1:size(book,2)
        s = sum(book(y,x,:));
        if (s > 0)
            book_rg(y,x,:) = [double(book(y,x,1))/s double(book(y,x,2))/s];
        end
    end
end


tmp = reshape(book_rg, size(book_rg,1)*size(book_rg,2), 2);
g = adaboost_discriminant(tmp, mu, sigma, p, alpha, classes, T);
gg = reshape(g, size(book_rg,1), size(book_rg,2));
mask = gg > 0.5;

mask3D(:,:,1) = mask;
mask3D(:,:,2) = mask;
mask3D(:,:,3) = mask;
result_im = uint8(double(book) .* mask3D);
figure;
imagesc(result_im);



end

