% Parametry czwórnika R-C
R = 1e3; % opornik R [Ω]
C = 40e-6; % kondensator C [F]

% Parametry sygnału wejściowego
n = 10; % liczba składowych harmonicznych
A = 1; % amplituda
f_min = 1; % minimalna częstotliwość [Hz]
f_max = 100; % maksymalna częstotliwość [Hz]

% Obliczanie liczby próbek M i kroku próbkowania
fs = 2*f_max; % częstotliwość próbkowania [Hz]
Ts = 1/fs; % okres próbkowania [s]
M = 2^nextpow2(fs); % liczba próbek
t = (0:M-1)*Ts; % wektor czasu

% Generowanie sygnału wejściowego
x = zeros(1, M);
for i = 1:n
    fi = f_min + (f_max-f_min)*rand(); % losowa częstotliwość [Hz]
    xi = A*cos(2*pi*fi*t); % składowa harmoniczna
    x = x + xi; % suma składowych
end

% Obliczanie sygnału wyjściowego
y = zeros(1, M);
for i = 2:M
    y(i) = y(i-1) + (x(i) - y(i-1))/(R*C*fs);
end

% Wyświetlanie wyników
figure;
subplot(2,1,1);
plot(t, x, 'b', t, y, 'r');
xlabel('Czas [s]');
ylabel('Amplituda');
legend('Sygnał wejściowy', 'Sygnał wyjściowy');

subplot(2,2,3);
plot_fft(x, fs);
title('Amplitudowe widmo sygnału wejściowego');
subplot(2,2,4);
plot_fft(y, fs);
title('Amplitudowe widmo sygnału wyjściowego');

figure;
subplot(2,2,1);
plot_phase(x, fs);
title('Fazowe widmo sygnału wejściowego');
subplot(2,2,2);
plot_phase(y, fs);
title('Fazowe widmo sygnału wyjściowego');

function plot_fft(x, fs)
    N = length(x);
    f = (0:N-1)*(fs/N);
    X = abs(fft(x))/N;
    plot(f, X);
    xlabel('Częstotliwość [Hz]');
    ylabel('Amplituda');
end

function plot_phase(x, fs)
    N = length(x);
    f = (0:N-1)*(fs/N);
    X = fft(x)/N;
    X = X(1:N/2+1);
    phase = unwrap(angle(X));
    plot(f(1:N/2+1), phase);
    xlabel('Częstotliwość [Hz]');
    ylabel('Faza [rad]');
end
