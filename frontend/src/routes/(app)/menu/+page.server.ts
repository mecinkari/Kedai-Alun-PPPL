import type { Actions } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const actions: Actions = {
};

export const load = (async () => {
    return {};
}) satisfies PageServerLoad;