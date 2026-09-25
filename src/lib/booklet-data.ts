/**
 * 手冊的資料來源（A4 與 A5 兩個版本共用）：
 * - `src/booklet/pages/*.md`：每檔一章（A4 版一章一張；A5 版一章自動分成數頁）
 * - `src/booklet/criteria/*.md`：診斷標準總表，依 CRITERIA_SHEETS 分組
 * - `src/booklet/doses/*.md`：劑量總表，依 DOSE_SHEETS 分組
 * 總表的每個 md 以主題頁 slug 命名，同一份內容也由 scripts/sync_doses.py 注入對應主題頁。
 * 兩個版本讀同一份資料，改內容只要改 md，兩邊重新建置就同步。
 */
import { loadSheets, loadDoses } from "./booklet";

// 手冊正文：每檔一章
const pageFiles = import.meta.glob("/src/booklet/pages/*.md", {
	query: "?raw",
	import: "default",
	eager: true,
}) as Record<string, string>;
export const sheets = loadSheets(pageFiles);

// 劑量表：跟主題頁「參考劑量」段落是同一份來源
const doseFiles = import.meta.glob("/src/booklet/doses/*.md", {
	query: "?raw",
	import: "default",
	eager: true,
}) as Record<string, string>;
const doses = loadDoses(doseFiles);
// 劑量總表分組：A4 版每組一張，內容多的章節（malignancy）拆開才塞得下
const DOSE_SHEETS: { id: string; title: string; slugs: string[] }[] = [
	{
		id: "doses-anemia",
		title: "參考劑量總表 I · 貧血與鐵",
		slugs: [
			"hemolytic-anemia-basics",
			"iron-deficiency-anemia",
			"thalassemia-iron-overload",
		],
	},
	{
		id: "doses-platelet",
		title: "參考劑量總表 II · 血小板",
		slugs: ["itp", "ttp-tma-evans", "thrombocytosis-mpn"],
	},
	{
		id: "doses-hemostasis",
		title: "參考劑量總表 III · 出血與血栓",
		slugs: ["bleeding-workup-hemophilia", "cancer-associated-thrombosis"],
	},
	{
		id: "doses-myeloid",
		title: "參考劑量總表 IV · AML、MDS、CML",
		slugs: ["aml-mds-cml"],
	},
	{
		id: "doses-lymphoid",
		title: "參考劑量總表 V · ALL 與 Lymphoma",
		slugs: ["all-leukemia", "lymphoma-treatment-lines"],
	},
	{
		id: "doses-myeloma",
		title: "參考劑量總表 VI · Myeloma",
		slugs: ["myeloma-and-transplant"],
	},
];
/** 總表（診斷標準、參考劑量）：一組 slug 拼成一張。note 是頁首的使用說明，source 是頁尾的同源說明。 */
export type TableSheet = {
	id: string;
	title: string;
	kicker: string;
	note: string | null;
	source: string;
	groups: { slug: string; title: string; body: string }[];
};

// 診斷標準總表：每個疾病群一張，各自先講第一性原理再列標準
const criteriaFiles = import.meta.glob("/src/booklet/criteria/*.md", {
	query: "?raw",
	import: "default",
	eager: true,
}) as Record<string, string>;
// 一份診斷標準可以用 `<!-- page -->` 分成數段，第 2 段起以 `<slug>#2`、`#3` 放進續張
const criteria = loadDoses(criteriaFiles).flatMap((c) =>
	c.body.split(/^<!--\s*page\s*-->\s*$/m).map((body, k) => ({
		slug: k === 0 ? c.slug : `${c.slug}#${k + 1}`,
		title: k === 0 ? c.title : `${c.title}（續）`,
		body: body.trim(),
	})),
);
const CRITERIA_SHEETS: { id: string; title: string; slugs: string[] }[] = [
	{
		id: "criteria-anemia",
		title: "診斷標準總表 I · 貧血與溶血",
		slugs: [
			"iron-deficiency-anemia",
			"thalassemia-iron-overload",
			"hemolytic-anemia-basics",
		],
	},
	{
		id: "criteria-hemostasis",
		title: "診斷標準總表 II · 血小板、凝血與血栓",
		slugs: [
			"itp",
			"ttp-tma-evans",
			"bleeding-workup-hemophilia",
			"cancer-associated-thrombosis",
		],
	},
	{
		id: "criteria-mpn",
		title: "診斷標準總表 III · MPN（PV、ET、PMF）",
		slugs: ["thrombocytosis-mpn"],
	},
	{
		id: "criteria-mpn-2",
		title: "診斷標準總表 III · MPN（續）",
		slugs: ["thrombocytosis-mpn#2"],
	},
	{
		id: "criteria-myeloid",
		title: "診斷標準總表 IV · AML、MDS、CML、ALL",
		slugs: ["aml-mds-cml", "all-leukemia"],
	},
	{
		id: "criteria-myeloid-2",
		title: "診斷標準總表 IV · 白血病與 MDS（續）",
		slugs: ["aml-mds-cml#2", "all-leukemia#2"],
	},
	{
		id: "criteria-lymphoma",
		title: "診斷標準總表 V · Lymphoma 與 CLL",
		slugs: ["lymphoma-treatment-lines"],
	},
	{
		id: "criteria-lymphoma-2",
		title: "診斷標準總表 V · Lymphoma 與 CLL（續）",
		slugs: ["lymphoma-treatment-lines#2"],
	},
	{
		id: "criteria-plasma",
		title: "診斷標準總表 VI · 漿細胞疾病",
		slugs: ["myeloma-and-transplant"],
	},
	{
		id: "criteria-plasma-2",
		title: "診斷標準總表 VI · 漿細胞疾病（續）",
		slugs: ["myeloma-and-transplant#2"],
	},
];

function buildSheets(
	defs: { id: string; title: string; slugs: string[] }[],
	pool: { slug: string; title: string; body: string }[],
	start: number,
	tag: string,
	note: string | null,
	source: string,
): TableSheet[] {
	return defs
		.map((d) => ({
			...d,
			groups: d.slugs
				.map((slug) => pool.find((x) => x.slug === slug))
				.filter((x): x is NonNullable<typeof x> => !!x),
		}))
		.filter((d) => d.groups.length > 0) // 還沒寫內容的總表先不出現
		.map((d, j) => ({
			id: d.id,
			title: d.title,
			kicker: `${String(start + j + 1).padStart(2, "0")} · ${tag}`,
			note,
			source,
			groups: d.groups,
		}));
}

export const criteriaSheets = buildSheets(
	CRITERIA_SHEETS,
	criteria,
	sheets.length,
	"診斷標準",
	null,
	"主題頁「診斷標準」段落與本表同源",
);

export const doseSheets = buildSheets(
	DOSE_SHEETS,
	doses,
	sheets.length + criteriaSheets.length,
	"劑量",
	"成人常規參考劑量，答題時講得出「數量級、途徑、頻率、要監測什麼」即可；實際處方以仿單、健保規定與最新指引為準，特殊族群（腎功能、孕婦、兒童）另行查核。",
	"主題頁「參考劑量」段落與本表同源",
);

/** 正文之後的所有總表，依序：診斷標準、參考劑量 */
export const tableSheets: TableSheet[] = [...criteriaSheets, ...doseSheets];
