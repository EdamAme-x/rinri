<script setup lang="ts">
import { ref } from 'vue'
import { ArrowRight, Check, ChevronRight, Copy } from 'lucide-vue-next'
import { XIcon, DiscordIcon, GitHubIcon } from 'vue3-simple-icons'

const SEARCH_URL = 'https://www.google.com/search?q=%E6%8A%80%E8%A1%93%E8%80%85%E5%80%AB%E7%90%86'
const ACM_CODE_URL = 'https://www.acm.org/binaries/content/assets/code-of-ethics/se-code-jpn.pdf'
const ACM_CODE_MD_URL = 'https://github.com/EdamAme-x/rinri/blob/main/docs/se-code-jpn.md'
const DISCORD_URL = 'https://discord.gg/evex'
const GITHUB_URL = 'https://github.com/EdamAme-x/rinri'
const SITE_URL = 'https://技術者倫理.com'

const SHARE_TEXT = '技術者倫理を守ろう。'
const SHARE_HASHTAGS = '技術者倫理'

const X_SHARE_URL =
  'https://twitter.com/intent/tweet' +
  `?text=${encodeURIComponent(SHARE_TEXT)}` +
  `&url=${encodeURIComponent(SITE_URL)}` +
  `&hashtags=${encodeURIComponent(SHARE_HASHTAGS)}`

// shields.io static badge — black text on white label, links to the site
const BADGE_IMG_URL =
  'https://img.shields.io/badge/' +
  encodeURIComponent('技術者倫理') +
  '-' +
  encodeURIComponent('遵守済み') +
  '-0a0a0a?style=for-the-badge&labelColor=ffffff'

const BADGE_MD = `[![技術者倫理 遵守済み](${BADGE_IMG_URL})](${SITE_URL})`
const BADGE_HTML = `<a href="${SITE_URL}"><img src="${BADGE_IMG_URL}" alt="技術者倫理 遵守済み" /></a>`

type SnippetKind = 'md' | 'html'

const snippetKind = ref<SnippetKind>('md')
const snippets: Record<SnippetKind, string> = {
  md: BADGE_MD,
  html: BADGE_HTML,
}

const copied = ref(false)
let copyTimer: number | undefined

async function copySnippet() {
  const text = snippets[snippetKind.value]
  try {
    await navigator.clipboard.writeText(text)
  } catch {
    const ta = document.createElement('textarea')
    ta.value = text
    ta.style.position = 'fixed'
    ta.style.opacity = '0'
    document.body.appendChild(ta)
    ta.select()
    document.execCommand('copy')
    document.body.removeChild(ta)
  }
  copied.value = true
  if (copyTimer) window.clearTimeout(copyTimer)
  copyTimer = window.setTimeout(() => (copied.value = false), 1600)
}
</script>

<template>
  <main class="page">
    <section class="hero">
      <p class="eyebrow"><span class="eyebrow-text">Engineering Ethics</span></p>
      <h1 class="title">技術者倫理を守ろう</h1>

      <p class="sr-only">技術者倫理を守ろう。</p>

      <div class="actions">
        <a class="btn btn-primary" :href="SEARCH_URL" target="_blank" rel="noopener noreferrer">
          <span>技術者倫理について調べる</span>
          <ArrowRight class="arrow" :size="16" aria-hidden="true" />
        </a>

        <a
          class="btn btn-ghost"
          :href="X_SHARE_URL"
          target="_blank"
          rel="noopener noreferrer"
          aria-label="Xで共有する"
        >
          <XIcon :size="16" aria-hidden="true" />
          <span>Xで広める</span>
        </a>
      </div>

      <p class="reference">
        <a class="link" :href="ACM_CODE_URL" target="_blank" rel="noopener noreferrer">
          ACM ソフトウェアエンジニア倫理綱領
        </a>
        <a
          class="link reference-md"
          :href="ACM_CODE_MD_URL"
          target="_blank"
          rel="noopener noreferrer"
        >
          ( Markdown版 )
        </a>
      </p>
    </section>

    <section class="badge-section">
      <details class="badge-details">
        <summary class="badge-summary">
          <ChevronRight class="badge-summary-caret" :size="14" aria-hidden="true" />
          <span>README に貼れるバッジ</span>
        </summary>

        <div class="badge-body">
          <a class="badge-preview" :href="SITE_URL" rel="noopener noreferrer">
            <img :src="BADGE_IMG_URL" alt="技術者倫理 遵守済み" width="200" height="28" />
          </a>

          <div class="snippet">
            <div class="snippet-head">
              <label class="snippet-select">
                <select v-model="snippetKind" aria-label="フォーマット">
                  <option value="md">Markdown</option>
                  <option value="html">HTML</option>
                </select>
                <span class="snippet-select-caret" aria-hidden="true">▾</span>
              </label>
              <button
                type="button"
                class="snippet-copy"
                :aria-label="copied ? 'コピーしました' : 'コピー'"
                @click="copySnippet"
              >
                <Check v-if="copied" :size="14" aria-hidden="true" />
                <Copy v-else :size="14" aria-hidden="true" />
                <span>{{ copied ? 'Copied' : 'Copy' }}</span>
              </button>
            </div>
            <pre class="snippet-code"><code>{{ snippets[snippetKind] }}</code></pre>
          </div>
        </div>
      </details>
    </section>

    <footer class="footer">
      <a
        class="icon-link"
        :href="DISCORD_URL"
        target="_blank"
        rel="noopener noreferrer"
        aria-label="Discord (evex)"
        title="discord.gg/evex"
      >
        <DiscordIcon :size="20" aria-hidden="true" />
      </a>

      <span class="sep" aria-hidden="true">/</span>

      <a
        class="icon-link"
        :href="GITHUB_URL"
        target="_blank"
        rel="noopener noreferrer"
        aria-label="GitHub (EdamAme-x/rinri)"
        title="github.com/EdamAme-x/rinri"
      >
        <GitHubIcon :size="20" aria-hidden="true" />
      </a>
    </footer>
  </main>
