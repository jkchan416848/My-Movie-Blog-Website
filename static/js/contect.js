console.log("contect-page");

const observers = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    console.log(entry);
    if (entry.isIntersecting) {
      entry.target.classList.add("show");
    } else {
      entry.target.classList.remove("show");
    }
  });
});
const hidden_element1 = document.querySelectorAll(".about-title");
hidden_element1.forEach((e1) => observers.observe(e1));
console.log(hidden_element1);
