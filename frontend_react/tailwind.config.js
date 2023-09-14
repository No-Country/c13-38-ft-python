/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.js",
    "./src/**/*.jsx",
    "./src/**/*.html",
  ],
  theme: {
    extend: {
      colors: {
        principal: '#5847AD',
        secundario1: '#0C4B8E',
        secundario2: '#535E92',
        secundario3: '#5E6AA4',
        acentuacion : "#189BFA",
      },
      fontSize: {
        'xxs':'10px',
        'sm': '12px',
        'md': '14px',
        'lg': '16px',
        'xl': '18px',
      },
    },
  },
  plugins: [require('tailwindcss-font-inter')],
}