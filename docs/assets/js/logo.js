function createLogo(variant = 'primary', size = 300) {
  const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
  svg.setAttribute("viewBox", "0 0 300 300");
  svg.setAttribute("width", size);
  svg.setAttribute("height", size);

  const styles = {
    primary: {
      bgColor: 'white',
      pathFill: '#1E84FF',
      textFill: 'white'
    },
    inverted: {
      bgColor: '#1E84FF',
      pathFill: 'white',
      textFill: '#1E84FF'
    }
  };

  const style = styles[variant];

  svg.innerHTML = `
    <rect width="300" height="300" fill="${style.bgColor}" />
    <path d="M50 50 H200 A50 50 0 0 1 250 100 V250 H100 A50 50 0 0 1 50 200 Z"
          fill="${style.pathFill}" />
    <text x="150" y="150"
          font-family="Poppins,sans-serif"
          font-size="160"
          font-weight="600"
          fill="${style.textFill}"
          text-anchor="middle"
          dominant-baseline="central">N</text>
  `;

  return svg;
}
