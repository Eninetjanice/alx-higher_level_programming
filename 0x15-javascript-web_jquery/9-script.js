// JavaScript script that displays hello in French

const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
$(() => {
  $.get(url, (data, textStatus) => {
    if (textStatus === 'success') {
      $('DIV#hello').text(data.hello);
    }
  });
});
