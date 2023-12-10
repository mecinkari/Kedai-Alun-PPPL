<script lang="ts">
	import Navbar from '$lib/components/Navbar.svelte';
	import type { LayoutData } from './$types';

	export let data: LayoutData;
</script>

<main class="flex flex-col min-h-screen w-full">
	<Navbar stikcy />
	<section class="container mx-auto px-2 sm:px-0">
		<slot />
	</section>
</main>