</template>

<style scoped>
.page {
  min-height: 100dvh;
  display: grid;
  grid-template-rows: 1fr auto auto;
  padding: 2rem 1.25rem calc(1.25rem + env(safe-area-inset-bottom));
  padding-left: max(1.25rem, env(safe-area-inset-left));
  padding-right: max(1.25rem, env(safe-area-inset-right));
  gap: 2rem;
  max-width: 720px;
  margin: 0 auto;
}

.hero {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  gap: 1rem;
}

.eyebrow {
  margin: 0 0 -0.65rem;
  font-family: 'Great Vibes', 'Snell Roundhand', 'Zapfino', 'Brush Script MT', cursive;
  font-size: clamp(1.45rem, 4vw, 2.05rem);
  font-weight: 400;
  letter-spacing: 0;
  line-height: 1;
  color: var(--muted);
  animation: eyebrow-reveal 700ms cubic-bezier(0.22, 1, 0.36, 1) both;
}

.eyebrow-text {
  position: relative;
  display: inline-block;
  background: linear-gradient(110deg, var(--muted) 10%, var(--fg) 44%, var(--muted) 72%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.eyebrow-text::before {
  content: '';
  position: absolute;
  inset: -0.25rem -0.35rem;
  background: linear-gradient(
    105deg,
    transparent 32%,
    rgba(255, 255, 255, 0.88) 50%,
    transparent 68%
  );
  transform: translateX(-120%) skewX(-18deg);
  animation: eyebrow-shine 900ms cubic-bezier(0.22, 1, 0.36, 1) 160ms both;
  mix-blend-mode: screen;
  pointer-events: none;
}

.eyebrow-text::after {
  content: '✦';
  position: absolute;
  top: -0.45rem;
  right: -0.85rem;
  color: var(--fg);
  font-family: Georgia, serif;
  font-size: 0.95rem;
  line-height: 1;
  text-shadow: 0 0 14px color-mix(in srgb, var(--fg) 36%, transparent);
  transform-origin: center;
  animation: eyebrow-spark 820ms cubic-bezier(0.16, 1, 0.3, 1) 520ms both;
  pointer-events: none;
}

.title {
  margin: 0;
  font-size: clamp(1.6rem, 7.5vw, 3.75rem);
  font-weight: 700;
  letter-spacing: -0.01em;
  line-height: 1.2;
  color: var(--fg);
  word-break: keep-all;
  overflow-wrap: anywhere;
  text-shadow: 0 1px 0 rgba(255, 255, 255, 0.6);
}

@media (prefers-color-scheme: dark) {
  .title {
    text-shadow: 0 1px 0 rgba(0, 0, 0, 0.6);
  }
}

.eyebrow::before,
.eyebrow::after {
  display: none;
}

@keyframes eyebrow-reveal {
  from {
    opacity: 0;
    transform: translateY(0.35rem) scale(0.98);
    filter: blur(4px);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
    filter: blur(0);
  }
}

@keyframes eyebrow-shine {
  0% {
    opacity: 0;
    transform: translateX(-120%) skewX(-18deg);
  }
  18% {
    opacity: 1;
  }
  100% {
    opacity: 0;
    transform: translateX(120%) skewX(-18deg);
  }
}

@keyframes eyebrow-spark {
  0% {
    opacity: 0;
    transform: scale(0.2) rotate(-35deg);
  }
  35% {
    opacity: 1;
    transform: scale(1.35) rotate(8deg);
  }
  100% {
    opacity: 0;
    transform: scale(0.75) rotate(28deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .eyebrow,
  .eyebrow-text::before,
  .eyebrow-text::after {
    animation: none;
  }

  .eyebrow-text::before,
  .eyebrow-text::after {
    opacity: 0;
  }
}

.actions {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  gap: 0.625rem;
  margin-top: 1.5rem;
  width: 100%;
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.75rem 1.4rem;
  border-radius: 999px;
  font-weight: 500;
  font-size: 0.9375rem;
  text-decoration: none;
  border: 1px solid transparent;
  -webkit-tap-highlight-color: transparent;
  touch-action: manipulation;
  transition:
    background-color 150ms ease,
    border-color 150ms ease,
    color 150ms ease,
    transform 150ms ease,
    box-shadow 150ms ease;
}

.btn:active {
  transform: translateY(0);
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.08);
}

.btn-primary {
  background: var(--fg);
  color: var(--bg);
  box-shadow:
    0 1px 2px rgba(0, 0, 0, 0.08),
    0 4px 12px -4px rgba(0, 0, 0, 0.18);
}

.btn-primary:hover {
  background: color-mix(in srgb, var(--fg) 88%, var(--bg));
  transform: translateY(-1px);
  box-shadow:
    0 1px 2px rgba(0, 0, 0, 0.1),
    0 8px 18px -6px rgba(0, 0, 0, 0.25);
}

.btn-ghost {
  background: var(--bg);
  color: var(--fg);
  border-color: var(--border);
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.04);
}

.btn-ghost:hover {
  background: var(--hairline);
  border-color: var(--fg);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px -6px rgba(0, 0, 0, 0.15);
}

.arrow {
  transition: transform 120ms ease;
}

.btn-primary:hover .arrow {
  transform: translateX(2px);
}

.btn :deep(svg) {
  display: block;
  flex-shrink: 0;
}

.x-icon {
  display: block;
  flex-shrink: 0;
}

.reference {
  margin: 1rem 0 0;
  font-size: 0.8125rem;
  color: var(--muted);
  letter-spacing: 0.01em;
}

.reference-md {
  margin-left: 0.4rem;
  opacity: 0.85;
}

.badge-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1.25rem 0 0.5rem;
  border-top: 1px solid var(--hairline);
  text-align: center;
}

.badge-details {
  width: 100%;
  max-width: 560px;
}

.badge-summary {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.45rem 0.85rem;
  margin: 0 auto;
  border: 1px solid var(--border);
  border-radius: 999px;
  background: var(--bg);
  color: var(--muted);
  font-size: 0.8125rem;
  font-weight: 500;
  list-style: none;
  cursor: pointer;
  user-select: none;
  -webkit-tap-highlight-color: transparent;
  transition:
    color 150ms ease,
    border-color 150ms ease,
    background-color 150ms ease;
}

.badge-summary::-webkit-details-marker {
  display: none;
}

.badge-summary:hover {
  color: var(--fg);
  border-color: var(--fg);
}

.badge-summary-caret {
  transition: transform 200ms ease;
}

.badge-details[open] > .badge-summary {
  color: var(--fg);
  border-color: var(--fg);
}

.badge-details[open] > .badge-summary .badge-summary-caret {
  transform: rotate(90deg);
}

.badge-body {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.5rem;
  padding-top: 1.5rem;
}

.badge-preview {
  display: inline-block;
  margin: 0.5rem 0;
  border-radius: 4px;
  -webkit-tap-highlight-color: transparent;
  transition:
    transform 150ms ease,
    filter 150ms ease;
  /* light mode: grey shadow under the badge */
  filter: drop-shadow(0 4px 10px rgba(0, 0, 0, 0.18));
}

.badge-preview:hover {
  transform: translateY(-1px);
  filter: drop-shadow(0 8px 16px rgba(0, 0, 0, 0.25));
}

.badge-preview:active {
  transform: translateY(0);
}

.badge-preview img {
  display: block;
  height: 28px;
  width: auto;
}

@media (prefers-color-scheme: dark) {
  /* dark mode: white glow so the badge separates from the dark page */
  .badge-preview {
    filter: drop-shadow(0 4px 12px rgba(255, 255, 255, 0.18));
  }
  .badge-preview:hover {
    filter: drop-shadow(0 8px 20px rgba(255, 255, 255, 0.28));
  }
}

.snippet {
  width: 100%;
  max-width: 560px;
  border: 1px solid var(--border);
  border-radius: 10px;
  background: var(--code-bg);
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.04);
  overflow: hidden;
  text-align: left;
}

