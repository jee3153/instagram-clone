module.exports = {
  purge: [],
  theme: {
    extend: {
      boxShadow: {
        inner2: `-2px -2px 4px #fff, -2px -2px 9px rgba(255,255,255,.5), inset 2px 2px 2px rgba(225,255,255,.1), 2px 2px 5px rgba(0,0,0,.15)`,
        outline2: `inset -2px -2px 8px rgba(255, 255, 255, 1), 
        inset -2px -2px 12px rgba(255, 255, 255, 0.5),
        inset 2px 2px 4px rgba(225, 255, 255, 0.1), 
        inset 2px 2px 8px rgba(0, 0, 0, 0.15)`,
        outline3: `inset -1px -1px 3px rgba(255, 255, 255, 0.9),
        inset -2px -2px 12px rgba(255, 255, 255, 0.5),
        inset 2px 2px 4px rgba(225, 255, 255, 0.1),
        2px 2px 8px rgba(0, 0, 0, 0.2)`,
      },
      padding: {
        "0.4": "0.4rem",
        "0.6": "0.6rem",
      },
      borderRadius: {
        xl: "1rem",
      },
    },
  },
  variants: {},
  plugins: [],
}
