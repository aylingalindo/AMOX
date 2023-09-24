const carousel = document.querySelector(".keypoints");
const arrowBtns = document.querySelectorAll(".keypointsBtn");
const firstCardWidth = carousel.querySelector(".card").offsetWidth;

arrowBtns.forEach(btn => {
    btn.addEventListener("click", () => {
        carousel.scrollLeft += btn.id === "left" ? -firstCardWidth - 18 : firstCardWidth + 18;
    })
});

let isDragging = false, startX, startScrollLeft; 

const dragStart = (e) => {
    isDragging = true;
    carousel.classList.add("dragging");
    startX = e.pageX;
    startScrollLeft = carousel.scrollLeft;
}

const dragging = (e) => {
    if(!isDragging) return;
    carousel.scrollLeft = startScrollLeft - (e.pageX - startX);
}

const dragStop = () => {
    isDragging = false;
    carousel.classList.remove("dragging");
}

carousel.addEventListener("mousedown", dragStart); 
carousel.addEventListener("mousemove", dragging); 
carousel.addEventListener("moveup", dragStop); 