.snippet-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
  padding: 0.65rem 0.75rem;
  border-bottom: 1px solid var(--border);
  background: var(--code-head-bg);
}

.snippet-select {
  position: relative;
  display: inline-flex;
  align-items: center;
}

.snippet-select select {
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  padding: 0.5rem 1.75rem 0.5rem 0.8rem;
  border: 1px solid var(--border);
  border-radius: 6px;
  background: var(--bg);
  color: var(--fg);
  font: inherit;
  font-size: 0.75rem;
  font-weight: 500;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
  transition:
    border-color 120ms ease,
    background-color 120ms ease;
}

.snippet-select select:hover {
  border-color: var(--fg);
}

.snippet-select select:focus-visible {
  outline: 2px solid var(--fg);
  outline-offset: 2px;
}

.snippet-select-caret {
  position: absolute;
  right: 0.5rem;
  pointer-events: none;
  font-size: 0.65rem;
  color: var(--muted);
}

.snippet-copy {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.5rem 0.85rem;
  border: 1px solid var(--border);
  border-radius: 6px;
  background: var(--bg);
  color: var(--fg);
  font-size: 0.75rem;
  font-weight: 500;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
  transition:
    background-color 120ms ease,
    border-color 120ms ease,
    color 120ms ease,
    transform 120ms ease;
}

