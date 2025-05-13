import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import content from '@astrojs/content';

export default defineConfig({
  site: 'https://atlantyde-labs.vercel.app',
  integrations: [mdx(), sitemap(), content()],
});