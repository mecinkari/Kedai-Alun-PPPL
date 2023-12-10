<script lang="ts">
	import { Alert, Card, Hr, Input, Label, P } from 'flowbite-svelte';
	import type { PageData } from './$types';

	export let data: PageData;

	let loading: boolean = false;
	let blob: string;

	const scan = async (e: Event) => {
		blob = '';
		loading = true;
		const form = new FormData();
		const { target } = e;
		const files = (target as HTMLInputElement).files as FileList;

		form.append('picture', files[0]);

		const response = await fetch('https://kedaialun-odb5yx637a-uc.a.run.app/predict', {
			method: 'POST',
			body: form
		});

		const data = await response.blob();
		blob = URL.createObjectURL(data);
		loading = false;
	};
</script>

<svelte:head>
	<title>Scan Biji Kopi - Kedai Alun</title>
</svelte:head>

<P size="2xl" weight="semibold">Scan Biji Kopi</P>

<Hr />

<form action="" enctype="multipart/form-data">
	<Label class="flex flex-col gap-y-2">
		<span>Masukkan gambar biji kopi untuk di-scan</span>
		<Input type="file" accept="image/*" on:change={(e) => scan(e)} />
	</Label>
</form>

{#if loading}
	<Alert color="blue" border><span class="font-bold text-2xl">Mohon Tunggu...</span></Alert>
{/if}

{#if blob}
	<Card class="mx-auto mt-6 max-w-2xl w-full">
		<P align="center">Hasil Scan</P>
		<img src={blob} alt="" />
	</Card>
{/if}
