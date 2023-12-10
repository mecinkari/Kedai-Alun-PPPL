import type { Handle } from "@sveltejs/kit";

export const handle: Handle = async ({ event, resolve }) => {
    const session = event.cookies.get("session");

    if (!session) {
        return await resolve(event)
    }

    const user = JSON.parse(session)

    if (user) {
        event.locals.user = {
            id: user.user.id,
            nama: user.user.nama,
            email: user.user.email,
            password: user.user.password,
            role: user.user.role
        }
    }

    return await resolve(event)
}