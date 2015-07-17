var suburbsContent = $('.suburb-content .table-responsive');
var suburbsNav = $('ul.suburbs');
var suburbs = suburbsNav.children('li');
var suburbHeader = $('.suburb-header');
var suburbNameHidden = $('#suburb-name-hidden');
var suburbNumberHidden = $('#suburb-number-hidden');
var suburbComment = $('#suburb-comment');

var suburbCommentWrap = $('.suburb-comment-wrap');
var suburbCommentText = $('.suburb-comment-text');
var btnSuburbComment = $('#btn-suburb-comment');


suburbs.click( function(e) {
	// Вычисляем индекс элемента на который кликнули
	suburbs.each( function(index) {
		if(this === e.currentTarget)
			i = index;
	});

	// Делаем активным тот класс на который кликнули
	suburbs.removeClass('active');
	var text = $(suburbs[i]).addClass('active').text();

	// Меняем значния текущего сабёрба
	suburbNumberHidden.val( suburbsInfo[i][0] );
	suburbNameHidden.val( suburbsInfo[i][1] );
	suburbComment.val( suburbsInfo[i][2] );
	suburbHeader.text( suburbsInfo[i][1] );
	suburbCommentText.text( suburbsInfo[i][2] );

	// Оставляем видимым только соответствующий suburb'у контент
	suburbsContent.removeClass('table-active').addClass('hidden');
	$(suburbsContent[i]).removeClass('hidden').addClass('table-active');
});


btnSuburbComment.click( function(e) {
	if(suburbCommentWrap.hasClass('hidden')) {
		suburbCommentWrap.removeClass('hidden');
	}
	else suburbCommentWrap.addClass('hidden');

	if(suburbCommentText.hasClass('hidden')) {
		suburbCommentText.removeClass('hidden');
	}
	else suburbCommentText.addClass('hidden');
});

var doneButtons = $('.tc-btn-done');
/*doneButtons.click( function(event) {

	var target = $(event.target);
	var tr = target.closest('td').siblings();

	if( tr.hasClass('disabled') ) 
	{
		 tr.removeClass('disabled');
		 target.html('<span class="glyphicon glyphicon-ok"></span> Done');
	}
	else 
	{
		tr.addClass('disabled');
		target.html('<span class="glyphicon glyphicon-remove"></span> Undo');
	}
});
doneButtons.click( function(event) {
	$(event.target).closest('tr').toggle(300);
});*/

doneButtons.click( function(event) {
	var target = $(event.target);
	target.closest('td').siblings().addClass('disabled');
	var content = new Date().toLocaleDateString();
	target.closest('td').addClass('disabled').html(content);
});