const headerEl = $('DIV#add_item');
headerEl.click(function () {
  $('UL.my_list').append('<li>Item</li>');
});
