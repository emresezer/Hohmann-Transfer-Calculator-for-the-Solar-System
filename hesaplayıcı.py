import math
G = 6.67430e-11         # m^3 kg^-1 s^-2
M_sun = 1.989e30        # kg
AU = 1.496e11           # m
gezegenler = {
    "Merkür": 0.387,
    "Venüs": 0.723,
    "Dünya": 1.000,
    "Mars": 1.524,
    "Jüpiter": 5.203,
    "Satürn": 9.537,
    "Uranüs": 19.191,
    "Neptün": 30.07,
    "Plüton": 39.48  # <3
}
print("🚀 Gezegenler Arası Δv Hesaplayıcı (Hohmann Transferi)")
print("---------------------------------------------------")
while True:
    baslangic = input("Başlangıç gezegeni: ").capitalize()
    if baslangic in gezegenler:
        break
    else:
        print("Geçersiz gezegen adı! Lütfen şunlardan birini girin:", ", ".join(gezegenler.keys()))
while True:
    hedef = input("Hedef gezegen: ").capitalize()
    if hedef in gezegenler:
        break
    else:
        print("Geçersiz gezegen adı! Lütfen şunlardan birini girin:", ", ".join(gezegenler.keys()))
r1 = gezegenler[baslangic] * AU
r2 = gezegenler[hedef] * AU
v_c1 = math.sqrt(G * M_sun / r1)
v_c2 = math.sqrt(G * M_sun / r2)
a = (r1 + r2) / 2
v1 = math.sqrt(G * M_sun * (2/r1 - 1/a))
v2 = math.sqrt(G * M_sun * (2/r2 - 1/a))
delta_v1 = abs(v1 - v_c1)
delta_v2 = abs(v_c2 - v2)
toplam_delta_v = delta_v1 + delta_v2
print(f"\n Başlangıç gezegeni: {baslangic}")
print(f" Hedef gezegen: {hedef}")
print(f"Δv1 (kalkış manevrası) = {delta_v1/1000:.2f} km/s")
print(f"Δv2 (varış manevrası) = {delta_v2/1000:.2f} km/s")
print(f" Toplam gereken Δv = {toplam_delta_v/1000:.2f} km/s")
if r2 > r1:
    print("↑ Dışa transfer (daha yüksek yörüngeye).")
elif r2 < r1:
    print("↓ İçe transfer (daha alçak yörüngeye).")
else:
    print("→ Aynı yörünge! Δv = 0 km/s.")
