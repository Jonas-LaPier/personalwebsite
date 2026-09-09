const button = document.querySelector('.menu');
const nav = document.querySelector('nav');
button?.addEventListener('click', () => {
  const open = button.getAttribute('aria-expanded') === 'true';
  button.setAttribute('aria-expanded', String(!open));
  nav.classList.toggle('open', !open);
});

const moleculeField = document.querySelector('.molecule-field');
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

const moleculeArt = {
  water: `<svg viewBox="0 0 100 70"><line x1="49" y1="38" x2="20" y2="17"/><line x1="51" y1="38" x2="80" y2="17"/><circle class="oxygen" cx="50" cy="42" r="15"/><circle class="hydrogen" cx="17" cy="15" r="9"/><circle class="hydrogen" cx="83" cy="15" r="9"/></svg>`,
  pfoa: `<svg viewBox="0 0 330 120"><g class="sticks"><path d="M35 61 70 61 105 61 140 61 175 61 210 61 245 61 278 61"/><path d="M35 61 8 61M35 61 22 30M35 61 22 92M70 61 70 25M70 61 70 97M105 61 105 25M105 61 105 97M140 61 140 25M140 61 140 97M175 61 175 25M175 61 175 97M210 61 210 25M210 61 210 97M245 61 245 25M245 61 245 97M282 65 302 45M274 57 296 35M278 61 300 84"/></g><g class="carbons"><circle cx="35" cy="61" r="9"/><circle cx="70" cy="61" r="9"/><circle cx="105" cy="61" r="9"/><circle cx="140" cy="61" r="9"/><circle cx="175" cy="61" r="9"/><circle cx="210" cy="61" r="9"/><circle cx="245" cy="61" r="9"/><circle cx="278" cy="61" r="10"/></g><g class="fluorines"><circle cx="8" cy="61" r="8"/><circle cx="22" cy="30" r="8"/><circle cx="22" cy="92" r="8"/><circle cx="70" cy="25" r="8"/><circle cx="70" cy="97" r="8"/><circle cx="105" cy="25" r="8"/><circle cx="105" cy="97" r="8"/><circle cx="140" cy="25" r="8"/><circle cx="140" cy="97" r="8"/><circle cx="175" cy="25" r="8"/><circle cx="175" cy="97" r="8"/><circle cx="210" cy="25" r="8"/><circle cx="210" cy="97" r="8"/><circle cx="245" cy="25" r="8"/><circle cx="245" cy="97" r="8"/></g><circle class="oxygen" cx="304" cy="35" r="10"/><circle class="oxygen" cx="304" cy="87" r="10"/><circle class="hydrogen" cx="322" cy="94" r="6"/></svg>`,
  tetrabromo: `<svg viewBox="0 0 190 190"><g class="sticks"><path d="M95 38 139 64 139 116 95 142 51 116 51 64Z"/><path d="M95 38V10M139 64l26-15M95 142v28M51 116l-26 15"/></g><g class="carbons"><circle cx="95" cy="38" r="8"/><circle cx="139" cy="64" r="8"/><circle cx="139" cy="116" r="8"/><circle cx="95" cy="142" r="8"/><circle cx="51" cy="116" r="8"/><circle cx="51" cy="64" r="8"/></g><g class="bromines"><circle cx="95" cy="10" r="13"/><circle cx="165" cy="49" r="13"/><circle cx="95" cy="170" r="13"/><circle cx="25" cy="131" r="13"/></g></svg>`
};

function releaseMolecule() {
  if (!moleculeField || reducedMotion || moleculeField.childElementCount >= 3) return;
  const chance = Math.random();
  const type = chance < .09 ? 'tetrabromo' : chance < .22 ? 'pfoa' : 'water';
  const molecule = document.createElement('span');
  molecule.className = `floating-molecule ${type}`;
  molecule.innerHTML = moleculeArt[type];
  molecule.style.setProperty('--lane', `${8 + Math.random() * 74}vh`);
  molecule.style.setProperty('--duration', `${38 + Math.random() * 18}s`);
  molecule.style.setProperty('--tilt', `${-18 + Math.random() * 36}deg`);
  molecule.style.setProperty('--direction', Math.random() > .5 ? 'normal' : 'reverse');
  molecule.style.setProperty('--wander-duration', `${7 + Math.random() * 7}s`);
  molecule.style.setProperty('--x-one', `${-18 + Math.random() * 36}px`);
  molecule.style.setProperty('--y-one', `${-22 + Math.random() * 44}px`);
  molecule.style.setProperty('--x-two', `${-24 + Math.random() * 48}px`);
  molecule.style.setProperty('--y-two', `${-18 + Math.random() * 36}px`);
  molecule.style.setProperty('--spin-one', `${-14 + Math.random() * 28}deg`);
  molecule.style.setProperty('--spin-two', `${-20 + Math.random() * 40}deg`);
  moleculeField.appendChild(molecule);
  molecule.addEventListener('animationend', () => molecule.remove());
}

if (moleculeField && !reducedMotion) {
  window.setTimeout(releaseMolecule, 3500);
  window.setInterval(releaseMolecule, 22000);
}
