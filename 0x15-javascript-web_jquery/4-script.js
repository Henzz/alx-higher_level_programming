const headerEl = $('DIV#toggle_header');
headerEl.click(function () {
  $('header').toggleClass('green');
  $('header').toggleClass('red');
});
