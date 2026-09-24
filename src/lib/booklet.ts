/**
 * 手冊頁面：`src/booklet/pages/*.md` 每檔一張 A4，`src/booklet/doses/*.md` 是劑量表的唯一來源。
 *
 * 這裡只做「讀檔 → 拆 frontmatter → 排序」；渲染交給 marked，版面交給 index.astro 的 CSS。
 */

export type Sheet = {
	id: string;
	title: string;
	kicker: string;
	site: string | null;
	body: string;
};

const FRONT = /^---\s*\n([\s\S]*?)\n---\s*\n?/;

function parseFront(raw: string): { data: Record<string, string>; body: string } {
	const m = raw.match(FRONT);
	if (!m) return { data: {}, body: raw };
	const data: Record<string, string> = {};
	for (const line of m[1].split('\n')) {
		const i = line.indexOf(':');
		if (i < 0) continue;
		const k = line.slice(0, i).trim();
		let v = line.slice(i + 1).trim();
		// 去掉行尾註解與引號
		v = v.replace(/\s+#.*$/, '').replace(/^["']|["']$/g, '');
		data[k] = v;
	}
	return { data, body: raw.slice(m[0].length) };
}

function baseName(path: string): string {
	return path.split('/').pop()!.replace(/\.md$/, '');
}

/** 依檔名排序（檔名以兩位數編號開頭）。 */
export function loadSheets(files: Record<string, string>): Sheet[] {
	return Object.entries(files)
		.map(([path, raw]) => {
			const { data, body } = parseFront(raw);
			return {
				id: baseName(path),
				title: data.title ?? baseName(path),
				kicker: data.kicker ?? '',
				site: data.site ?? null,
				body: body.trim(),
			};
		})
		.sort((a, b) => a.id.localeCompare(b.id));
}

export type DoseTable = { slug: string; title: string; body: string };

/** 劑量檔：frontmatter 的 title 是主題名，body 是表格。依 order 排序（跟主題頁一致）。 */
export function loadDoses(files: Record<string, string>): DoseTable[] {
	return Object.entries(files)
		.map(([path, raw]) => {
			const { data, body } = parseFront(raw);
			return {
				slug: baseName(path),
				title: data.title ?? baseName(path),
				order: Number(data.order ?? 99),
				body: body.trim(),
			};
		})
		.sort((a, b) => a.order - b.order)
		.map(({ slug, title, body }) => ({ slug, title, body }));
}

/**
 * 橫式 A4 的排版：把 body 依 `## ` 切成段落，各自包成 <section>。
 * 並排規則（寬度換高度）：
 * - 段落標題前一行寫 `<!-- pair -->`，這段與下一段並排成兩欄。
 * - 「破題關鍵句」＋「容易被電」這兩個固定結尾段預設並排。
 * 標題之前的內容（第一性原理框）照原樣輸出。
 */
export function layoutSheet(body: string, render: (md: string) => string): string {
	const parts = body.split(/^(?=## )/m);
	const lead = parts[0].startsWith('## ') ? '' : parts.shift()!;
	const secs = parts.map((p) => {
		const pairNext = /<!--\s*pair\s*-->\s*$/.test(p);
		const md = p.replace(/<!--\s*pair\s*-->\s*$/, '');
		const title = md.match(/^## (.+)$/m)?.[1] ?? '';
		return { md, title, pairNext };
	});
	// lead 的結尾也可以放 pair 標記，指向第一段
	const out: string[] = [];
	if (lead.trim()) out.push(render(lead.replace(/<!--\s*pair\s*-->\s*$/, '')));
	for (let i = 0; i < secs.length; i++) {
		const s = secs[i];
		const n = secs[i + 1];
		const autoTail = n && /破題關鍵句/.test(s.title) && /容易被電/.test(n.title);
		if (n && (s.pairNext || autoTail)) {
			out.push(
				`<div class="pair"><section>${render(s.md)}</section><section>${render(n.md)}</section></div>`,
			);
			i++;
		} else {
			out.push(`<section>${render(s.md)}</section>`);
		}
	}
	return out.join('\n');
}
