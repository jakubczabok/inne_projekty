clear all; close all; clc;

% stała grawitacyjna
global g;
g=9.81;

% współczynnik oporu powietrza
global k;
k=0.5;

% pobranie danych od użytkownika
global m;
m=input('podaj masę [kg]: ');
v0=input('podaj prędkość początkową [m/s]: ');
alpha=input('podaj kąt wyrzutu [stopnie]: ');
x0=input('podaj położenie początkowe na osi X [m]: ');
y0=input('podaj położenie początkowe na osi Y [m]: ');

% zmiana jednostki kąta
alpha=pi*(alpha/180);

% rozkład prędkości początkowej na składowe
vx0=v0*cos(alpha);
vy0=v0*sin(alpha);

% początek układu (wektor położenia i prędkości)
wpp = [y0;vy0;x0;vx0];

% maksymalny czas trwania symulacji
tmax = 15;

% funkcja tworząca wektor pochodnych
function dy = f (t , y)
global m;
global g;
global k;
% położenie w osi Y = y(1)
% prędkość w osi Y = y(2)
% położenie w osi X = y(3)
% prędkość w osi X = y(4)
dy(1)=y(2);
dy(2)=-g-k/m*(y(2)*y(2)+y(4)*y(4))^(1/2)*y(2);
dy(3)=y(4);
dy(4)=-k/m*(y(2)*y(2)+y(4)*y(4))^(1/2)*y(4);
end

% funkcja definiująca moment upadku
function [value,isterminal,direction] = Stop(t, y)
value = y(1);
isterminal = 1;
direction = -1;
end

% czas
ts=linspace(0,tmax,tmax*1000);

% rozwiązanie równania różniczkowego (bez odbicia)
opcje = odeset('Events', @Stop);
[t,y]=ode45('f',ts,wpp,opcje);

% znalezienie momentu odbicia
maxY=max(y(:,1));
bounceindex=[~, index] = max(y(:,1));

% utworzenie macierzy z położeniami i prędkościami (do momentu odbicia)
y2=y(1:bounceindex, :);

% stan układu w momencie odbicia (wektor położenia i prędkości)
wpp2 = [y(bounceindex,1);y(bounceindex,2);y(bounceindex,3);-y(bounceindex,4)];

% rozwiązanie równania różniczkowego(po odbiciu)
opcje = odeset('Events', @Stop);
[t,y3]=ode45('f',ts,wpp2,opcje);

% cała macierz z położeniami i prędkościami
y2=vertcat(y2,y3);

% rysowanie trajektorii i obliczenie maksymalnej wysokości oraz odległości i czasu miejsca upadku
f1=figure(1)
hold on
ylabel("oś Y[m]");
xlabel("oś X[m]");
maxY=max(y2(:,1));
maxX=y2(end,3);
txt=[sprintf("maksymalna wysokość=%dm",maxY);sprintf("odległość w chwili upadku=%dm",maxX);sprintf("czas upadku=%ds",t(end))];
annotation('textbox', [0.725, 0.90, 0.1, 0],'String',txt);
y2(end,1)=0;
plot(y2(:,3),y2(:,1));
hold off;

