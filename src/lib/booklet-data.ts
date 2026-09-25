/**
 * 手冊的資料來源（A4 與 A5 兩個版本共用）：
 * - `src/booklet/pages/*.md`：每檔一章（A4 版一章一張；A5 版一章自動分成數頁）
 * - `src/booklet/doses/*.md`：劑量總表，依 DOSE_SHEETS 分組
 * 兩個版本讀同一份資料，改內容只要改 md，兩邊重新建置就同步。
 */
import { loadSheets, loadDoses } from './booklet';

// 手冊正文：每檔一章
const pageFiles = import.meta.glob('/src/booklet/pages/*.md', {
	query: '?raw',
	import: 'default',
	eager: true,
}) as Record<string, string>;
export const sheets = loadSheets(pageFiles);

// 劑量表：跟主題頁「參考劑量」段落是同一份來源
const doseFiles = import.meta.glob('/src/booklet/doses/*.md', {
	query: '?raw',
	import: 'default',
	eager: true,
}) as Record<string, string>;
const doses = loadDoses(doseFiles);
// 劑量總表分組：A4 版每組一張，內容多的章節（malignancy）拆開才塞得下
const DOSE_SHEETS: { id: string; title: string; slugs: string[] }[] = [
	{
		id: 'doses-anemia',
		title: '參考劑量總表 I · 貧血與鐵',
		slugs: ['hemolytic-anemia-basics', 'iron-deficiency-anemia', 'thalassemia-iron-overload'],
	},
	{
		id: 'doses-platelet',
		title: '參考劑量總表 II · 血小板',
		slugs: ['itp', 'ttp-tma-evans', 'thrombocytosis-mpn'],
	},
	{
		id: 'doses-hemostasis',
		title: '參考劑量總表 III · 出血與血栓',
		slugs: ['bleeding-workup-hemophilia', 'cancer-associated-thrombosis'],
	},
	{
		id: 'doses-myeloid',
		title: '參考劑量總表 IV · AML、MDS、CML',
		slugs: ['aml-mds-cml'],
	},
	{
		id: 'doses-lymphoid',
		title: '參考劑量總表 V · ALL 與 Lymphoma',
		slugs: ['all-leukemia', 'lymphoma-treatment-lines'],
	},
	{
		id: 'doses-myeloma',
		title: '參考劑量總表 VI · Myeloma',
		slugs: ['myeloma-and-transplant'],
	},
];
export const doseSheets = DOSE_SHEETS.map((d, j) => ({
	id: d.id,
	title: d.title,
	kicker: `${String(sheets.length + j + 1).padStart(2, '0')} · 劑量`,
	groups: d.slugs.map((slug) => doses.find((x) => x.slug === slug)).filter((x): x is NonNullable<typeof x> => !!x),
}));
