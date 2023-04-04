/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
        colors: {
            primary: '#4B49AC',
            secondary: "#EEEEF7",
            secondaryLight: "#f5f7fa",
            menuItem: "#3C3A89",
            white: "#ffffff",
            muted: "#ADADAD",
            spot: "#8A81B5",
            error: "#ff6347"
        },
        fontFamily: {
            display: ["Outfit", "sans-serif"],
        },
        extend: {},
    },
    plugins: [],
}