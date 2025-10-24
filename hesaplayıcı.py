import math

# --- Evrensel Sabitler ---
G = 6.67430e-11         # m^3 kg^-1 s^-2
M_gunes = 1.989e30      # kg
AU = 1.496e11           # m
SN_GUN = 86400.0
SN_YIL = 365.25 * SN_GUN
R_dunya = 6371e3
LEO = R_dunya + 300e3    # Alçak Dünya Yörüngesi (örnek)

# --- Gezegenlerin Ortalama Yörünge Yarıçapları (AU) ---
gezegenler = {
    "Merkür": 0.387,
    "Venüs": 0.723,
    "Dünya": 1.000,
    "Mars": 1.524,
    "Jüpiter": 5.203,
    "Satürn": 9.537,
    "Uranüs": 19.191,
    "Neptün": 30.068
}

def norm_acı(rad):
    """Açıyı [0, 2π) aralığına normalize et"""
    return rad % (2 * math.pi)

def sn_gun(saniye):
    return saniye / SN_GUN

def sn_yil(saniye):
    return saniye / SN_YIL

# --- Başlangıç bilgileri ---
print("=== Faz Açılı Hohmann Transfer Hesaplayıcı ===")
print("Kullanılabilir gezegenler:", ", ".join(gezegenler.keys()))

# Başlangıç gezegeni seçimi
while True:
    baslangic = input("Başlangıç gezegeni: ").strip().capitalize()
    if baslangic in gezegenler:
        break
    print("Geçersiz gezegen! Şunlardan birini girin:", ", ".join(gezegenler.keys()))

# Hedef gezegen veya özel yarıçap girişi
secim = input("Hedef listeden mi seçilsin? (e/h) [e]: ").strip().lower()
if secim == "" or secim == "e":
    while True:
        hedef = input("Hedef gezegen: ").strip().capitalize()
        if hedef in gezegenler:
            r_hedef_au = gezegenler[hedef]
            break
        print("Geçersiz gezegen! Şunlardan birini girin:", ", ".join(gezegenler.keys()))
else:
    # Kullanıcı özel bir AU değeri girecek
    while True:
        try:
            r_hedef_au = float(input("Hedef yörünge yarıçapını girin (AU): ").strip())
            if r_hedef_au <= 0:
                print("Yarıçap pozitif olmalı.")
                continue
            hedef = f"Özel({r_hedef_au:.3f} AU)"
            break
        except ValueError:
            print("Sayısal AU değeri girin.")

# Gezegenlerin anlık konum açıları (isteğe bağlı)
def aci_sor(metin, varsayilan=0.0):
    s = input(f"{metin} (derece) [varsayılan: {varsayilan}°]: ").strip()
    if s == "":
        return math.radians(varsayilan)
    try:
        return math.radians(float(s))
    except ValueError:
        print("Geçersiz değer, varsayılan kullanılacak.")
        return math.radians(varsayilan)

print("\nGezegenlerin Güneş etrafındaki anlık konum açılarını (boylam) girebilirsiniz.")
theta1 = aci_sor(f"{baslangic} gezegeninin heliosentrik boylamı", 0.0)
theta2 = aci_sor(f"{hedef} gezegeninin heliosentrik boylamı", 60.0)  # hedef 60° önde varsayılan

# --- Yardımcı Fonksiyonlar ---
GM_gunes = G * M_gunes

def au_metre(r_au):
    return r_au * AU

def ortalama_aci_hizi(r_m):
    # n = sqrt(GM / r^3)
    return math.sqrt(GM_gunes / (r_m ** 3))

def dairesel_hiz(r_m):
    return math.sqrt(GM_gunes / r_m)

# Başlangıç ve hedef yarıçapları
r1 = au_metre(gezegenler[baslangic])
r2 = au_metre(r_hedef_au)

# Açısal hızlar ve yörünge periyotları
n1 = ortalama_aci_hizi(r1)
n2 = ortalama_aci_hizi(r2)
T1 = 2 * math.pi / n1
T2 = 2 * math.pi / n2

# Hohmann transfer parametreleri
a_transfer = 0.5 * (r1 + r2)
t_transfer = math.pi * math.sqrt(a_transfer ** 3 / GM_gunes)

# Hohmann Δv hesapları (Güneş merkezli)
v_c1 = dairesel_hiz(r1)
v_c2 = dairesel_hiz(r2)
v_transfer_peri = math.sqrt(GM_gunes * (2 / r1 - 1 / a_transfer))
v_transfer_apo = math.sqrt(GM_gunes * (2 / r2 - 1 / a_transfer))
dv_cikis = abs(v_transfer_peri - v_c1)
dv_varis = abs(v_c2 - v_transfer_apo)
dv_toplam = dv_cikis + dv_varis

