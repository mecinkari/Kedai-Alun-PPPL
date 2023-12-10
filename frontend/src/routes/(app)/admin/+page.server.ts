import { redirect, type Actions } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const actions: Actions = {
    register: async ({ request, fetch }) => {
        const form = await request.formData();
        const password: string = form.get("password") as string
        const retype_password: string = form.get("retype_password") as string
        const same_password = password == retype_password;

        if (!same_password) {
            const data = {
                msg: "Error! Password doesn't match at all"
            }
            console.log(data)
            return {
                data
            }
        }

        const response = await fetch("http://127.0.0.1:1010/user/create", {
            method: "POST",
            body: form
        })

        if (response.status != 200) {
            return {
                data: {
                    msg: "Error"
                }
            }
        }

        const data = await response.json()
        console.log(data)
        return {
            data
        }
    }
};

export const load = (async ({ locals }) => {
    if (!locals.user) {
        throw redirect(301, '/login')
    }

    return {};
}) satisfies PageServerLoad;