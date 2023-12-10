<script lang="ts">
	import type { LayoutData } from './$types';

	export let data: LayoutData;
</script>

<main class="min-h-screen w-full flex flex-col justify-center items-center bg-primary-100">
	<slot />
</main>
