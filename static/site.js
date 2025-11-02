// micro-interactions: reveal on scroll + small accessible toggles
(function(){
  // reveal on scroll using IntersectionObserver
  const io = new IntersectionObserver((entries)=>{
    entries.forEach(e => {
      if(e.isIntersecting){
        e.target.classList.add('is-visible');
      }
    });
  },{threshold:0.12});

  document.querySelectorAll('.reveal').forEach(el=>io.observe(el));

  // keyboard accessibility: focus visible on nav links
  const navLinks = document.querySelectorAll('.floating-nav a');
  navLinks.forEach(a=>{
    a.addEventListener('focus', ()=> a.classList.add('is-focused'));
    a.addEventListener('blur', ()=> a.classList.remove('is-focused'));
  });
})();

