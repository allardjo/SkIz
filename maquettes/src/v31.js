  // carrousel d'avis + étoiles
  var reduceMotion=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.querySelectorAll('[data-car]').forEach(function(c){
    var sl=c.querySelectorAll('.av-slide'),dots=c.querySelectorAll('.av-dot'),i=0,timer;
    function go(n){i=(n+sl.length)%sl.length;sl.forEach(function(s,k){s.classList.toggle('on',k===i)});dots.forEach(function(d,k){d.classList.toggle('on',k===i)})}
    function play(){clearInterval(timer);if(!reduceMotion)timer=setInterval(function(){go(i+1)},7000)}
    dots.forEach(function(d,k){d.addEventListener('click',function(){go(k);play()})});
    c.querySelector('.av-next').addEventListener('click',function(){go(i+1);play()});
    c.querySelector('.av-prev').addEventListener('click',function(){go(i-1);play()});
    c.addEventListener('mouseenter',function(){clearInterval(timer)});c.addEventListener('mouseleave',play);play();
  });
  // compteurs
