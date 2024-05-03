$(document).ready(function () {
  $('INPUT#language_code').on('keypress', function (e) {
    if (e.which === 13) {
      translateLang();
    }
  });
  $('INPUT#btn_translate').click(function () {
    translateLang();
  });
});

function translateLang () {
  const langCode = $('INPUT#language_code').val();
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + langCode;
  $.get(url, function (data, status) {
    $('DIV#hello').text(data.hello);
  });
}
