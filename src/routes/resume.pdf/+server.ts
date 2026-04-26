import { error } from '@sveltejs/kit';
import type { RequestHandler } from './$types';

const GOOGLE_DOC_ID = '1bhVwWsPEovf2HFZMU3aLZC3aPFxYEFkTHlsXKnVAU3c';
const EXPORT_URL = `https://docs.google.com/document/d/${GOOGLE_DOC_ID}/export?format=pdf`;
const DOWNLOAD_FILENAME = 'Daniel-Miretsky-Resume.pdf';

export const GET: RequestHandler = async ({ fetch, setHeaders }) => {
	const upstream = await fetch(EXPORT_URL);

	if (!upstream.ok || !upstream.body) {
		throw error(502, 'Could not fetch resume from Google Docs');
	}

	setHeaders({
		'content-type': 'application/pdf',
		'content-disposition': `attachment; filename="${DOWNLOAD_FILENAME}"`,
		// Cache at the edge for 1h, allow stale for a day while revalidating.
		// Tweak if you want changes to propagate faster/slower.
		'cache-control': 'public, max-age=3600, stale-while-revalidate=86400'
	});

	return new Response(upstream.body, { status: 200 });
};
