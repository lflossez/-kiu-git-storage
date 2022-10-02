def solution(M1, M2, m1, m2, V, t):
    R = 0.082
    T = t + 273.15
    P_total = (m1/M1 + m2/M2)*R*T/V
    return P_total