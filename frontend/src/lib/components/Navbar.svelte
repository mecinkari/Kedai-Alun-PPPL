<script lang="ts">
	import { page } from '$app/stores';
	import { NavBrand, NavHamburger, NavLi, NavUl, Navbar } from 'flowbite-svelte';

	export let fixed: Boolean = false;
	export let stikcy: Boolean = false;

	$: activeUrl = $page.url.pathname;
</script>

<Navbar class={`${fixed == true ? 'fixed top-0' : ''} ${stikcy == true ? 'sticky top-0' : ''}`}>
	<NavBrand href="/">
		<span class="self-center whitespace-nowrap text-xl font-semibold dark:text-white"
			>Kedai Alun</span
		>
	</NavBrand>
	<NavHamburger />
	<NavUl {activeUrl}>
		{#if $page.data.user}
			<NavLi href="/admin">Dashboard</NavLi>
		{/if}
		<NavLi href="/menu">Menu</NavLi>
		<NavLi href="/scanbijikopi">Scan Biji Kopi</NavLi>

		{#if !$page.data.user}
			<NavLi href="/login">Log In</NavLi>
		{/if}

		{#if $page.data.user}
			<form action="/logout" method="post">
				<button
					class="block py-2 pr-4 pl-3 md:p-0 rounded md:border-0 hover:text-primary-700"
					type="submit">Logout</button
				>
			</form>
		{/if}
	</NavUl>
</Navbar>
