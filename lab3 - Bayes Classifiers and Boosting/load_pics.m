function  [out1 , out2] = load_pic()
%LOAD_PIC Summary of this function goes here
%   Detailed explanation goes here

%clear all                   % Remove all old variables
%close all                   % Close all figures
%clc                         % Clear the command window
%Load resource
out1 = imread('hand.ppm','ppm');
out2 = imread('book.ppm','ppm');

%[out1 , out2] = [hand, book];
end

