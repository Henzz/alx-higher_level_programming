const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$(document).ready(function () {
  $.get(url, function (data, status) {
    $('DIV#hello').text(data.hello);
  });
});
