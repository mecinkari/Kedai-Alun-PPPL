<script lang="ts">
	import Navbar from '$lib/components/Navbar.svelte';
	import type { PageData } from './$types';
	import { Alert, Button, Card, Input, Label, P } from 'flowbite-svelte';

	export let data: PageData;
</script>

<svelte:head>
	<title>Login Admin Kedai Alun</title>
</svelte:head>

<Navbar fixed />

<Card class="w-full max-w-2xl flex flex-col gap-y-6">
	<P size="3xl" weight="semibold" align="center" italic>Kedai Alun &times; Seblak Aing Tea</P>

	{#if data.user}
		<Alert color="blue">
			<span>{JSON.stringify(data.user)}</span>
		</Alert>
	{/if}

	<form action="" method="post" class="flex flex-col gap-y-4">
		<Label class="flex flex-col gap-y-2">
			<span>Email</span>
			<Input type="email" name="email" required />
		</Label>
		<Label class="flex flex-col gap-y-2">
			<span>Password</span>
			<Input type="password" name="password" required />
		</Label>
		<Button type="submit">Log In</Button>
	</form>
</Card>
