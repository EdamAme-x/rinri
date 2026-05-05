<script setup lang="ts">
const SEARCH_URL = 'https://www.google.com/search?q=%E6%8A%80%E8%A1%93%E8%80%85%E5%80%AB%E7%90%86'
const DISCORD_URL = 'https://discord.gg/evex'
const GITHUB_URL = 'https://github.com/EdamAme-x/rinri'

const SHARE_TEXT = '技術者倫理を守ろう。'
const SHARE_URL = 'https://技術者倫理.com'
const SHARE_HASHTAGS = '技術者倫理'

const X_SHARE_URL =
  'https://twitter.com/intent/tweet' +
  `?text=${encodeURIComponent(SHARE_TEXT)}` +
  `&url=${encodeURIComponent(SHARE_URL)}` +
  `&hashtags=${encodeURIComponent(SHARE_HASHTAGS)}`
</script>

<template>
  <main class="page">
    <section class="hero">
      <p class="eyebrow">Engineering Ethics</p>
      <h1 class="title">技術者倫理を守ろう</h1>
      <p class="lead">エンジニアとしての誠実さを、今日も。</p>

      <div class="actions">
        <a class="btn btn-primary" :href="SEARCH_URL" target="_blank" rel="noopener noreferrer">
          技術者倫理について調べる
          <span class="arrow" aria-hidden="true">→</span>
        </a>

        <a
          class="btn btn-ghost"
          :href="X_SHARE_URL"
          target="_blank"
          rel="noopener noreferrer"
          aria-label="Xで共有する"
        >
          <svg class="x-icon" viewBox="0 0 24 24" width="16" height="16" aria-hidden="true">
            <path
              fill="currentColor"
              d="M18.244 2H21.5l-7.5 8.57L23 22h-6.844l-5.36-6.99L4.6 22H1.34l8.02-9.166L1 2h7.02l4.83 6.39L18.244 2Zm-1.2 18h1.86L7.04 4H5.07L17.044 20Z"
            />
          </svg>
          <span>Xで広める</span>
        </a>
      </div>
    </section>

    <footer class="footer">
      <a class="link" :href="DISCORD_URL" target="_blank" rel="noopener noreferrer">
        discord.gg/evex
      </a>
      <span class="sep" aria-hidden="true">/</span>
      <a class="link" :href="GITHUB_URL" target="_blank" rel="noopener noreferrer">
        github.com/EdamAme-x/rinri
      </a>
    </footer>
  </main>
</template>

<style scoped>
.page {
  min-height: 100dvh;
  display: grid;
  grid-template-rows: 1fr auto;
  padding: 2rem 1.25rem;
  gap: 2rem;
  max-width: 720px;
  margin: 0 auto;
}

.hero {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  gap: 1rem;
}

.eyebrow {
  margin: 0;
  font-size: 0.75rem;
  font-weight: 500;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--muted);
}

.title {
  margin: 0;
  font-size: clamp(2rem, 6vw, 3.5rem);
  font-weight: 700;
  letter-spacing: -0.01em;
  line-height: 1.2;
  color: var(--fg);
}

.lead {
  margin: 0;
  color: var(--muted);
  font-size: clamp(0.95rem, 2.2vw, 1.0625rem);
}

.actions {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  gap: 0.625rem;
  margin-top: 1.25rem;
}

.btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.25rem;
  border-radius: 8px;
  font-weight: 500;
  font-size: 0.9375rem;
  text-decoration: none;
  border: 1px solid transparent;
  transition:
    background-color 120ms ease,
    border-color 120ms ease,
    color 120ms ease,
    transform 120ms ease;
}

.btn:active {
  transform: translateY(1px);
}

.btn-primary {
  background: var(--fg);
  color: var(--bg);
}

.btn-primary:hover {
  background: color-mix(in srgb, var(--fg) 88%, var(--bg));
}

.btn-ghost {
  background: transparent;
  color: var(--fg);
  border-color: var(--border);
}

.btn-ghost:hover {
  background: var(--hairline);
  border-color: var(--fg);
}

.arrow {
  transition: transform 120ms ease;
}

.btn-primary:hover .arrow {
  transform: translateX(2px);
}

.x-icon {
  display: block;
  flex-shrink: 0;
}

.footer {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.75rem;
  flex-wrap: wrap;
  padding: 1.5rem 0 0.5rem;
  border-top: 1px solid var(--hairline);
  color: var(--muted);
  font-size: 0.875rem;
}

.link {
  color: inherit;
  text-decoration: none;
  transition: color 120ms ease;
}

.link:hover {
  color: var(--fg);
}

.sep {
  opacity: 0.5;
  user-select: none;
}
</style>
