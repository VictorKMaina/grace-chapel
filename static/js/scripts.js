$(document).ready(function () {
    $("div.container:not(div.container:first)").hide(0, () => {
      $("div.container:not(div.container:first)").fadeIn(500);
    });

    let link = window.location.pathname;
    $(`a.nav-link[href="${link}"]`).parent().addClass('active');
    $('ul.nav a').filter(function() {
         return this.href == link;
    }).parent().addClass('active');
});