<svelte:head>
	<title>Daniel Miretsky</title>
	<meta name="description" content="About Daniel Miretsky" />
</svelte:head>

<script lang="ts">
  import avatar from '$lib/assets/avatar.png';
</script>

<div class="home-layout">
	<section class="flex-column hero">
		<div class="hero-inner">
			<div class="hero-text montserrat-regular">
				<p class="eyebrow">About Me</p>
				<div class="hero-name-row">
					<div class="avatar-placeholder">
						<img src={avatar} class="avatar-image" alt="Daniel Miretsky" />
					</div>
					<h1>Daniel Miretsky</h1>
				</div>
				<div class="prose montserrat-regular">
                    <p>
                        I am a student at <a href="https://www.wit.edu" target="_blank" class="montserrat-regular">Wentworth Institute of Technology</a> in Boston, MA, majoring in Computer Science. Here you will find some of my favorite and best coding projects and open source contributions that I have worked on over the past few years as I familiarized myself with the world of computer science. You can also find my resume and contact information below.
                    </p>
                </div>
			</div>
		</div>
	</section>

	<section class="bottom-half" aria-label="Quick links">
		<div class="bottom-inner">
			<div class="quick-buttons">
				<a class="quick-button russo-one-regular" href="/portfolio">View Portfolio</a>
				<a class="flex flex-column justify-center items-center quick-button russo-one-regular" href="/resume.pdf" target="_blank" rel="noopener">Resume</a>
			</div>

			<nav class="flex flex-row justify-center items-center social" aria-label="Social links">
				<a class="social-link" href="https://www.linkedin.com/in/danielmiretsky/" target="_blank" aria-label="LinkedIn">
					<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">
						<path
							d="M4.98 3.5C4.98 4.88 3.87 6 2.5 6S0 4.88 0 3.5 1.12 1 2.5 1s2.48 1.12 2.48 2.5ZM.5 23.5h4V7.98h-4V23.5Zm7 0h3.98v-8.42c0-2.25.42-4.44 3.2-4.44 2.74 0 2.78 2.56 2.78 4.58v8.28h3.99V14.39c0-4.47-.96-7.91-6.18-7.91-2.5 0-4.18 1.37-4.86 2.67h-.05V7.98H7.5V23.5Z" />
					</svg>
				</a>
				<a class="social-link" href="https://github.com/DMFriends" target="_blank" aria-label="GitHub">
					<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">
						<path
							d="M12 .5C5.73.5.75 5.7.75 12.12c0 5.1 3.28 9.43 7.83 10.95.57.1.78-.25.78-.56v-2c-3.18.7-3.85-1.26-3.85-1.26-.52-1.35-1.27-1.71-1.27-1.71-1.04-.73.08-.72.08-.72 1.15.08 1.76 1.22 1.76 1.22 1.02 1.78 2.68 1.27 3.33.97.1-.76.4-1.27.72-1.56-2.54-.3-5.2-1.3-5.2-5.78 0-1.27.44-2.31 1.16-3.13-.12-.3-.5-1.5.11-3.13 0 0 .95-.31 3.11 1.2.9-.26 1.87-.39 2.83-.39.96 0 1.93.13 2.83.39 2.16-1.51 3.1-1.2 3.1-1.2.62 1.63.24 2.83.12 3.13.72.82 1.16 1.86 1.16 3.13 0 4.49-2.66 5.48-5.2 5.77.41.36.77 1.08.77 2.18v3.23c0 .31.2.67.79.56 4.54-1.52 7.82-5.85 7.82-10.95C23.25 5.7 18.27.5 12 .5Z" />
					</svg>
				</a>
				<a class="social-link" href="mailto:me@danielmiretsky.com" target="_blank" aria-label="Email">
					<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">
						<path
							d="M4 5.5h16A2.5 2.5 0 0 1 22.5 8v8A2.5 2.5 0 0 1 20 18.5H4A2.5 2.5 0 0 1 1.5 16V8A2.5 2.5 0 0 1 4 5.5Zm0 2 8 5 8-5H4Zm16 9V9.7l-7.48 4.67a1 1 0 0 1-1.04 0L4 9.7v6.8c0 .28.22.5.5.5h15a.5.5 0 0 0 .5-.5Z" />
					</svg>
				</a>
			</nav>
		</div>

		<div class="suggestions-feedback-container">
			<p class="montserrat-regular">Suggestions? Feedback? Open an <a href="https://github.com/DMFriends/portfolio-site/issues" target="_blank" class="link">issue</a> or <a href="https://github.com/DMFriends/portfolio-site/pulls" target="_blank" class="link">PR</a>!</p>
		</div>

		<footer class="footer">
			<span>© {new Date().getFullYear()} Daniel Miretsky. All rights reserved.</span>
		</footer>
	</section>
</div>

