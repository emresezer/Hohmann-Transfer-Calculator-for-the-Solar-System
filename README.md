<h1 align="center">🛰️ Hohmann Transfer Calculator for the Solar System</h1>
<p align="center">
  <em>A Python tool to compute Hohmann transfer orbits in the Solar System</em>
</p>

<hr>

<h2>🎯 Purpose & Scope</h2>
<p>
  This project enables calculation of orbital transfer parameters via the classic <strong>Hohmann transfer</strong> mechanism, 
  tailored for planetary bodies in the Solar System. It serves as both an educational and analytical tool for orbital mechanics and astrophysics.
</p>
<ul>
  <li>Calculate the ∆v (delta-v) required to transfer between two circular orbits of different radii around the Sun or a planet.</li>
  <li>Support for planetary bodies, transfer between orbits of known radii, or user-defined orbits.</li>
  <li>Output relevant orbital transfer information such as semi-major axis of transfer ellipse, eccentricity, time of flight, and required ∆v.</li>
  <li>Scripted in Python for clarity and extensibility.</li>
</ul>

<hr>

<h2>🧩 Project Structure</h2>

<pre>
📁 Hohmann-Transfer-Calculator-for-the-Solar-System/
│
├── calculator.py         → Main script in English for computing transfer parameters
├── hesaplayıcı.py        → Main script in Turkish variant (optional)
└── README.md             → This documentation file
</pre>

<hr>

<h2>⚙️ Installation & Usage</h2>
<ol>
  <li>Ensure you have <strong>Python 3.x</strong> installed.</li>
  <li>Install dependencies (e.g. <code>numpy</code>, <code>scipy</code> if used):
    <pre><code>pip install numpy scipy</code></pre>
  </li>
  <li>Run the calculator script:
    <pre><code>python calculator.py</code></pre>
    or for Turkish version:
    <pre><code>python hesaplayıcı.py</code></pre>
  </li>
  <li>Follow the prompts (or edit input variables) to define:
    <ul>
      <li>initial orbit radius (r₁)</li>
      <li>target orbit radius (r₂)</li>
      <li>central body gravitational parameter (µ) or select a Solar System body</li>
    </ul>
  </li>
  <li>The script outputs results such as transfer ellipse semi-major axis, eccentricity, time of flight, and ∆v requirements.</li>
</ol>

<hr>

<h2>📐 Orbital Mechanics Model</h2>

<p>
The core calculation is based on standard formulas for the Hohmann transfer between two circular co-planar orbits:
</p>

<pre>
a_transfer = (r₁ + r₂) / 2

∆v₁ = √(µ / r₁) × ( √(2 r₂ / (r₁ + r₂)) – 1 )
∆v₂ = √(µ / r₂) × ( 1 – √(2 r₁ / (r₁ + r₂)) )

time_of_flight = π × √(a_transfer³ / µ)
</pre>

<p>
Where:
<ul>
  <li><code>r₁</code> = initial orbit radius</li>
  <li><code>r₂</code> = target orbit radius</li>
  <li><code>a_transfer</code> = semi-major axis of the transfer ellipse</li>
  <li><code>µ</code> = standard gravitational parameter of the central body</li>
  <li><code>∆v₁</code>, <code>∆v₂</code> = velocity increments at departure and insertion respectively</li>
</ul>
</p>

<hr>

