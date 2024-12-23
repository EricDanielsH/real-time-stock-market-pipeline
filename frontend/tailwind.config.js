/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}", // Include all files with Tailwind classes
  ],
  theme: {
    extend: {}, // Add customizations here
  },
  plugins: [], // Add plugins here if needed
};