<style>
	.home-layout {
		min-height: 100svh;
		min-height: 100vh;
		display: flex;
		flex-direction: column;
		background: #020617;
		color: #e5e7eb;
		box-sizing: border-box;
	}

	:global(body) {
		margin: 0;
		background: #ffffff;
	}

	.suggestions-feedback-container {
		padding: 1.25rem 1.5rem 1.5rem;
		text-align: center;
		font-size: 0.8rem;
		color: #0f172a;
		font-family: "Montserrat", sans-serif;
	}

	.suggestions-feedback-container a {
		color: #38bdf8;
		position: relative;
	}
	
	.suggestions-feedback-container a::after {
		content: "";
		position: absolute;
		left: 0;
		bottom: -0.1rem;
		width: 0;
		height: 1px;
		background: #38bdf8;
	}

	.suggestions-feedback-container a:hover::after {
		width: 100%;
	}
		
	.montserrat-regular {
		font-family: "Montserrat", sans-serif;
		font-optical-sizing: auto;
		font-weight: 400;
		font-style: normal;
	}

	a.montserrat-regular {
		color: #ffffff;
		text-decoration: underline;
	}

    .russo-one-regular {
        font-family: "Russo One", sans-serif;
        font-weight: 400;
        font-style: normal;
    }

	.hero {
		position: relative;
		padding: 4rem 1.5rem 3rem;
		display: flex;
		align-items: center;
		justify-content: center;
		background-image: linear-gradient(to bottom, rgba(15, 23, 42, 0.85), rgba(15, 23, 42, 0.95)),
			url('/code.jpg');
		background-size: cover;
		background-position: center;
	}

	.hero-inner {
		position: relative;
		z-index: 1;
		max-width: 1120px;
		margin: 0 auto;
		display: flex;
		align-items: center;
		justify-content: flex-start;
	}

	.hero-text h1 {
		margin: 0.2rem 0 0.75rem;
		font-size: clamp(2.3rem, 3.2vw, 3rem);
		line-height: 1.1;
	}

	.eyebrow {
		letter-spacing: 0.13em;
		text-transform: uppercase;
		font-size: 0.75rem;
		color: #9ca3af;
	}

	.hero-name-row {
		display: inline-flex;
		align-items: center;
		gap: 1rem;
	}

	.avatar-placeholder {
		flex-shrink: 0;
		width: 3.5rem;
		height: 3.5rem;
		aspect-ratio: 1;
		border-radius: 50%;
		overflow: hidden;
		border: 2px solid rgba(148, 163, 184, 0.6);
		box-shadow: 0 10px 25px rgba(15, 23, 42, 0.8);
	}

	.avatar-image {
		width: 100%;
		height: 100%;
		object-fit: cover;
		object-position: center 22%;
		display: block;
		border-radius: 50%;
	}

	@media (max-width: 640px) {
		.hero-name-row {
			gap: 0.75rem;
		}
	}

	.bottom-half {
		flex: 1;
		display: flex;
		flex-direction: column;
		min-height: 0;
		padding: 2.5rem 1.5rem 0;
		color: #0f172a;
		background: #ffffff;
	}

	.bottom-inner {
		flex: 1;
		max-width: 1120px;
		width: 100%;
		margin: 0 auto;
		display: grid;
		gap: 2.5rem;
		justify-items: center;
		align-content: start;
	}

	.footer {
		margin-top: auto;
		padding: 1.25rem 1.5rem 1.5rem;
		text-align: center;
		font-size: 0.8rem;
		color: #0f172a;
		font-family: "Montserrat", sans-serif;
		border-top: 1px solid rgba(15, 23, 42, 0.12);
		background: #ffffff;
	}

	.quick-buttons {
		width: 100%;
		display: grid;
		grid-template-columns: repeat(2, minmax(0, 1fr));
		gap: 1.25rem;
		overflow: hidden;
	}

	.quick-button {
		display: flex;
		align-items: center;
		justify-content: center;
		min-height: 3.25rem;
		padding: 0.85rem 1.25rem;
		border-radius: 0.35rem;
		background: linear-gradient(180deg, #0b84b6, #0670a2);
		color: #ffffff;
		text-decoration: none;
		box-shadow: 0 10px 20px rgba(2, 6, 23, 0.18);
		border: 1px solid rgba(2, 6, 23, 0.15);
		transition: transform 0.12s ease, box-shadow 0.2s ease, filter 0.2s ease;
		overflow: hidden;
		will-change: transform, background-color;
		transform: translateY(0);
		background-color: rgba(255, 255, 255, 0.04);
	}

	.quick-button:hover {
		transform: translateY(-1px);
		background-color: rgba(255, 255, 255, 0.04);
		will-change: transform, background-color;
	}

	.quick-buttons a:nth-child(3) {
		grid-column: 1 / -1;
		max-width: 420px;
		width: 100%;
		justify-self: center;
	}

	.social {
		padding-top: 2rem;
		display: flex;
		flex-wrap: wrap;
		gap: 2.25rem;
		justify-content: center;
	}

	.social-link {
		width: 3.1rem;
		height: 3.1rem;
		border-radius: 999px;
		display: inline-flex;
		align-items: center;
		justify-content: center;
		background: rgba(15, 23, 42, 0.12);
		border: 1px solid rgba(15, 23, 42, 0.18);
		color: rgba(15, 23, 42, 0.72);
		transition: transform 0.12s ease, background 0.2s ease, color 0.2s ease;
		text-decoration: none;
	}

	.social-link:hover {
		transform: translateY(-1px);
		background: rgba(56, 189, 248, 0.14);
		color: rgba(2, 6, 23, 0.95);
	}

	.social-link svg {
		width: 1.35rem;
		height: 1.35rem;
		fill: currentColor;
	}

	.prose {
		line-height: 1.7;
	}

	.prose p {
		margin: 0;
	}

	@media (max-width: 640px) {
		.hero {
			padding-top: 3rem;
			padding-bottom: 2.5rem;
		}

		.quick-buttons {
			grid-template-columns: minmax(0, 1fr);
		}

		.quick-buttons a:nth-child(3) {
			max-width: none;
		}

		.social {
			gap: 1.25rem;
		}
	}
</style>