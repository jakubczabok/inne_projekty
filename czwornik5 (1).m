% parametry czwórnika R-C
% opornik R [Ω]
R = 1e3; 
% kondensator C [F]
C = 40e-6;

% parametry sygnału wejściowego
% liczba składowych harmonicznych
n = 10; 
% amplituda
A = input('podaj amplitudę: ');
% minimalna częstotliwość [Hz]
f_min = 1; 
% maksymalna częstotliwość [Hz]
f_max = 100; 

% ustalenie liczby próbek i kroku próbkowania
% częstotliwość próbkowania [Hz]
fs = 2*f_max; 
% okres próbkowania [s]
Ts = 1/fs;
% liczba próbek
M = input('podaj liczbę próbek (potęga liczby 2): ');
% wektor czasu
t = (0:M-1)*Ts; 

% generowanie sygnału wejściowego
x = zeros(1, M);
for i = 1:n
    % losowa częstotliwość [Hz]
    fi = f_min + (f_max-f_min)*rand(); 
    % składowa harmoniczna
    xi = A*cos(2*pi*fi*t); 
    % suma składowych
    x = x + xi; 
end

% obliczanie sygnału wyjściowego
y = zeros(1, M);
for i = 2:M
    y(i) = y(i-1) + (x(i) - y(i-1))/(R*C*fs);
end

% wyświetlanie wyników
figure;
subplot(2,1,1);
plot(t, x, 'b', t, y, 'r');
xlabel('czas [s]');
ylabel('amplituda');
legend('sygnał wejściowy', 'sygnał wyjściowy');

subplot(2,2,3);
% zastosowanie funkcji napisanej niżej w skrypcie
widmo_amplitudowe(x, fs);
title('amplitudowe widmo sygnału wejściowego');
subplot(2,2,4);
% zastosowanie funkcji napisanej niżej w skrypcie
widmo_amplitudowe(y, fs);
title('amplitudowe widmo sygnału wyjściowego');

figure;
subplot(2,2,1);
% zastosowanie funkcji napisanej niżej w skrypcie
widmo_fazowe(x, fs);
title('fazowe widmo sygnału wejściowego');
subplot(2,2,2);
% zastosowanie funkcji napisanej niżej w skrypcie
widmo_fazowe(y, fs);
title('fazowe widmo sygnału wyjściowego');

% funkcje pomocnicze
function widmo_amplitudowe(x, fs)
    % długość sygnału
    N = length(x);
    % wektor częstotliwości
    f = (0:N-1)*(fs/N);
    % widmo amplitudowe jako wartości bezwzględne 
    % po przeprowadzeni dyskretnej transformacji Fouriera sygnału 
    % znormalizowanej przez długość sygnału
    X = abs(fft(x))/N;
    % rysowanie wykresu
    plot(f, X);
    xlabel('częstotliwość [Hz]');
    ylabel('amplituda');
end
function widmo_fazowe(x, fs)
    % długość sygnału
    N = length(x);
    % wektor częstotliwości
    f = (0:N-1)*(fs/N);
    % dyskretna transformacja Fouriera sygnału 
    % znormalizowana przez jego długość
    X = fft(x)/N;
    % skalowanie widma dla częstotliwości
    X = X(1:N/2+1);
    % widmo fazowe jako kąty fazowe z widma
    % po usunięciu skoków kąta między -pi a pi
    phase = unwrap(angle(X));
    % rysowanie wykresu
    plot(f(1:N/2+1), phase);
    xlabel('częstotliwość [Hz]');
    ylabel('faza [rad]');
end
