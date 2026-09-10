// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import catppuccin from '@catppuccin/starlight';

const SITE = 'https://htlin222.github.io';
const BASE = '/hema-board-interview-guide';
const OG_IMAGE = `${SITE}${BASE}/og.png`;

// https://astro.build/config
export default defineConfig({
	site: SITE,
	base: BASE,
	integrations: [
		starlight({
			title: '血液科口試走向指南',
			description: '整理歷屆考生心得，去名化後的口試主題、典型問答流程與準備策略',
			social: [],
			customCss: ['./src/styles/custom.css'],
			favicon: '/favicon.svg',
			head: [
				// Starlight 自己會出 og:title / og:description / og:url，這裡補圖片與卡片格式
				{ tag: 'meta', attrs: { property: 'og:image', content: OG_IMAGE } },
				{ tag: 'meta', attrs: { property: 'og:image:width', content: '1200' } },
				{ tag: 'meta', attrs: { property: 'og:image:height', content: '630' } },
				{
					tag: 'meta',
					attrs: {
						property: 'og:image:alt',
						content: '血液科口試走向指南：推理架構 × 破題關鍵句 × 擬答 × 追問',
					},
				},
				{ tag: 'meta', attrs: { property: 'og:type', content: 'website' } },
				{ tag: 'meta', attrs: { name: 'twitter:card', content: 'summary_large_image' } },
				{ tag: 'meta', attrs: { name: 'twitter:image', content: OG_IMAGE } },
				// 不支援 SVG favicon 的瀏覽器用 PNG 遞補
				{
					tag: 'link',
					attrs: { rel: 'icon', type: 'image/png', sizes: '32x32', href: `${BASE}/favicon-32.png` },
				},
				{
					tag: 'link',
					attrs: { rel: 'apple-touch-icon', sizes: '180x180', href: `${BASE}/apple-touch-icon.png` },
				},
				{ tag: 'meta', attrs: { name: 'theme-color', content: '#1e1e2e' } },
			],
			plugins: [
				catppuccin({
					dark: { flavor: 'mocha', accent: 'mauve' },
					light: { flavor: 'latte', accent: 'mauve' },
				}),
			],
			sidebar: [
				{
					label: '總覽',
					link: '/',
				},
				{
					label: '主題別考點',
					items: [{ autogenerate: { directory: 'topics' } }],
				},
				{
					label: '一頁速查（可列印）',
					link: '/handout/',
					attrs: { target: '_blank' },
				},
			],
		}),
	],
});
