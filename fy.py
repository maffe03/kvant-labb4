import numpy as np
c=2.998e8 #m/s
h=6.626e-34 #Js
e=1.602e-19 #CV
a=h*c/e
h_=h/(2*np.pi) #Js
m_e=9.1093837015e-31 #kg
m_n=1.6749e-27 #kg
m_p=1.6726e-27 #kg
def eV(E): return E/e # J/eV
def Joule(E): return E*e #eV/J
me_c2 = eV(m_e*c**2) #eV
h_c = (eV(h_ * c) * 1e9) #eVnm
E0 = 8.854e-12 #eV
H_E_0 = eV(m_e * e**4 / (8 * E0**2 * h**2)) #eV för grundläge i väte, ta * n^2
N_A = 6.022e23 #1/mol
k_b = 1.380649e-23 #J/K
m=3.1
M=63.54
P=8.96e6
def E_F(P, M): return (h**2/(8*m_e) * np.power((3*P*N_A/(M*np.pi)),2/3))
def printall(): print("h: " + str(h) + "\nm_e: " + str(m_e) + "\nc: " + str(c) + "\ne: " + str(e) + "\nh_: " + str(h_))
