<svelte:head>
  <title>Portfolio | Daniel Miretsky</title>
  <meta name="description" content="Showcase of projects and experience." />
</svelte:head>

<section class="hero">
  <div class="hero-inner">
    <div class="hero-text">
      <a href="/" class="back-link">← Back</a>
      <p class="eyebrow">Portfolio</p>
    </div>
  </div>
</section>

<section id="projects" class="section">
  <div class="section-header">
    <h2>My Coding Projects</h2>
    <p>
      A curated selection of my coding projects.
    </p>
  </div>

  <div class="grid">
    <article class="card project">
      <div class="card-tag">Featured</div>
      <h3>Project One</h3>
      <p class="card-subtitle">
        A brief description of the project, what you built, and why it’s interesting.
      </p>
      <ul class="pill-list">
        <li>SvelteKit</li>
        <li>TypeScript</li>
        <li>Tailwind CSS</li>
      </ul>
      <div class="card-footer">
        <a href="#" class="link">Live site</a>
        <a href="#" class="link">Source code</a>
      </div>
    </article>

    <article class="card project">
      <h3>Project Two</h3>
      <p class="card-subtitle">
        Focus on the problem you solved, your role, and measurable impact where possible.
      </p>
      <ul class="pill-list">
        <li>Node.js</li>
        <li>REST APIs</li>
        <li>PostgreSQL</li>
      </ul>
      <div class="card-footer">
        <a href="#" class="link">Case study</a>
      </div>
    </article>

    <article class="card project">
      <h3>Project Three</h3>
      <p class="card-subtitle">
        Include personal experiments, open source work, or learning projects you’re proud of.
      </p>
      <ul class="pill-list">
        <li>Design systems</li>
        <li>Storybook</li>
        <li>Testing</li>
      </ul>
      <div class="card-footer">
        <a href="#" class="link">View details</a>
      </div>
    </article>
  </div>
</section>

<section id="open-source" class="section">
  <div class="section-header">
    <h2>My Open Source Contributions</h2>
    <p>
      A curated selection of my open source contributions.
    </p>
  </div>

  <div class="grid">
    <article class="card project">
      <div class="card-tag">Featured</div>
      <h3>Project One</h3>
      <p class="card-subtitle">
        A brief description of the project, what you built, and why it’s interesting.
      </p>
      <ul class="pill-list">
        <li>SvelteKit</li>
        <li>TypeScript</li>
        <li>Tailwind CSS</li>
      </ul>
      <div class="card-footer">
        <a href="#" class="link">Live site</a>
        <a href="#" class="link">Source code</a>
      </div>
    </article>

    <article class="card project">
      <h3>Project Two</h3>
      <p class="card-subtitle">
        Focus on the problem you solved, your role, and measurable impact where possible.
      </p>
      <ul class="pill-list">
        <li>Node.js</li>
        <li>REST APIs</li>
        <li>PostgreSQL</li>
      </ul>
      <div class="card-footer">
        <a href="#" class="link">Case study</a>
      </div>
    </article>

    <article class="card project">
      <h3>Project Three</h3>
      <p class="card-subtitle">
        Include personal experiments, open source work, or learning projects you’re proud of.
      </p>
      <ul class="pill-list">
        <li>Design systems</li>
        <li>Storybook</li>
        <li>Testing</li>
      </ul>
      <div class="card-footer">
        <a href="#" class="link">View details</a>
      </div>
    </article>
  </div>
</section>

<section id="skills" class="section section-alt">
  <div class="skills-container">
    <h3>Skills</h3>
    <ul class="pill-list">
      <li>JavaScript / TypeScript</li>
      <li>Svelte / SvelteKit</li>
      <li>React</li>
      <li>Node.js</li>
      <li>UX & accessibility</li>
      <li>Testing</li>
    </ul>
  </div>
</section>

<footer class="footer">
  <span>© {new Date().getFullYear()} Daniel Miretsky. All rights reserved.</span>
</footer>

