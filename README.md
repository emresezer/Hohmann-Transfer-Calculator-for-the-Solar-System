<h1 align="center">☀️ Hohmann Transfer Calculator for the Solar System 🚀</h1>

<hr>

<h2>🛰️ Project Overview</h2>

<p>
This project is a <b>command-line orbital mechanics calculator</b> that computes <b>Hohmann transfer trajectories</b> between planets in the Solar System.  
It simulates <b>interplanetary travel</b> using classical two-body mechanics and calculates:
</p>

<ul>
  <li>Heliocentric transfer orbits</li>
  <li>Phase angle and wait time before launch</li>
  <li>Delta-v requirements (departure, arrival, and total)</li>
  <li>Transfer time and orbital periods</li>
  <li>Optional LEO (Low Earth Orbit) escape velocity correction</li>
</ul>

<p>
All computations are made using <b>analytical orbital mechanics formulas</b> and can be adapted for <i>mission planning, academic research, or educational simulations</i>.
</p>

<hr>

<h2>⚙️ Features</h2>

<ul>
  <li>Supports all major Solar System planets (Mercury → Neptune)</li>
  <li>Custom target orbital radius (AU) input</li>
  <li>Custom initial heliocentric longitudes</li>
  <li>Automatic calculation of:
    <ul>
      <li>Phase angle (φ)</li>
      <li>Transfer duration</li>
      <li>Wait time until ideal alignment</li>
      <li>Total Δv (optionally including LEO escape)</li>
    </ul>
  </li>
  <li>Readable and well-commented Python code for teaching orbital dynamics</li>
</ul>

<hr>

<h2>🧭 Universal Constants and Units</h2>

<p>
The program uses the following physical constants and reference units, all expressed in <b>SI (metric)</b> form.  
These constants define the gravitational environment of the Solar System for Hohmann transfer computations.
</p>

<ul>
  <li><b>Universal Gravitational Constant:</b>  
  <code>G = 6.67430 × 10⁻¹¹ m³·kg⁻¹·s⁻²</code></li>

  <li><b>Solar Mass:</b>  
  <code>M☉ = 1.989 × 10³⁰ kg</code></li>

  <li><b>Astronomical Unit (AU):</b>  
  <code>1 AU = 1.496 × 10¹¹ m</code></li>

  <li><b>Earth Radius and Low Earth Orbit (LEO) Example:</b>  
  <code>R⊕ = 6.371 × 10⁶ m</code>,  
  <code>LEO = R⊕ + 3.00 × 10⁵ m</code></li>

  <li><b>Time Conversions:</b>  
  <code>1 day = 86,400 s</code>,  
  <code>1 year = 365.25 × 86,400 s</code></li>
</ul>

<p>
All formulas operate strictly in SI units:
</p>

<ul>
  <li>Distance → <b>meters (m)</b></li>
  <li>Velocity → <b>meters per second (m/s)</b></li>
  <li>Time → <b>seconds (s)</b></li>
</ul>


<h2>🧮 Physics Background</h2>

<p>
The <b>Hohmann transfer orbit</b> is the most energy-efficient two-impulse trajectory between two coplanar circular orbits around a central mass (e.g., the Sun).  
This tool implements the following classical relations.
</p>

<h3>1. Gravitational Parameter (μ)</h3>
<p>
For the Sun: μ = G × M<sub>☉</sub>.  
In the program: <code>GM_sun = G * M_sun</code>.
</p>

<h3>2. Mean Motion (n)</h3>
<p>
The average angular velocity of a body in circular orbit:
</p>

<pre><code>n = √(μ / r³)</code></pre>

<p>
The orbital period is related as:
</p>

<pre><code>T = 2π / n</code></pre>

<h3>3. Circular Orbital Velocity (v<sub>c</sub>)</h3>
<p>
Velocity for a stable circular orbit of radius <i>r</i>:
</p>

<pre><code>v_c = √(μ / r)</code></pre>

<h3>4. Vis-Viva Equation</h3>
<p>
The velocity at any point of an elliptical orbit:
</p>

<pre><code>v = √(μ * (2/r - 1/a))</code></pre>

<p>
where <i>a</i> is the semi-major axis of the orbit.
</p>

