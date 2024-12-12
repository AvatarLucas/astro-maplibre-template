// @ts-check
import { defineConfig } from "astro/config";
import mdx from "@astrojs/mdx";
import sitemap from "@astrojs/sitemap";
import tailwind from "@astrojs/tailwind";
import { resolve } from 'path';

export default defineConfig({
  site: "https://avatarlucas.github.io",
  base: "astro-maplibre-template",
  integrations: [mdx(), sitemap(), tailwind()],
  vite: {
    resolve: {
      alias: {
        '@lib': resolve('./src/lib')
      } 
    } 
  } 
});
