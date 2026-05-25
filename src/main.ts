import { ViteSSG } from 'vite-ssg/single-page'
import App from './App.vue'
import './styles.css'

export const createApp = ViteSSG(App, ({ isClient }) => {
  if (!isClient) return

  const banner = '%c⚠ 開発者タブを閉じてください！'
  const sub = '%cソースを覗くのは技術者倫理違反です！！\n— 技術者倫理.com'

  console.log(
    banner + '\n' + sub,
    'color:#ff3b3b;font-size:28px;font-weight:800;letter-spacing:0.04em;',
    'color:#ff3b3b;font-size:15px;font-weight:700;line-height:1.6;',
  )
})
