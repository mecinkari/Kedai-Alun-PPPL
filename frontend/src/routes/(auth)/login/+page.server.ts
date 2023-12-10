import { redirect, type Actions } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const actions: Actions = {
    default: async ({ fetch, cookies, request }) => {
        const form = await request.formData();

        const response = await fetch(`http://127.0.0.1:1010/auth/login`, {
            method: "POST",
            body: form
        })

        const data = await response.json();
        console.log(data, response.status)

        if (response.status == 401) {
            return {
                data: data
            }
        }

        cookies.set("session", JSON.stringify(data), {
            path: '/',
            httpOnly: true,
            sameSite: 'strict',
            maxAge: 60 * 60 * 24 * 1
        })

        throw redirect(301, '/admin')
    }
};

export const load = (async ({ locals }) => {
    return {
        user: locals.user
    };
}) satisfies PageServerLoad;