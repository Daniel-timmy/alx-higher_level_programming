$(document).ready(function () {
    $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function(data, txtStatus)
    {
        $('DIV#hello').text(data.hello)
    });
});