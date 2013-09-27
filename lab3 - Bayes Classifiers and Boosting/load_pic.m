function  load_pic()
%LOAD_PIC Summary of this function goes here
%   Detailed explanation goes here

clear all                   % Remove all old variables
close all                   % Close all figures
clc                         % Clear the command window
hand = imread('hand.ppm','ppm');
book = imread('book.ppm','ppm');
imagesc(hand);
figure;
imagesc(book);

end