<style>
  section {
    width: 100%;
  }

  .hero {
    padding: 2rem 1.5rem 0rem;
  }

  .hero-inner {
    max-width: 1120px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: minmax(0, 2fr) minmax(0, 1.4fr);
    gap: 3rem;
    align-items: center;
  }

  .eyebrow {
    letter-spacing: 0.13em;
    text-transform: uppercase;
    font-size: 0.75rem;
    color: #9ca3af;
  }

  .back-link {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    color: #e5e7eb;
    text-decoration: none;
    border: 1px solid rgba(148, 163, 184, 0.35);
    background: rgba(15, 23, 42, 0.55);
    padding: 0.35rem 0.75rem;
    border-radius: 999px;
    font-size: 0.85rem;
    width: fit-content;
    margin-bottom: 0.75rem;
    transition: background 0.2s ease, border-color 0.2s ease, transform 0.1s ease;
  }

  .back-link:hover {
    background: rgba(30, 64, 175, 0.45);
    border-color: rgba(129, 140, 248, 0.6);
    transform: translateY(-1px);
  }

  .section {
    padding: 2.5rem 1.5rem;
  }

  .section-alt {
    background: radial-gradient(circle at top, rgba(15, 23, 42, 0.9), rgba(15, 23, 42, 0.3));
  }

  .section-header {
    max-width: 1120px;
    margin: 0 auto 1.75rem;
  }

  .section-header h2 {
    margin: 0 0 0.5rem;
    font-size: 1.4rem;
  }

  .section-header p {
    margin: 0;
    color: #9ca3af;
    max-width: 32rem;
  }

  .grid {
    max-width: 1120px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 1.5rem;
  }

  .card {
    background: rgba(15, 23, 42, 0.9);
    border-radius: 1rem;
    padding: 1.35rem 1.4rem 1.3rem;
    border: 1px solid rgba(148, 163, 184, 0.25);
    box-shadow: 0 18px 45px rgba(15, 23, 42, 0.85);
    display: flex;
    flex-direction: column;
    gap: 0.7rem;
  }

  .card-tag {
    display: inline-flex;
    align-items: center;
    padding: 0.2rem 0.65rem;
    border-radius: 999px;
    font-size: 0.7rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    background: rgba(22, 163, 74, 0.15);
    color: #4ade80;
    border: 1px solid rgba(34, 197, 94, 0.4);
    align-self: flex-start;
  }

  .project h3 {
    margin: 0;
    font-size: 1.05rem;
  }

  .card-subtitle {
    margin: 0;
    color: #9ca3af;
    font-size: 0.9rem;
  }

  .pill-list {
    list-style: none;
    padding: 0;
    margin: 0.2rem 0 0.4rem;
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
  }

  .pill-list li {
    padding: 0.25rem 0.6rem;
    border-radius: 999px;
    border: 1px solid rgba(148, 163, 184, 0.35);
    font-size: 0.75rem;
    color: #e5e7eb;
    background: rgba(15, 23, 42, 0.8);
  }

  .card-footer {
    margin-top: auto;
    display: flex;
    gap: 1rem;
    font-size: 0.85rem;
  }

  .link {
    color: #38bdf8;
    text-decoration: none;
    position: relative;
  }

  .link::after {
    content: "";
    position: absolute;
    left: 0;
    bottom: -0.1rem;
    width: 0;
    height: 1px;
    background: #38bdf8;
    transition: width 0.2s ease;
  }

  .link:hover::after {
    width: 100%;
  }

  .skills-container {
    max-width: 1120px;
    margin: 0 auto;
    display: grid;
    gap: 0.5rem;
  }

  .skills-container h3 {
    margin: 0 0 0.5rem;
    font-size: 1rem;
  }

  .footer {
    padding: 1.5rem;
    border-top: 1px solid rgba(31, 41, 55, 0.85);
    text-align: center;
    font-size: 0.8rem;
    color: #ffffff;
    font-family: "Montserrat", sans-serif;
  }

  /* Responsive */
  @media (max-width: 960px) {
    .hero-inner {
      grid-template-columns: minmax(0, 1fr);
    }

    .grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .skills-container {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 1rem;
      margin-top: 1rem;
      margin-bottom: 1rem;
      margin-left: 1rem;
      margin-right: 1rem;
      padding-top: 1rem;
      padding-bottom: 1rem;
    }
  }

  @media (max-width: 640px) {
    .hero {
      padding-top: 3rem;
      padding-bottom: 2.5rem;
    }

    .section {
      padding-inline: 1.25rem;
    }

    .grid {
      grid-template-columns: minmax(0, 1fr);
    }
  }
</style>