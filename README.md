<h1>operations-research-decision-suite</h1>
<p>Computational Operations Research, combinatorial graph routing, linear programming (HiGHS), multi-criteria decision making (AHP), and quantitative time-series forecasting in Python</p>

<h2>Project description</h2>
<p>This repository provides a modular, production-grade computational framework covering fundamental methods in Operations Research, discrete mathematics, and quantitative decision analysis:</p>
<ol>
  <li>
    <dl>
      <dt><b>Linear Programming &amp; Optimization:</b></dt>
      <dd>Solves constrained multivariate linear minimization models ($\min c^T x$ s.t. $A x \geq b, x \geq 0$) using the dual simplex HiGHS solver via <code>scipy.optimize.linprog</code>.</dd>
      <dd>Constructs continuous geometric boundary envelopes to shade 2D feasible solution spaces.</dd>
    </dl>
  </li>
  <li>
    <dl>
      <dt><b>Network Routing &amp; Combinatorial Optimization:</b></dt>
      <dd>Solves the Traveling Salesperson Problem (TSP) using exhaustive permutation enumeration across symmetric distance matrices.</dd>
      <dd>Executes single-source single-target Dijkstra routing on directed weighted graphs using <code>networkx</code>.</dd>
      <dd>Implements piecewise multi-stage milestone routing traversing sequential constrained waypoints ($1 \to 4 \to 7 \to 10 \to 11$).</dd>
    </dl>
  </li>
  <li>
    <dl>
      <dt><b>Decision Analysis &amp; Multi-Criteria Prioritization:</b></dt>
      <dd>Evaluates business alternatives under probabilistic risk regimes via Expected Monetary Value (EMV) and Expected Value of Perfect Information (EVPI).</dd>
      <dd>Conducts symbolic boundary sensitivity analysis using <code>sympy</code> to identify dominance probability switching thresholds.</dd>
      <dd>Calculates normalized priority vectors for Analytic Hierarchy Process (AHP / Saaty) pairwise reciprocal comparison matrices.</dd>
    </dl>
  </li>
  <li>
    <dl>
      <dt><b>Empirical Time-Series Forecasting:</b></dt>
      <dd>Applies Naive and sliding-window rolling Moving Averages (2-week and 4-week MA) over sequential demand registrations[span_44](start_span)[span_44](end_span).</dd>
      <dd>Validates model performance and selects optimal forecasting candidates based on Mean Squared Error (MSE).</dd>
    </dl>
  </li>
</ol>

<h2>Project files</h2>
<table>
  <tr>
    <th colspan="2">operations-research-decision-suite</th>
  </tr>
  <tr>
    <td>main.py</td>
    <td>Central CLI orchestrator providing execution routing across all operational sub-modules</td>
  </tr>
  <tr>
    <td>modules/linear_programming.py</td>
    <td>SciPy HiGHS simplex optimizer and Matplotlib feasible-region geometric visualizer</td>
  </tr>
  <tr>
    <td>modules/network_routing.py</td>
    <td>Exact TSP brute-force solver and NetworkX shortest-path / multi-stage waypoint engines</td>
  </tr>
  <tr>
    <td>modules/decision_analysis.py</td>
    <td>Expected monetary value (EMV), EVPI, SymPy symbolic sensitivity, and Saaty AHP priority evaluator</td>
  </tr>
  <tr>
    <td>modules/time_series_analysis.py</td>
    <td>Empirical forecasting routines (Naive, 2-Week MA, 4-Week MA) with MSE validation</td>
  </tr>
  <tr>
    <td>README.md</td>
    <td>Mathematical documentation and operational guide</td>
  </tr>
  <tr>
    <td>.gitignore</td>
    <td>Exclusion rules for Python bytecode, virtual environments, and generated plots</td>
  </tr>
</table>

