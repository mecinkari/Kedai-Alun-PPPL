import { redirect, type Actions } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const actions: Actions = {
    default({ cookies }) {
        cookies.set("session", "", {
            path: '/',
            expires: new Date(0)
        })

        throw redirect(301, '/login')
    }
};

export const load = (async () => {
    throw redirect(302, '/')
    // return {};
}) satisfies PageServerLoad;