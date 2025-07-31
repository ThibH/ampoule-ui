/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./django_components_ui/**/*.{html,js,py}",
    "./documentation/**/*.{html,js,py}",
  ],
  theme: {
    extend: {
      // Custom extensions if needed
    },
  },
  plugins: [
    // Note: DaisyUI is imported directly in input.css using Tailwind CSS 4.x @plugin syntax
    // See django_components_ui/static/django_components_ui/css/input.css for DaisyUI configuration
  ],
};
