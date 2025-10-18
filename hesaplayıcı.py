import math
G = 6.67430e-11         # m^3 kg^-1 s^-2
M_sun = 1.989e30        # kg
AU = 1.496e11           # m
planets = {
    "Dünya": 1.0,
    "Mars": 1.524,
    "Venüs": 0.723
}
print("Gezegenler arası Δv Hesaplayıcı (Hohmann Transfer)")
start = input("Başlangıç gezegeni (Dünya/Mars/Venüs): ")
end = input("Hedef gezegen (Dünya/Mars/Venüs): ")
r1 = planets[start] * AU
r2 = planets[end] * AU
v_c1 = math.sqrt(G * M_sun / r1)
v_c2 = math.sqrt(G * M_sun / r2)
a = (r1 + r2) / 2
v1 = math.sqrt(G * M_sun * (2/r1 - 1/a))
v2 = math.sqrt(G * M_sun * (2/r2 - 1/a))
delta_v1 = v1 - v_c1
delta_v2 = v_c2 - v2
total_delta_v = delta_v1 + delta_v2
print(f"\nBaşlangıç gezegeni: {start}")
print(f"Hedef gezegen: {end}")
print(f"Δv1 (yörüngeye çıkış) = {delta_v1/1000:.2f} km/s")
print(f"Δv2 (hedef gezegene giriş) = {delta_v2/1000:.2f} km/s")
print(f"Toplam Δv = {total_delta_v/1000:.2f} km/s")