# LEO'dan kaçış dahil edilsin mi?
leo_dahil = input("\nLEO'dan kaçış dahil edilsin mi? (e/h) [e]: ").strip().lower()
if leo_dahil == "" or leo_dahil == "e":
    v_LEO = math.sqrt(G * 5.972e24 / LEO)
    v_kacis = math.sqrt(2 * G * 5.972e24 / LEO)
    dv_LEO_kacis = max(0.0, v_kacis - v_LEO)
else:
    dv_LEO_kacis = 0.0

# Faz açısı hesabı (yaklaşık)
phi_gerekli = math.pi - n2 * t_transfer
phi_gerekli = norm_acı(phi_gerekli)

# Mevcut faz farkı
faz_mevcut = norm_acı(theta2 - theta1)

# Göreceli açısal hız
rel_n = n2 - n1

# Bekleme süresi hesabı
if abs(rel_n) < 1e-12:
    t_bekle = None
else:
    delta_phi = norm_acı(phi_gerekli - faz_mevcut)
    t_bekle = delta_phi / rel_n
    if t_bekle < 0:
        sinodik_periyot = 2 * math.pi / abs(rel_n)
        t_bekle += sinodik_periyot

# Kalkış ve varış zamanları
t_kalkis = 0.0 if t_bekle is None else t_bekle
t_varis = t_kalkis + t_transfer

# Tahmini açılar
theta1_kalkis = norm_acı(theta1 + n1 * t_kalkis)
theta2_varis = norm_acı(theta2 + n2 * t_varis)

# --- Sonuçlar ---
print("\n=== SONUÇLAR ===")
print(f"Başlangıç gezegeni: {baslangic}")
print(f"Hedef gezegen: {hedef}")
print(f"r1 = {r1/AU:.6f} AU, r2 = {r2/AU:.6f} AU")
print(f"n1 = {n1:.6e} rad/sn ; periyot T1 = {sn_gun(T1):.2f} gün")
print(f"n2 = {n2:.6e} rad/sn ; periyot T2 = {sn_gun(T2):.2f} gün")
print(f"\nYarı büyük eksen (a) = {a_transfer/AU:.6f} AU")
print(f"Transfer süresi = {sn_gun(t_transfer):.2f} gün = {sn_yil(t_transfer):.4f} yıl")
print(f"Δv (kalkış - Güneş merkezli) = {dv_cikis:.2f} m/s")
print(f"Δv (varış - Güneş merkezli) = {dv_varis:.2f} m/s")
print(f"Toplam Δv (Güneş merkezli) = {dv_toplam:.2f} m/s")
if dv_LEO_kacis > 0:
    print(f"Δv (LEO -> kaçış) ≈ {dv_LEO_kacis:.2f} m/s")
    print(f"Toplam görev Δv (LEO'dan hedefe) ≈ {dv_toplam + dv_LEO_kacis:.2f} m/s")

# Faz açısı bilgileri
print("\n--- Fazlama ve Zamanlama ---")
print(f"Gerekli faz açısı = {math.degrees(phi_gerekli):.3f}° (hedef bu kadar önde olmalı)")
print(f"Mevcut faz açısı = {math.degrees(faz_mevcut):.3f}°")
if t_bekle is None:
    print("Göreceli hareket çok küçük, fazlama tanımsız.")
else:
    print(f"Göreceli açısal hız = {rel_n:.6e} rad/sn")
    print(f"Bekleme açısı = {math.degrees(norm_acı(phi_gerekli - faz_mevcut)):.3f}°")
    print(f"Bekleme süresi = {sn_gun(t_kalkis):.2f} gün = {sn_yil(t_kalkis):.6f} yıl")
    print(f"Kalkış boylamı = {math.degrees(theta1_kalkis):.3f}°")
    print(f"Varıştaki hedef boylamı = {math.degrees(theta2_varis):.3f}°")
    print(f"Varış zamanı (şimdiden itibaren) = {sn_gun(t_varis):.2f} gün")

print("\n--- Notlar ---")
print("1) Bu hesaplamalar dairesel ve eş düzlemli (coplanar) yörüngeler varsayar.")
print("2) Faz açısı kuralı yaklaşık olarak φ = π - n_hedef * t_transfer şeklindedir.")
print("3) Gerçek görev planlarında gezegen etkileri, eğiklik ve çekim kayıpları ayrıca hesaplanmalıdır.")

bana bu kodda olan her şeyi fizik öğretmeniymişsin gibi formüllerle adım adım anlat ve örnek hesaplama çöz  
