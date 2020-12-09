$(document).ready(function () {
    let link = window.location.pathname;
    $(`a.nav-link[href="${link}"]`).parent().addClass('active');
    $('ul.nav a').filter(function() {
         return this.href == link;
    }).parent().addClass('active');
});