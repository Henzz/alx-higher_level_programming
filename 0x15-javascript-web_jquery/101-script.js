$(document).ready(function () {
  const listEl = $('UL.my_list');
  // Adds new element
  $('DIV#add_item').click(function () {
    listEl.append('<li>Item</li>');
  });
  // Removes last child element
  $('DIV#remove_item').click(function () {
    $('UL.my_list li:last-child').remove();
  });
  // Clears all child elements
  $('DIV#clear_list').click(function () {
    listEl.empty();
  });
});
