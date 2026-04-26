<script lang="ts">
	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href="/avatar.png" type="image/png" />
</svelte:head>

{@render children()}
