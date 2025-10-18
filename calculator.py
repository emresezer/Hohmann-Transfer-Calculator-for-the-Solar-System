import math
G = 6.67430e-11         # m^3 kg^-1 s^-2
M_sun = 1.989e30        # kg
AU = 1.496e11           # m
planets = {
    "Earth": 1.0,
    "Mars": 1.524,
    "Venus": 0.723
}
print("Interplanetary Δv Calculator (Hohmann Transfer)")
start = input("Starting planet (Earth/Mars/Venus): ")
end = input("Target planet (Earth/Mars/Venus): ")
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
print(f"\nStarting planet: {start}")
print(f"Target planet: {end}")
print(f"Δv1 (departure burn) = {delta_v1/1000:.2f} km/s")
print(f"Δv2 (arrival burn) = {delta_v2/1000:.2f} km/s")
print(f"Total Δv = {total_delta_v/1000:.2f} km/s")
