/**
 * 從主題頁的 markdown 原文抽出「印成 A4 隨身帶」需要的部分。
 *
 * 取捨原則：handout 是另一種產物，不是全文的列印版。只留**能自己生出答案**的東西——
 * 推理架構、每題的破題關鍵句、速記表、陷阱；擬答與影片留在網站上看。
 */

/** 移除行內 SVG 圖示：紙上印出來沒有顏色，圖示只會佔位。 */
export function stripIcons(md: string): string {
	return md.replace(/<svg[\s\S]*?<\/svg>\s*/g, '');
}

type Section = { heading: string; body: string };

/** 依 `## ` 切段。回傳的 heading 已去除圖示。 */
function splitSections(md: string): Section[] {
	const out: Section[] = [];
	const re = /^## (.+)$/gm;
	const marks: { title: string; start: number; end: number }[] = [];
	let m: RegExpExecArray | null;
	while ((m = re.exec(md))) {
		marks.push({ title: m[1], start: m.index, end: m.index + m[0].length });
	}
	marks.forEach((mk, i) => {
		const bodyEnd = i + 1 < marks.length ? marks[i + 1].start : md.length;
		out.push({
			heading: stripIcons(mk.title).trim(),
			body: md.slice(mk.end, bodyEnd).trim(),
		});
	});
	return out;
}

export type Handout = {
	frameworks: Section[];
	tables: string | null;
	openers: { question: string; line: string }[];
	pitfalls: string | null;
};

/** 破題關鍵句 callout 的內容（去掉外層 div 與標題列）。 */
function openerText(block: string): string {
	const inner = block
		.replace(/<div class="callout callout-keywords">/, '')
		.replace(/<div class="callout-title">[\s\S]*?<\/div>/, '')
		.replace(/<\/div>\s*$/, '');
	const text = stripIcons(inner).replace(/\s+/g, ' ').trim();
	// 紙本只留引號裡那句；後面「——為什麼要這樣開場」的解釋留在網站上。
	const quoted = text.match(/^[「『]([\s\S]*?)[」』]/);
	return quoted ? quoted[1].trim() : text.replace(/\s*——[\s\S]*$/, '').trim();
}

/** 題目標題：支援 `**Q: …**`、`**Q1：…**`、`**1. …**` 幾種寫法，也接受粗體論點當標題。 */
function questionTitle(raw: string): string {
	return stripIcons(raw)
		.replace(/^\*\*/, '')
		.replace(/\*\*$/, '')
		.replace(/^Q\d*[:：]\s*/, '')
		.replace(/^\d+\.\s*/, '')
		.replace(/[？?]$/, '')
		.trim()
		// 紙上只需要認得出是哪一題，過長的題目截短（盡量斷在標點）
		.replace(/^(.{16,30}?)[，。；、—]\s*.+$/, '$1…')
		.replace(/^(.{30}).+$/, '$1…');
}

export function extractHandout(md: string): Handout {
	const sections = splitSections(md);

	const frameworks = sections.filter((s) => /推理架構|框架|核心邏輯/.test(s.heading));
	const tables = sections.find((s) => s.heading.includes('速記表'))?.body ?? null;
	const pitfalls = sections.find((s) => s.heading.includes('容易被電'))?.body ?? null;

	// 破題關鍵句：往前找最近的一個題目標題當它的題名
	const openers: { question: string; line: string }[] = [];
	// 注意：有些頁面的問答包在編號清單裡，callout 整塊是縮排的，
	// 所以結尾的 </div> 前面可能有空白，不能寫死成 \n\n</div>。
	const calloutRe =
		/<div class="callout callout-keywords">[\s\S]*?<\/div>\s*\n\s*\n[\s\S]*?\n\s*\n\s*<\/div>/g;
	let c: RegExpExecArray | null;
	while ((c = calloutRe.exec(md))) {
		const before = md.slice(0, c.index);
		const titles = [
			...before.matchAll(/^\s*(?:-\s*)?(\*\*(?:Q\d*[:：]|\d+\.)?[^\n*][^\n]*?\*\*)\s*$/gm),
		];
		const last = titles.at(-1);
		openers.push({
			question: last ? questionTitle(last[1]) : '',
			line: openerText(c[0]),
		});
	}

	return { frameworks, tables, openers, pitfalls };
}
