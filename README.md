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

<h2>🧮 Physics Background</h2>

<p>
The Hohmann transfer orbit is the most fuel-efficient two-impulse transfer between two coplanar circular orbits around the same central body (e.g., the Sun).  
The calculator uses the following key equations:
</p>

<pre><code>
a_transfer = (r1 + r2) / 2
t_transfer = π * sqrt(a_transfer³ / GM_sun)
Δv_depart  = |√(GM_sun / r1) * (√(2r2 / (r1 + r2)) - 1)|
Δv_arrive  = |√(GM_sun / r2) * (1 - √(2r1 / (r1 + r2)))|
φ_required = π - n_target * t_transfer
</code></pre>

<p>
Where:
</p>

<ul>
  <li><b>r₁</b> – radius of the initial orbit (m)</li>
  <li><b>r₂</b> – radius of the target orbit (m)</li>
  <li><b>n</b> – mean motion = √(GM / r³)</li>
  <li><b>GM_sun</b> – gravitational parameter of the Sun</li>
</ul>

<hr>

<h2>📂 Project Structure</h2>

<pre><code>
Hohmann-Transfer-Calculator-for-the-Solar-System/
├── calculator.py    # Main program file
├── hesaplayıcı.py   # Turkish program file
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