<h3>5. Hohmann Transfer Ellipse</h3>
<p>
Semi-major axis of the transfer orbit:
</p>

<pre><code>a_t = (r₁ + r₂) / 2</code></pre>

<p>
Transfer time (half-period of the ellipse):
</p>

<pre><code>t_transfer = π * √(a_t³ / μ)</code></pre>

<h3>6. Δv Calculations (Heliocentric)</h3>

<p>
Departure (from r₁):</p>
<pre><code>Δv_depart = |v_t(r₁) - v_c(r₁)|</code></pre>
<pre><code>v_t(r₁) = √(μ * (2/r₁ - 1/a_t))</code></pre>

<p>
Arrival (at r₂):</p>
<pre><code>Δv_arrive = |v_c(r₂) - v_t(r₂)|</code></pre>

<p>
Total heliocentric Δv:</p>
<pre><code>Δv_total = Δv_depart + Δv_arrive</code></pre>

<h3>7. LEO Escape Approximation</h3>

<p>
For missions starting from Earth orbit:</p>

<pre><code>v_LEO = √(G * M_⊕ / r_LEO)
v_esc = √(2 * G * M_⊕ / r_LEO)
Δv_escape ≈ v_esc - v_LEO
</code></pre>

<p>
This correction is added to the heliocentric Δv to approximate the total launch Δv requirement.
</p>

<h3>8. Phase Angle and Timing Geometry</h3>

<p>
Required phase angle at launch:</p>

<pre><code>φ_required ≈ π - n₂ * t_transfer</code></pre>

<p>
Current phase difference:</p>

<pre><code>Δθ_current = (θ₂ - θ₁)  (normalized to [0, 2π))</code></pre>

<p>
Relative angular velocity:</p>

<pre><code>n_rel = n₂ - n₁</code></pre>

<p>
Wait time before optimal launch:</p>

<pre><code>t_wait = normalize(φ_required - Δθ_current) / n_rel</code></pre>

<p>
If negative, the synodic period is added:
</p>

<pre><code>T_syn = 2π / |n_rel|</code></pre>

<hr>

<h2>📂 Project Structure</h2>

<pre><code>
Hohmann-Transfer-Calculator-for-the-Solar-System/
├── calculator.py    # Main program file
├── harita.py        # Turkish map file
├── hesaplayıcı.py   # Turkish program file
├── harita.py        # Main map file
└── README.md        # Project documentation (this file)
</code></pre>

<hr>

<h2>📚 Dependencies</h2>

<p>No external dependencies are required. The script uses only Python's built-in <code>math</code> library.</p>

<pre><code>import math</code></pre>

<h2>💻 How to Use</h2>

<ol>
  <li>Clone the repository:
    <pre><code>git clone https://github.com/emresezer/Hohmann-Transfer-Calculator-for-the-Solar-System.git</code></pre>
  </li>
  <li>Run the Python script:
    <pre><code>python calculator.py</code></pre>
  </li>
  <li>Follow the interactive prompts:
    <ul>
      <li>Select a starting planet</li>
      <li>Choose a target planet or custom orbit</li>
      <li>Optionally include LEO escape</li>
      <li>View full mission parameters</li>
    </ul>
  </li>
</ol>

<h2>
🌍 Example Output (Earth → Mars):
</h2>

<pre><code>
=== RESULTS ===
Starting planet: Earth
Target planet: Mars
r1 = 1.000000 AU, r2 = 1.524000 AU
Transfer time = 258.77 days = 0.709 years
Δv total (heliocentric) = 5594.43 m/s
Phase angle required = 44.3°
Wait time = 142.6 days
</code></pre>



<h2> Applications & Future Improvements</h2>

<ul>
  <li>Space mission design and trajectory planning</li>
  <li>Educational orbital mechanics demonstrations</li>
  <li>Research simulations in astrophysics or aerospace studies</li>
</ul>


<ul>
  <li>Add 3D orbit inclination and eccentricity effects</li>
  <li>Integrate matplotlib visualizations for transfer trajectories</li>
  <li>Support patched-conic multi-body transfers</li>
  <li>Extend for interstellar mission concepts</li>
</ul>
