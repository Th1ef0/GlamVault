/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      fontFamily: {
        Krub: ['Krub', 'sans-serif'],
        Julius: ['Julius Sans One', 'sans-serif'],
      }
    }
  },
  plugins: []
};
