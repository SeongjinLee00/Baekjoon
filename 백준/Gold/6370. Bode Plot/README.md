# [Gold III] Bode Plot - 6370 

[문제 링크](https://www.acmicpc.net/problem/6370) 

### 성능 요약

메모리: 123316 KB, 시간: 104 ms

### 분류

미적분학(calculus), 수학(math), 물리학(physics)

### 문제 설명

<p>Consider the AC circuit below. We will assume that the circuit is in steady-state. Thus, the voltage at nodes 1 and 2 are given by v<sub>1</sub> = V<sub>S</sub> cos ω t and v<sub>2</sub> = V<sub>R</sub> cos ( ωt + θ ) where VS is the voltage of the source, ω is the frequency (in radians per second), and t is time. V<sub>R</sub> is the magnitude of the voltage drop across the resistor, and θ is its phase.</p>

<p><img alt="" src="https://www.acmicpc.net/upload/images/bode.png" style="height:193px; width:259px"></p>

<p>You are to write a program to determine V<sub>R</sub> for different values of ω. You will need two laws of electricity to solve this problem. The first is Ohm’s Law, which states v<sub>2</sub> = i R where i is the current in the circuit, oriented clockwise. The second is i = C d/dt (v<sub>1</sub> – v<sub>2</sub>) which relates the current to the voltage on either side of the capacitor. “d/dt” indicates the derivative with respect to t.</p>

### 입력 

 <p>The input will consist of one or more lines. The first line contains three real numbers and a non-negative integer. The real numbers are V<sub>S</sub>, R, and C, in that order. The integer, n, is the number of test cases. The following n lines of the input will have one real number per line. Each of these numbers is the angular frequency, ω.</p>

### 출력 

 <p>For each angular frequency in the input you are to output its corresponding V<sub>R</sub> on a single line. Each V<sub>R</sub> value output should be rounded to three digits after the decimal point.</p>

