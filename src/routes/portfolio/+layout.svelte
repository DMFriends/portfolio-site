<main class="portfolio-layout">
  <slot />
</main>

<style>
  .portfolio-layout {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    background: radial-gradient(circle at top left, #1f2933, #020617 45%, #000000 100%);
    color: #e5e7eb;
    font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  }

  :global(body) {
    margin: 0;
    background: #020617;
  }
</style>