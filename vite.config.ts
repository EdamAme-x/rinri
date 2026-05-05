import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// Use polling watcher when running on WSL/Windows-mounted paths,
// where inotify events don't propagate from the Windows filesystem.
const isWslOnWindowsMount = process.cwd().startsWith('/mnt/')

export default defineConfig({
  base: '/',
  plugins: [vue()],
  server: {
    watch: isWslOnWindowsMount
      ? {
          usePolling: true,
          interval: 250,
        }
      : undefined,
  },
  build: {
    target: 'es2022',
    sourcemap: true,
  },
})
