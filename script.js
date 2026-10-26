'use strict';
const menuToggle=document.querySelector('.menu-toggle');
const navigation=document.querySelector('#main-navigation');
function closeMenu(focus=false){document.body.classList.remove('menu-open');menuToggle?.setAttribute('aria-expanded','false');menuToggle?.setAttribute('aria-label','Open navigation');if(focus)menuToggle?.focus();}
menuToggle?.addEventListener('click',()=>{const open=menuToggle.getAttribute('aria-expanded')!=='true';document.body.classList.toggle('menu-open',open);menuToggle.setAttribute('aria-expanded',String(open));menuToggle.setAttribute('aria-label',open?'Close navigation':'Open navigation');if(open)navigation?.querySelector('a')?.focus();});
navigation?.addEventListener('click',e=>{if(e.target.closest('a'))closeMenu();});
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&document.body.classList.contains('menu-open'))closeMenu(true);if(e.key==='Tab'&&document.body.classList.contains('menu-open')){const first=navigation.querySelector('a');const last=menuToggle;if(e.shiftKey&&document.activeElement===first){e.preventDefault();last.focus();}else if(!e.shiftKey&&document.activeElement===last){e.preventDefault();first.focus();}}});
window.matchMedia('(min-width:961px)').addEventListener('change',e=>{if(e.matches)closeMenu();});
const galleryItems=[...document.querySelectorAll('.gallery-item')];
const galleryToggle=document.querySelector('#gallery-toggle');
const lightbox=document.querySelector('.lightbox');
let activeIndex=0,previousFocus;
function showPhoto(index){activeIndex=(index+galleryItems.length)%galleryItems.length;const item=galleryItems[activeIndex];const image=lightbox.querySelector('figure img');image.src=item.dataset.image;image.alt=item.dataset.caption;lightbox.querySelector('#lightbox-caption').textContent=item.dataset.caption;lightbox.querySelector('#lightbox-counter').textContent=`${activeIndex+1} / ${galleryItems.length}`;}
galleryItems.forEach((item,index)=>item.addEventListener('click',()=>{previousFocus=item;showPhoto(index);lightbox.showModal();document.body.style.overflow='hidden';lightbox.querySelector('.lightbox-close').focus();}));
galleryToggle?.addEventListener('click',()=>{const expanded=galleryToggle.getAttribute('aria-expanded')!=='true';galleryItems.forEach((item,index)=>{if(index>=6)item.hidden=!expanded;});galleryToggle.setAttribute('aria-expanded',String(expanded));galleryToggle.firstChild.textContent=expanded?'Show fewer photos ':'View all 33 photos ';if(!expanded)document.querySelector('#gallery')?.scrollIntoView({block:'start'});});
lightbox?.querySelector('.lightbox-close')?.addEventListener('click',()=>lightbox.close());
lightbox?.querySelector('.lightbox-prev')?.addEventListener('click',()=>showPhoto(activeIndex-1));
lightbox?.querySelector('.lightbox-next')?.addEventListener('click',()=>showPhoto(activeIndex+1));
lightbox?.addEventListener('keydown',e=>{if(e.key==='ArrowLeft'){e.preventDefault();showPhoto(activeIndex-1);}if(e.key==='ArrowRight'){e.preventDefault();showPhoto(activeIndex+1);}});
lightbox?.addEventListener('click',e=>{if(e.target===lightbox)lightbox.close();});
lightbox?.addEventListener('close',()=>{document.body.style.overflow='';previousFocus?.focus();});
