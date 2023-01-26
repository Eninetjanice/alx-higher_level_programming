// This script fetches and prints how to say “Hello” depending on the language
// The language code will be the value entered in the
// tag INPUT#language_code (ex: es, fr, en etc.) &
// translation fetched when the user clicks on INPUT#btn_translate
// OR presses ENTER when the focus is on INPUT#language_code

$('document').ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  const translate = $('INPUT#btn_translate');
  const enter = $('INPUT#language_code');

  if (translate.click() || enter.click()) {
    (function () {
      $.get(url + $.param({ lang: enter.val() }), function (data) {
        $('DIV#hello').html(data.hello);
      });
    });
  }
});
