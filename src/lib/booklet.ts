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
