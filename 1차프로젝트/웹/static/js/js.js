const content = "무슨 내용이 들어가야 할지 모르겠당s(￣▽￣)/"
const text = document.querySelector('#text')
let i = 0;

    function typing() {
        let txt =  content[i++]
        text.innerHTML += txt=== "\n" ? "<br/>": txt;
        if(i > content.length) {
            text.textContent = ""
            i = 0;
        }

    }
    setInterval(typing, 100)

    var slides = document.querySelector('.slides'),
    slide = document.querySelectorAll('.slides li'),
    currentIdx = 0,
    slideCount = slide.length,
    prevBtn =document.querySelector('.prev'),
    slidewidth = 450,
    slideMargin = 10,
    nextBtn =document.querySelector('.next');

    slides.style.width = (slidewidth + slideMargin) *slideCount - slideMargin + 'px';

   function moveSlide(num) {
    slides.style.left = -num * 460 + 'px'
    currentIdx = num;
   }
   nextBtn.addEventListener('click', function() {
   if(currentIdx < slideCount -1 ) {
    moveSlide(currentIdx +1);}else{moveSlide(0)}
})
prevBtn.addEventListener('click', function() {
    if(currentIdx > 0 ) {
     moveSlide(currentIdx - 1);}else{moveSlide(slideCount -1)}
 })