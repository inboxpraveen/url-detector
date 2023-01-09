$(document).ready(function() {

    // Transition effect for navbar and back-to-top icon
    $(window).scroll(function() {
      // checks if window is scrolled more than 500px, adds/removes solid class
      if($(this).scrollTop() > 550) { 
          $('.navbar').addClass('solid');
          $('.back-to-top').addClass('visible'); 
      } else {
          $('.navbar').removeClass('solid');
          $('.back-to-top').removeClass('visible');  
      }

    });

    // Scrolling effect for Arrow icons
    $("#scrollIcon").click(function(e) {
        e.preventDefault();
        $.scrollTo($("#about"), 1000);
    });
    $("#nav-about").click(function(e) {
        e.preventDefault();
        $.scrollTo($("#about"), 1000);
    });
    $("#nav-contact").click(function(e) {
        e.preventDefault();
        $.scrollTo($("#contact"), 1000);
    });
    $(".navbar-brand").click(function(e) {
        e.preventDefault();
        $.scrollTo(0, 1000);
    });
      
  });


let modal;
document.addEventListener("click", (e) => {
  if (e.target.className === "modal-open") {
    modal = document.getElementById(e.target.dataset.id);
    openModal(modal);
  } else if (e.target.className === "modal-close") {
    closeModal(modal);
  } else {
    return;
  }
});

const openModal = (modal) => {
    document.body.style.overflow = "hidden";
    modal.setAttribute("open", "true");
    document.addEventListener("keydown", escClose);
    let overlay = document.createElement("div");
    overlay.id = "modal-overlay";
    document.body.appendChild(overlay);
  };

  const closeModal = (modal) => {
    document.body.style.overflow = "auto";
    modal.removeAttribute("open");
    document.removeEventListener("keydown", escClose);
    document.body.removeChild(document.getElementById("modal-overlay"));
  };

  const escClose = (e) => {
    if (e.keyCode == 27) {
      closeModal();
    }
  };

  