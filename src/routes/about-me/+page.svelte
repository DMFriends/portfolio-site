<svelte:head>
	<title>Daniel Miretsky</title>
	<meta name="description" content="About Daniel Miretsky" />
</svelte:head>

<div class="page">
	<header class="hero">
		<div class="hero-overlay" aria-hidden="true"></div>
		<div class="hero-content">
			<h1>Daniel Miretsky</h1>
			<p class="tagline">About Me</p>
		</div>
	</header>

	<main class="content">
		<section class="intro">
			<!-- Add your photo next to the intro if desired -->
			<div class="prose">
				<p>
					Hello! My name is Daniel Miretsky and I am a student at Wentworth Institute of Technology in Boston, MA, majoring in Computer Science. Here you will find some of my favorite and best coding projects and open source contributions that I have worked on over the past few years as I familiarized myself with the world of computer science. You can also find my resume and contact information below.
				</p>
			</div>
		</section>
	</main>
</div>

<style>
	.page {
		min-height: 100vh;
		background-color: #fafafa;
		color: #212121;
	}

	.hero {
		position: relative;
		height: 340px;
		display: flex;
		align-items: center;
		justify-content: center;
		background-image: url('/code.jpg');
		background-size: cover;
		background-position: center;
	}

	.hero-overlay {
		position: absolute;
		inset: 0;
		background-color: rgba(31, 31, 31, 0.5);
		pointer-events: none;
	}

	.hero-content {
		position: relative;
		z-index: 1;
		text-align: center;
		color: #fff;
	}

	.hero-content h1 {
		margin: 0;
		font-size: clamp(2rem, 5vw, 3rem);
		font-weight: 600;
		letter-spacing: -0.02em;
	}

	.tagline {
		margin: 0.5rem 0 0;
		font-size: 1.125rem;
		opacity: 0.95;
	}

	.content {
		max-width: 720px;
		margin: 0 auto;
		padding: 3rem 1.5rem;
	}

	.prose {
		line-height: 1.7;
	}

	.prose p {
		margin: 0 0 1rem;
	}

	.prose p:last-child {
		margin-bottom: 0;
	}
</style>
