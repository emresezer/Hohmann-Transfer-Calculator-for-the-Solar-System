import math

# --- Universal Constants ---
G = 6.67430e-11         # m^3 kg^-1 s^-2
M_sun = 1.989e30        # kg
AU = 1.496e11           # m
SEC_DAY = 86400.0
SEC_YEAR = 365.25 * SEC_DAY
R_earth = 6371e3
LEO = R_earth + 300e3    # Low Earth Orbit (example)

# --- Mean Orbital Radii of Planets (AU) ---
planets = {
    "Mercury": 0.387,
    "Venus": 0.723,
    "Earth": 1.000,
    "Mars": 1.524,
    "Jupiter": 5.203,
    "Saturn": 9.537,
    "Uranus": 19.191,
    "Neptune": 30.068
}

def normalize_angle(rad):
    """Normalize an angle to [0, 2π) range"""
    return rad % (2 * math.pi)

def sec_to_days(seconds):
    return seconds / SEC_DAY

def sec_to_years(seconds):
    return seconds / SEC_YEAR

# --- Start Information ---
print("=== Phase-Angle Hohmann Transfer Calculator ===")
print("Available planets:", ", ".join(planets.keys()))

# Starting planet selection
while True:
    start = input("Starting planet: ").strip().capitalize()
    if start in planets:
        break
    print("Invalid planet! Choose one of:", ", ".join(planets.keys()))

# Target planet or custom radius input
choice = input("Select target from list? (y/n) [y]: ").strip().lower()
if choice == "" or choice == "y":
    while True:
        target = input("Target planet: ").strip().capitalize()
        if target in planets:
            r_target_au = planets[target]
            break
        print("Invalid planet! Choose one of:", ", ".join(planets.keys()))
else:
    # User enters a custom orbital radius (AU)
    while True:
        try:
            r_target_au = float(input("Enter target orbital radius (AU): ").strip())
            if r_target_au <= 0:
                print("Radius must be positive.")
                continue
            target = f"Custom({r_target_au:.3f} AU)"
            break
        except ValueError:
            print("Enter a numeric AU value.")

# Optional: current angular positions
def ask_angle(prompt, default=0.0):
    s = input(f"{prompt} (degrees) [default: {default}°]: ").strip()
    if s == "":
        return math.radians(default)
    try:
        return math.radians(float(s))
    except ValueError:
        print("Invalid value, default used.")
        return math.radians(default)

print("\nYou can enter the current heliocentric longitudes of the planets.")
theta1 = ask_angle(f"{start} planet's heliocentric longitude", 0.0)
theta2 = ask_angle(f"{target} planet's heliocentric longitude", 60.0)  # target 60° ahead by default

# --- Helper Functions ---
GM_sun = G * M_sun

def au_to_meters(r_au):
    return r_au * AU

def mean_motion(r_m):
    # n = sqrt(GM / r^3)
    return math.sqrt(GM_sun / (r_m ** 3))

def circular_velocity(r_m):
    return math.sqrt(GM_sun / r_m)

# Radii of start and target orbits
r1 = au_to_meters(planets[start])
r2 = au_to_meters(r_target_au)

# Angular velocities and orbital periods
n1 = mean_motion(r1)
n2 = mean_motion(r2)
T1 = 2 * math.pi / n1
T2 = 2 * math.pi / n2

# Hohmann transfer parameters
a_transfer = 0.5 * (r1 + r2)
t_transfer = math.pi * math.sqrt(a_transfer ** 3 / GM_sun)

# Hohmann Δv calculations (heliocentric)
v_c1 = circular_velocity(r1)
v_c2 = circular_velocity(r2)
v_transfer_peri = math.sqrt(GM_sun * (2 / r1 - 1 / a_transfer))
v_transfer_apo = math.sqrt(GM_sun * (2 / r2 - 1 / a_transfer))
dv_depart = abs(v_transfer_peri - v_c1)
dv_arrive = abs(v_c2 - v_transfer_apo)
dv_total = dv_depart + dv_arrive

# Include LEO escape?
leo_include = input("\nInclude escape from LEO? (y/n) [y]: ").strip().lower()
if leo_include == "" or leo_include == "y":
    v_LEO = math.sqrt(G * 5.972e24 / LEO)
    v_escape = math.sqrt(2 * G * 5.972e24 / LEO)
    dv_LEO_escape = max(0.0, v_escape - v_LEO)
else:
    dv_LEO_escape = 0.0

# Phase angle (approx.)
phi_required = math.pi - n2 * t_transfer
phi_required = normalize_angle(phi_required)

# Current phase difference
phase_current = normalize_angle(theta2 - theta1)

# Relative angular velocity
rel_n = n2 - n1

# Wait time calculation
if abs(rel_n) < 1e-12:
    t_wait = None
else:
    delta_phi = normalize_angle(phi_required - phase_current)
    t_wait = delta_phi / rel_n
    if t_wait < 0:
        synodic_period = 2 * math.pi / abs(rel_n)
        t_wait += synodic_period

# Departure and arrival times
t_depart = 0.0 if t_wait is None else t_wait
t_arrive = t_depart + t_transfer

# Predicted angles
theta1_depart = normalize_angle(theta1 + n1 * t_depart)
theta2_arrive = normalize_angle(theta2 + n2 * t_arrive)

# --- Results ---
print("\n=== RESULTS ===")
print(f"Starting planet: {start}")
print(f"Target planet: {target}")
print(f"r1 = {r1/AU:.6f} AU, r2 = {r2/AU:.6f} AU")
print(f"n1 = {n1:.6e} rad/s ; period T1 = {sec_to_days(T1):.2f} days")
print(f"n2 = {n2:.6e} rad/s ; period T2 = {sec_to_days(T2):.2f} days")
print(f"\nSemi-major axis (a) = {a_transfer/AU:.6f} AU")
print(f"Transfer time = {sec_to_days(t_transfer):.2f} days = {sec_to_years(t_transfer):.4f} years")
print(f"Δv (departure - heliocentric) = {dv_depart:.2f} m/s")
print(f"Δv (arrival - heliocentric) = {dv_arrive:.2f} m/s")
print(f"Total Δv (heliocentric) = {dv_total:.2f} m/s")
if dv_LEO_escape > 0:
    print(f"Δv (LEO -> escape) ≈ {dv_LEO_escape:.2f} m/s")
    print(f"Total mission Δv (from LEO to target) ≈ {dv_total + dv_LEO_escape:.2f} m/s")

# Phase and timing information
print("\n--- Phasing and Timing ---")
print(f"Required phase angle = {math.degrees(phi_required):.3f}° (target should lead by this much)")
print(f"Current phase angle = {math.degrees(phase_current):.3f}°")
if t_wait is None:
    print("Relative motion too small, phasing undefined.")
else:
    print(f"Relative angular velocity = {rel_n:.6e} rad/s")
    print(f"Wait angle = {math.degrees(normalize_angle(phi_required - phase_current)):.3f}°")
    print(f"Wait time = {sec_to_days(t_depart):.2f} days = {sec_to_years(t_depart):.6f} years")
    print(f"Departure longitude = {math.degrees(theta1_depart):.3f}°")
    print(f"Target longitude at arrival = {math.degrees(theta2_arrive):.3f}°")
    print(f"Arrival time (from now) = {sec_to_days(t_arrive):.2f} days")

print("\n--- Notes ---")
print("1) These calculations assume circular and coplanar (2D) orbits.")
print("2) The phase angle rule is approximately φ = π - n_target * t_transfer.")
print("3) Real mission planning must include gravitational assists, inclination, and perturbations.")