.snippet-copy:hover {
  border-color: var(--fg);
  transform: translateY(-1px);
}

.snippet-copy:active {
  transform: translateY(0);
}

.snippet-copy :deep(svg) {
  display: block;
}

.snippet-code {
  margin: 0;
  padding: 1.1rem 1.1rem;
  font-family:
    ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace;
  font-size: 0.78rem;
  line-height: 1.7;
  color: var(--fg);
  white-space: pre-wrap;
  word-break: break-all;
  overflow-x: auto;
}

.snippet-code code {
  font: inherit;
  color: inherit;
}

.footer {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.25rem;
  flex-wrap: wrap;
  padding: 1.5rem 0 0.5rem;
  border-top: 1px solid var(--hairline);
  color: var(--muted);
  font-size: 0.875rem;
  text-align: center;
}

.link {
  color: inherit;
  text-decoration: none;
  border-bottom: 1px dashed currentColor;
  padding-bottom: 1px;
  -webkit-tap-highlight-color: transparent;
  transition:
    color 150ms ease,
    border-color 150ms ease;
}

.link:hover {
  color: var(--fg);
  border-bottom-color: currentColor;
}

.icon-link {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  border-radius: 999px;
  color: var(--muted);
  -webkit-tap-highlight-color: transparent;
  transition:
    color 150ms ease,
    background-color 150ms ease,
    transform 150ms ease;
}

.icon-link:hover {
  color: var(--fg);
  background: var(--hairline);
  transform: translateY(-1px);
}

.icon-link :deep(svg) {
  display: block;
}

.sep {
  opacity: 0.5;
  user-select: none;
}

@media (max-width: 480px) {
  .page {
    padding: 1.5rem 1rem calc(1rem + env(safe-area-inset-bottom));
    gap: 1.25rem;
  }

  .actions {
    flex-direction: column;
    align-items: stretch;
    gap: 0.5rem;
  }

  .btn {
    width: 100%;
    padding: 0.85rem 1.25rem;
    font-size: 1rem;
  }

  .footer {
    font-size: 0.8125rem;
    padding-top: 1.25rem;
  }
}

@media (hover: none) {
  .btn-primary:hover,
  .btn-ghost:hover {
    transform: none;
  }
  .btn-primary:hover .arrow {
    transform: none;
  }
}
</style>
