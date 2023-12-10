<script lang="ts">
	import {
		Alert,
		Button,
		Card,
		Fileupload,
		Hr,
		Input,
		Label,
		Li,
		List,
		P,
		Select,
		Table,
		TableBody,
		TableBodyCell,
		TableBodyRow,
		TableHead,
		TableHeadCell
	} from 'flowbite-svelte';
	import { page } from '$app/stores';
	import type { PageData } from './$types';

	export let data: PageData;

	type Transaction = {
		column: number;
		data: [
			{
				harga_barang: number;
				kuantitas: number;
				nama_barang: string;
				tanggal_pembelian: string;
				total: number;
				user_id: string;
			}
		];
		row: number;
		total_per_tanggal: [
			{
				sum_total: number;
				tanggal_pembelian: string;
			}
		];
	};

	let json_data: Transaction | null;
	$: loading = false;
	$: date = '';

	let full_card = 'w-full max-w-full';
	let roles = [
		{ value: '0', name: 'Developer' },
		{ value: '1', name: 'Admin' },
		{ value: '2', name: 'Default' }
	];

	const formatNumber = (num: number) => {
		return new Intl.NumberFormat('id-ID').format(num);
	};

	const fileUpload = async (e: Event) => {
		loading = true;
		json_data = null;
		const files = (e.target as HTMLInputElement).files as FileList;
		const form = new FormData();

		form.append('file', files[0]);

		const response = await fetch('http://127.0.0.1:1010/api/dashboard', {
			method: 'POST',
			body: form
		});

		// const data = await response.json();
		json_data = (await response.json()) as Transaction;
		loading = false;
		console.log(json_data);
	};
</script>

<svelte:head>
	<title>Admin Dashboard - Kedai Alun</title>
</svelte:head>

<P size="2xl">Selamat Datang, {$page.data.user.nama}</P>
<!-- $page.data.user.role == 1 -->
<div class={`grid ${$page.data.user.role == 1 ? 'lg:grid-cols-3' : ''} my-6 gap-2`}>
	<Card class={`lg:col-span-2 ${full_card} flex flex-col gap-y-4`}>
		<form>
			<Label>
				<span>Masukkan File CSV</span>
				<Input type="file" accept=".csv" name="file" on:change={(e) => fileUpload(e)} />
			</Label>
		</form>

		{#if !json_data}
			<Alert>
				<p>Header column yang wajib ada:</p>
				<List>
					<Li>User ID</Li>
					<Li>Tanggal Pembelian</Li>
					<Li>Nama Barang</Li>
					<Li>Harga Barang</Li>
					<Li>Kuantitas</Li>
					<Li>Total</Li>
				</List>
			</Alert>
		{/if}

		<!-- <form>
			<Label>
				<span>Buat Tabel Transaksi Baru</span>
				<Input type="date" name="date" bind:value={date} />
			</Label>
			<Button type="submit" on:click={() => createTable()}>Buat Tabel</Button>
		</form> -->

		{#if loading}
			<Alert color="yellow" border>Loading...</Alert>
		{/if}

		{#if json_data}
			<Table>
				<TableHead>
					<TableHeadCell>Tanggal Pembelian</TableHeadCell>
					<TableHeadCell>Makanan / Minuman</TableHeadCell>
				</TableHead>
				<TableBody>
					{#each json_data.data as jd}
						<TableBodyRow>
							<TableBodyCell>{jd.tanggal_pembelian}</TableBodyCell>
							<TableBodyCell>{jd.nama_barang}</TableBodyCell>
						</TableBodyRow>
					{/each}
				</TableBody>
			</Table>

			{#each json_data.total_per_tanggal as jd}
				<P>Total di tanggal {jd.tanggal_pembelian}: Rp{formatNumber(jd.sum_total)}</P>
			{/each}
		{/if}
	</Card>
	{#if $page.data.user.role == 1}
		<Card class={`${full_card}`}>
			<P size="2xl">Register User Baru</P>
			<Hr />
			<form action="?/register" method="post" class="flex flex-col gap-y-6">
				<Label>
					<span>Nama</span>
					<Input type="text" name="nama" />
				</Label>
				<Label>
					<span>Email</span>
					<Input type="email" name="email" />
				</Label>
				<Label>
					<span>Password</span>
					<Input type="password" name="password" />
				</Label>
				<Label>
					<span>Retype Password</span>
					<Input type="password" name="retype_password" />
				</Label>
				<Label>
					<span>Role</span>
					<Select items={roles} />
				</Label>
				<div class="flex flex-row gap-x-2">
					<Button class="flex-grow" type="submit" color="green">Submit</Button>
					<Button class="flex-grow" type="reset" color="red" outline>Reset</Button>
				</div>
			</form>
		</Card>
	{/if}
</div>
