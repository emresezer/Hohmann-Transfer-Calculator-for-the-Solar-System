import math
G = 6.67430e-11         # m^3 kg^-1 s^-2
M_sun = 1.989e30        # kg
AU = 1.496e11           # m
planets = {
    "Mercury": 0.387,
    "Venus": 0.723,
    "Earth": 1.000,
    "Mars": 1.524,
    "Jupiter": 5.203,
    "Saturn": 9.537,
    "Uranus": 19.191,
    "Neptune": 30.07,
    "Pluto": 39.48  # <3
}
print("🚀 Interplanetary Δv Calculator (Hohmann Transfer)")
print("---------------------------------------------------")
while True:
    start = input("Starting planet: ").capitalize()
    if start in planets:
        break
    else:
        print("Invalid planet name! Please enter one of:", ", ".join(planets.keys()))
while True:
    end = input("Target planet: ").capitalize()
    if end in planets:
        break
    else:
        print("Invalid planet name! Please enter one of:", ", ".join(planets.keys()))
r1 = planets[start] * AU
r2 = planets[end] * AU
v_c1 = math.sqrt(G * M_sun / r1)
v_c2 = math.sqrt(G * M_sun / r2)  
a = (r1 + r2) / 2 
v1 = math.sqrt(G * M_sun * (2/r1 - 1/a)) 
v2 = math.sqrt(G * M_sun * (2/r2 - 1/a))  
delta_v1 = abs(v1 - v_c1)
delta_v2 = abs(v_c2 - v2)
total_delta_v = delta_v1 + delta_v2
print(f"\n Starting planet: {start}")
print(f" Target planet: {end}")
print(f"Δv1 (departure burn) = {delta_v1/1000:.2f} km/s")
print(f"Δv2 (arrival burn) = {delta_v2/1000:.2f} km/s")
print(f" Total Δv required = {total_delta_v/1000:.2f} km/s")
if r2 > r1:
    print("↑ Outward transfer (to a higher orbit).")
elif r2 < r1:
    print("↓ Inward transfer (to a lower orbit).")
else:
    print("→ Same orbit! Δv = 0 km/s.")
