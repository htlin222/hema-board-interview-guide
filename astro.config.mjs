// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import catppuccin from '@catppuccin/starlight';

// https://astro.build/config
export default defineConfig({
	site: 'https://htlin222.github.io',
	base: '/hema-board-interview-guide',
	integrations: [
		starlight({
			title: '血液科口試走向指南',
			description: '整理歷屆考生心得，去名化後的口試主題、典型問答流程與準備策略',
			social: [],
			customCss: ['./src/styles/custom.css'],
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
			],
		}),
	],
});
