/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "users/templates/users/*.html",
    "posts/templates/posts/*.html",
    "users/static/users/*.js",
    "posts/static/posts/*.js",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