<h2>Methodological Formulation</h2>
<table>
  <tr>
    <th>Domain</th>
    <th>Algorithm / Criterion</th>
    <th>Analytical Model</th>
  </tr>
  <tr>
    <td><b>Linear Programming</b></td>
    <td>Dual Simplex (HiGHS)</td>
    <td>$\min 2x_1 + 3x_2 \quad \text{s.t.} \quad x_1 + 2x_2 \geq 18, \quad 4x_1 + 3x_2 \geq 48, \quad x_1 \geq 3$</td>
  </tr>
  <tr>
    <td><b>Combinatorics</b></td>
    <td>TSP Enumeration</td>
    <td>$\min_{\pi \in S_n} \sum_{i=1}^{n-1} d(\pi_i, \pi_{i+1}) + d(\pi_n, \pi_1)$</td>
  </tr>
  <tr>
    <td><b>Graph Theory</b></td>
    <td>Dijkstra / Milestones</td>
    <td>$d(u, v) = \min \sum_{(i,j) \in P} w_{ij} \quad \text{across waypoints } \{1, 4, 7, 10, 11\}$</td>
  </tr>
  <tr>
    <td><b>Decision Theory</b></td>
    <td>EMV &amp; EVPI</td>
    <td>$\text{EMV}(A_i) = \sum_j P_j \cdot R_{ij}, \quad \text{EVPI} = \text{EVwPI} - \max_i \text{EMV}(A_i)$</td>
  </tr>
  <tr>
    <td><b>Multi-Criteria</b></td>
    <td>AHP Local Priorities</td>
    <td>$w_i = \frac{1}{n} \sum_{j=1}^n \frac{a_{ij}}{\sum_{k=1}^n a_{kj}}$</td>
  </tr>
  <tr>
    <td><b>Forecasting</b>[</td>
    <td>Rolling MA &amp; MSE</td>
    <td>$\hat{y}_{t} = \frac{1}{k} \sum_{i=1}^k y_{t-i}, \quad \text{MSE} = \frac{1}{n} \sum_{t=1}^n (y_t - \hat{y}_t)^2$</td>
  </tr>
</table>

<h2>Installation and launch</h2>
<ol>
  <b>
    <li>
      <dl>
        <dt>Clone repository</dt>
        <dd>
          <code>git clone https://github.com/Kyoryuu-lab/operations-research-decision-suite.git</code>
        </dd>
        <dd>
          <code>cd operations-research-decision-suite</code>
        </dd>
      </dl>
    </li>
  </b>
  <b>
    <li>
      <dl>
        <dt>Install dependencies</dt>
        <dd>
          <code>pip install numpy scipy networkx sympy pandas matplotlib</code>
        </dd>
      </dl>
    </li>
  </b>
  <b>
    <li>
      <dl>
        <dt>Run complete suite</dt>
        <dd>
          <code>python main.py --module all</code>
        </dd>
        <dd>Run single module with plot saving: <code>python main.py --module lp --save-plots</code></dd>
      </dl>
    </li>
  </b>
</ol>

<h2>Example of console output (python main.py --module all)</h2>
<samp>
  <p>
    ==============================================================================<br />
    &nbsp;&nbsp;1. MODUL: LINEARE PROGRAMMIERUNG &amp; ZULAESSIGER BEREICH<br />
    ==============================================================================<br />
    [*] HiGHS Solver Konvergenz : True<br />
    [*] Optimale Variablenbelegung: x1 = 8.4000, x2 = 4.8000<br />
    [*] Minimaler Zielfunktionswert: 31.2000<br />
    <br />
    ==============================================================================<br />
    &nbsp;&nbsp;2. MODUL: GRAPHENTHEORIE &amp; NETZWERK-ROUTING<br />
    ==============================================================================<br />
    [*] TSP Kuerzeste Rundreise : B0 -&gt; B1 -&gt; B2 -&gt; B3 -&gt; B4 -&gt; B0<br />
    [*] Minimale Gesamtstrecke&nbsp;&nbsp;: 1400 km<br />
    [*] Kuerzester Pfad (1 -&gt; 11) : 1 -&gt; 4 -&gt; 7 -&gt; 10 -&gt; 11<br />
    [*] Minimale Pfadkosten&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: 21<br />
    [*] Meilenstein-Pfad (1-&gt;4-&gt;7-&gt;10-&gt;11): 1 -&gt; 4 -&gt; 7 -&gt; 10 -&gt; 11<br />
    [*] Gesamtlaenge Meilenstein-Route&nbsp;&nbsp;&nbsp;: 27<br />
    <br />
    ==============================================================================<br />
    &nbsp;&nbsp;3. MODUL: ENTSCHEIDUNGSTHEORIE &amp; AHP<br />
    ==============================================================================<br />
    [*] Erwartete Geldwerte (EMV):<br />
    &nbsp;&nbsp;&nbsp;&nbsp;- A1: 10600.00 EUR<br />
    &nbsp;&nbsp;&nbsp;&nbsp;- A2: 11700.00 EUR<br />
    &nbsp;&nbsp;&nbsp;&nbsp;- A3: 6700.00 EUR<br />
    [*] Erwartungswert bei vollkommener Information: 13200.00 EUR<br />
    [*] Wert vollkommener Information (EVPI)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: 1500.00 EUR<br />
    [*] Sensitivitaetsschwelle: Alternative A3 dominiert A1 fuer P_S in: P_S &gt; 0.272727272727273<br />
    <br />
    [*] AHP Lokale Prioritaetsvektoren (A1, A2, A3):<br />
    &nbsp;&nbsp;&nbsp;&nbsp;- Kriterium 1: [0.0818, 0.2364, 0.6818]<br />
    &nbsp;&nbsp;&nbsp;&nbsp;- Kriterium 2: [0.7306, 0.0811, 0.1883]<br />
    &nbsp;&nbsp;&nbsp;&nbsp;- Kriterium 3: [0.2000, 0.6000, 0.2000]<br />
    <br />
    ==============================================================================<br />
    &nbsp;&nbsp;4. MODUL: ZEITREIHENPROGNOSE &amp; MODELL-VALIDIERUNG<br />
    ==============================================================================<br />
    [*] Mittlere quadratische Fehler (MSE):<br />
    &nbsp;&nbsp;&nbsp;&nbsp;- Naive&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: MSE = 23.3333<br />
    &nbsp;&nbsp;&nbsp;&nbsp;- 2-Week MA&nbsp;&nbsp;&nbsp;&nbsp;: MSE = 22.8125<br />
    &nbsp;&nbsp;&nbsp;&nbsp;- 4-Week MA&nbsp;&nbsp;&nbsp;&nbsp;: MSE = 25.1094<br />
    [+] Genauestes Prognosemodell: 2-Week MA<br />
    <br />
    ==============================================================================<br />
    &nbsp;&nbsp;AUSFUEHRUNG ERFOLGREICH ABGESCHLOSSEN.<br />
    ==============================================================================<br />
  </p>
